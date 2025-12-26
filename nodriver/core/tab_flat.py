
from ..core.connection_flat import Connection
from .. import cdp


class Tab:

    def __init__(self, target: cdp.target.TargetInfo, browser: "nodriver.core.browser.Browser" = None, **kwargs ):
        self.target = target
        self.browser = browser









