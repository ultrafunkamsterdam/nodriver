import logging
import os
import pathlib
import sys
import tempfile
from typing import Union, List, Optional

from ._contradict import ContraDict

__all__ = [
    "Config",
    "find_chrome_executable",
    "temp_profile_dir",
    "is_root",
    "is_posix",
    "PathLike",
]

logger = logging.getLogger(__name__)
is_posix = sys.platform.startswith(("darwin", "cygwin", "linux", "linux2"))

PathLike = Union[str, pathlib.Path]
AUTO = None


class Config(ContraDict):
    """ """

    def __init__(
            self,
            user_data_dir: Optional[PathLike] = AUTO,
            headless: Optional[bool] = False,
            browser_executable_path: Optional[PathLike] = AUTO,
            browser_args: Optional[List[str]] = AUTO,
            sandbox: Optional[bool] = True,
            lang: Optional[str] = "en-US,en;q=0.9",
            **kwargs: dict,
    ):
        """
        creates a config object.
        Can be called without any arguments to generate a best-practice config, which is recommended.

        calling the object, eg :  myconfig() , will return the list of arguments which
        are provided to the browser.

        additional arguments can be added using the :py:obj:`~add_argument method`

        Instances of this class are usually not instantiated by end users.

        :param user_data_dir: the data directory to use
        :param headless: set to True for headless mode
        :param browser_executable_path: specify browser executable, instead of using autodetect
        :param browser_args: forwarded to browser executable. eg : ["--some-chromeparam=somevalue", "some-other-param=someval"]
        :param sandbox: disables sandbox
        :param autodiscover_targets: use autodiscovery of targets
        :param lang: language string to use other than the default "en-US,en;q=0.9"
        :param kwargs:

        :type user_data_dir: PathLike
        :type headless: bool
        :type browser_executable_path: PathLike
        :type browser_args: list[str]
        :type sandbox: bool
        :type lang: str
        :type kwargs: dict
        """

        if not browser_args:
            browser_args = []

        custom_data_dir = bool(user_data_dir)
        if not user_data_dir:
            user_data_dir = temp_profile_dir()

        if not browser_executable_path:
            browser_executable_path = find_chrome_executable()

        self.browser_args = browser_args
        self.user_data_dir = user_data_dir
        self.custom_data_dir = custom_data_dir
        self.browser_executable_path = browser_executable_path
        self.headless = headless
        self.sandbox = sandbox
        self.host = None
        self.port = None

        # when using posix-ish operating system and running as root
        # you must use no_sandbox = True, which in case is corrected here
        if is_posix and is_root() and sandbox:
            logger.info("detected root usage, autoo disabling sandbox mode")
            self.sandbox = False

        self.autodiscover_targets = True
        self.lang = lang

        # other keyword args will be accessible by attribute
        self.__dict__.update(kwargs)
        super().__init__()

    def __getattr__(self, item):
        if item not in self.__dict__:
            return

    def __call__(self):
        # the host and port will be added when starting
        # the browser, as by the time it starts, the port
        # is probably already taken
        args = []
        args += ["--user-data-dir=%s" % self.user_data_dir]
        args += ["--remote-allow-origins=*"]
        args += ["--no-first-run"]
        args += ["--no-service-autorun"]
        args += ["--no-default-browser-check"]
        args += ["--homepage=about:blank"]
        args += ["--no-pings"]
        args += ["--password-store=basic"]
        args += ["--disable-infobars"]
        args += ["--disable-breakpad"]
        args += ["--disable-component-update"]
        args += ["--disable-backgrounding-occluded-windows"]
        args += ["--disable-renderer-backgrounding"]
        args += ["--disable-background-networking"]
        args += ["--disable-dev-shm-usage"]

        if self.browser_args:
            args.extend([arg for arg in self.browser_args if arg not in args])
            # args.extend(self.browser_args)
        if self.headless:
            args.append("--headless=new")
        if not self.sandbox:
            args.append("--no-sandbox")
        if self.host:
            args.append("--remote-debugging-host=%s" % self.host)
        if self.port:
            args.append("--remote-debugging-port=%s" % self.port)
        return args

    def add_argument(self, arg: str):
        if any(
                x in arg.lower()
                for x in [
                    "headless",
                    "data-dir",
                    "data_dir",
                    "no-sandbox",
                    "no_sandbox",
                    "lang",
                ]
        ):
            raise ValueError(
                '"%s" not allowed. please use one of the attributes of the Config object to set it'
                % arg
            )
        self.browser_args.append(arg)


def is_root():
    """
    helper function to determine if user trying to launch chrome
    under linux as root, which needs some alternative handling
    :return:
    :rtype:
    """
    import ctypes, os

    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0


def temp_profile_dir():
    """generate a temp dir (path)"""
    path = os.path.normpath(tempfile.mkdtemp(prefix="uc_"))
    return path


def find_chrome_executable(return_all=False):
    """
    Finds the chrome, beta, canary, chromium executable
    and returns the disk path
    """
    candidates = []
    if is_posix:
        for item in os.environ.get("PATH").split(os.pathsep):
            for subitem in (
                    "google-chrome",
                    "chromium",
                    "chromium-browser",
                    "chrome",
                    "google-chrome-stable",
            ):
                candidates.append(os.sep.join((item, subitem)))
        if "darwin" in sys.platform:
            candidates += [
                "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                "/Applications/Chromium.app/Contents/MacOS/Chromium",
            ]

    else:
        for item in map(
                os.environ.get,
                ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA", "PROGRAMW6432"),
        ):
            if item is not None:
                for subitem in (
                        "Google/Chrome/Application",
                        "Google/Chrome Beta/Application",
                        "Google/Chrome Canary/Application",
                ):
                    candidates.append(os.sep.join((item, subitem, "chrome.exe")))
    rv = []
    for candidate in candidates:
        if os.path.exists(candidate) and os.access(candidate, os.X_OK):
            logger.debug("%s is a valid candidate... " % candidate)
            rv.append(candidate)
        else:
            logger.debug(
                "%s is not a valid candidate because don't exist or not executable "
                % candidate
            )

    winner = None

    if return_all and rv:
        return rv

    if rv and len(rv) > 1:
        # assuming the shortest path wins
        winner = min(rv, key=lambda x: len(x))

    elif len(rv) == 1:
        winner = rv[0]

    if winner:
        return os.path.normpath(winner)

    raise FileNotFoundError(
        "could not find a valid chrome browser binary. please make sure chrome is installed."
        "or use the keyword argument 'browser_executable_path=/path/to/your/browser' "
    )
