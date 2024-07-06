## Packager

## cc: okzyrox

import windows
from packages.list import PACKAGES as package_list
import log
import sys, os, colorama, random, time, requests
from tqdm import tqdm

PACKAGER_VERSION = "0.0.1a"

DEFAULT_INSTALL_PATH = "C:\\Program Files\\packager\\"
DEFAULT_DOWNLOAD_PATH = "https://raw.githubusercontent.com/okzyrox/packager/main/packager/packages/"
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
    
    response = requests.get(download_path, stream=True)

    with open("downloaded/" + package_name, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)

def install(package_name, path=DEFAULT_INSTALL_PATH):
    install_path = path + "\\packages\\"
    
    if package_name not in package_list:
        log.output("Package not found: " + package_name, "RED", 1)
        log.output("ERR: package not found", "RED", 1)
        return

    if not os.path.exists(install_path):
        #os.makedirs(install_path)
        log.output("First Install - making paths: " + install_path, "CYAN", 2)
    

    if os.path.exists(install_path + package_name):
        log.output("Package already installed: " + package_name, "YELLOW", 1)
        log.output("ERR: package already installed", "YELLOW", 1)
        return
    
    #if sys.platform == "win32":
    if not windows.is_in_path(install_path):
        #windows.add_to_path(install_path)
        log.output("First Install - adding paths: " + install_path, "CYAN", 2)
    
    package = package_list["test"]
    install_name = package["name"] + "-" + package["version"]
    print("----------------------------------------")
    log.output("Installing: " + install_name, "GREEN", 1)
    download(package_name, package["version"])

    
def main():
    #if sys.platform == "win32":
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
            case "help":
                print("Commands:")
                print("  install <package>")
                print("  uninstall <package>")
                print("  list")
                print("  config")
                print("  help")
                print("  docs <package>")
                print("  docs <package> view <file>")
                print()
            case "list":
                install_path = DEFAULT_INSTALL_PATH + "\\packages\\"
                if not os.path.exists(install_path):
                    #os.makedirs(install_path)
                    log.output("You have no packages installed!", "WHITE", 1)
            case other:
                log.output("Command not implemented", "YELLOW", 1)


main()