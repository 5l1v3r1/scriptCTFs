#!/usr/bin/python3
from zipfile import ZipFile


def banner():
    """
    This function print a fancy banner
    """
    print("\033[32m")
    print("         ___          _         ___ _                     _   _")
    print("        | _ )_ _ _  _| |_ ___  | __| |_ ___ _ _ _ _  __ _| | | |   ___  ___ _ __")
    print("        | _ \ '_| || |  _/ -_) | _||  _/ -_) '_| ' \/ _` | | | |__/ _ \/ _ \ '_ \\")
    print("        |___/_|  \_,_|\__\___| |___|\__\___|_| |_||_\__,_|_|_|____\___/\___/ .__/")
    print("                                                        |___|            |_|")
    print("\033[0m")


def getArchiveName(zip_file):
    """
    This function return the list of names in the archive.
    """

    with ZipFile(zip_file, 'r') as f:
        names = f.namelist()

    return str(names[0])


def unzipArchives(zip_file, password):
    """
    This function extract compressed files in a ZIP archive
    """
    with ZipFile(zip_file) as archive:
        archive.extractall(pwd=bytes(password, "utf8"))


def main():

    zip_file = "Eternal_Loop.zip"
    password = "hackthebox"

    banner()

    while True:
        print("[+]Extracting \033[35m {0} \033[0m with password \033[36m {1}\
              \033[0m".format(zip_file, password))
        unzipArchives(zip_file, password)

        zip_file = getArchiveName(zip_file)
        password = getArchiveName(zip_file)
        password = password.replace('.zip', '').replace('\n', '')

if __name__ == "__main__":
    main()
