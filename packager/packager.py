## Packager

## cc: okzyrox

import windows
from packages.list import PACKAGES as package_list
import log
import sys, os, colorama, random, time, requests
from tqdm import tqdm

PACKAGER_VERSION = "0.0.1a"

DEFAULT_INSTALL_PATH = "C:\\Program Files\\packager\\"
DEFAULT_DOWNLOAD_PATH = "https://github.com/okzyrox/packager/tree/main/packager-packages/packages/"
# considering here or C:\packager\ ?
# inside the folder is:
##packager/
##├─ packages/..
##├─ installed_packages.json
##├─ packager.exe
##├─ packager.cfg

currently_installing = False
currently_installing_package = ""


def download(package_name, version):
    log.output("ERR: not implemented lmao", "RED", 1)
    log.output("or is it...", "RED", 1)

    if package_name not in package_list:
        log.output("Package not found: " + package_name, "RED", 1)
        log.output("ERR: package not found", "RED", 1)
        return
    
    download_path = DEFAULT_DOWNLOAD_PATH + package_name
    log.output("Downloading: " + package_name + " v" + version, "GREEN", 2)
    log.output("from: " + download_path, "GREY", 2)
    check = requests.get(url=download_path)

    if check.status_code == 404:
        log.output("Package not found: " + package_name, "RED", 2)  
        return

def install(package_name, path=DEFAULT_INSTALL_PATH):
    install_path = path + "\\packages\\"
    
    if package_name not in package_list:
        log.output("Package not found: " + package_name, "RED", 1)
        log.output("ERR: package not found", "RED", 1)
        return

    if os.path.exists(install_path + package_name):
        log.output("Package already installed: " + package_name, "YELLOW", 1)
        log.output("ERR: package already installed", "YELLOW", 1)
        return
    
    if not os.path.exists(install_path):
        #os.makedirs(install_path)
        log.output("First Install - making paths: " + install_path, "CYAN", 2)
    if sys.platform == "win32":
        if not windows.is_in_path(install_path):
            #windows.add_to_path(install_path)
            log.output("First Install - adding paths: " + install_path, "CYAN", 2)
    
    package = package_list["test"]
    install_name = package["name"] + "-" + package["version"]
    print("----------------------------------------")
    log.output("Installing: " + install_name, "GREEN", 1)
    for i in tqdm(range(0, 100), desc=install_name):
        time.sleep(0.05)
    download(package_name, package["version"])

    
def main():
    if sys.platform == "win32":
        colorama.just_fix_windows_console()
    if len(sys.argv) < 2:
        print("Packager v" + PACKAGER_VERSION)
        print()
        print("Commands:")
        print("  install <package>")
        print("  uninstall <package>")
        print("  list")
        print("  config")
        print("  help")
        print("  docs <package>")
        print("  docs <package> view <file>")
        print()
    else:
        command = sys.argv[1]
        match command:
            case "install":
                if len(sys.argv) < 3:
                    print("ERR: missing package name")
                    return
                install(sys.argv[2])
                

main()