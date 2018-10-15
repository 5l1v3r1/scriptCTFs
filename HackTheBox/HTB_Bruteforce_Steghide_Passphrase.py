#!/usr/bin/python3
# Author: https;//github.com/mohabaks
# Description: Quick script to brute-force steghide passphrase
# Dependecies: steghide

import argparse
import subprocess

from threading import Thread


def steghideCracker(password, stegofile):
    """
    Brute-Force steghide passphrase

    This function brute-force steghide passphrase using a given file.

    Parameters
    ----------
        password: The passphrase
        stegofile: Selected stego file

    Returns
    -------
        password: Return password used to crack the file

    """
    steghide = ["steghide", "extract", "-sf", stegofile, "-p", password]

    status = subprocess.run(args=steghide)
    if status.returncode != 1:
        print("\033[32m Successfully brute-foce \033[35m{0}\033[0m passphrase:\
              {1}\033[36m{1}\033[0m".format(stegofile, password))
        exit(0)


def main():
    parse = argparse.ArgumentParser(usage='%(prog)s [options]',
                                    description="A simple program to brute-\
                                    force steghide passhrase",
                                    epilog="Happy hacking ;)")
    parse.add_argument('-d', '--dictionary', help='Specify a dictionary file',
                       required=True, metavar='', dest='passfile',
                       type=argparse.FileType('r', encoding='latin-1'))
    parse.add_argument('-sf', '--stegofile', help='Specify a stego file',
                       required=True, metavar='', dest='stegofile')

    options = parse.parse_args()

    dict_file = options.passfile.read().splitlines()
    stegofile = options.stegofile

    for password in dict_file:
        t = Thread(target=steghideCracker, args=(password, stegofile))
        t.start()


if __name__ == "__main__":
    main()
