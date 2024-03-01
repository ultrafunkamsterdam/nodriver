from pathlib import Path
import re
from packaging.version import Version


import subprocess

docs = Path("docs")
example = Path("example")
dist = Path("dist")
egg = Path("nodriver.egg-info")


def find_file(pattern: str, root: str = ".", recursive: bool = True):
    root = Path(root).resolve()
    glob = root.glob if not recursive else root.rglob
    for o in glob(pattern):
        if o.is_file():
            return o


def find_replace_in_file(file, search, repl):
    file = Path(file).resolve()
    binary = False
    try:
        content = file.read_text()
    except UnicodeDecodeError:
        content = file.read_bytes()
        binary = True
    if binary:
        try:
            search = search.encode()
            repl = repl.encode()
        except:
            pass
        file.write_bytes(re.sub(search, repl, content))
    else:
        file.write_text(re.sub(search, repl, content))


def remove(path):
    path = Path(path).resolve()
    if path.is_file():
        path.unlink()
        return True
    for item in path.rglob("*"):
        if item.is_file():
            item.unlink()
            continue
        remove(item)
    path.rmdir()
    return True


def change_version():

    current = Version(get_version(project_file))
    new_version = None
    while not new_version:
        try:
            new_version = Version(input(f"change version (current: {current})? : "))
        except:
            continue
    if new_version != current:
        find_replace_in_file(
            project_file, "version = [\"']([^\s]+)[\"']", f'version = "{new_version}"'
        )


def get_version(project_file: Path):
    content = project_file.read_text()
    return re.search("version = [\"']([^\s]+)[\"']", content)[1]


project_file = find_file("pyproject.toml")

subprocess.run("make.bat html", shell=True, cwd="./docs")
subprocess.run("make.bat markdown", shell=True, cwd="./docs")
subprocess.run("copy docs\\_build\\markdown\\README.md .", shell=True)
change_version()
subprocess.run("black nodriver/core *.py")
subprocess.run("git add docs nodriver pyproject.toml example README.md")
subprocess.run("git status")
commit = input("commit?:")
if commit:
    subprocess.run(f'git commit -m "{commit}"')

    subprocess.run("python -m build")
    subprocess.run("twine upload dist\\*")
