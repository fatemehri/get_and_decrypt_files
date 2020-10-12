from ftplib import FTP
import pyAesCrypt
import os
import datetime
import glob


def get_files():
    path = 'livestock/'
    ftp = FTP()
    ftp.connect('', 5021)
    ftp.login('admin', '')
    ftp.cwd(path)
    ftp.pwd()
    files_name = ftp.nlst()

    for name in files_name:
        ftp.retrbinary("RETR " + name, open(name, 'wb').write)


def dec_files():
    bufferSize = 64 * 1024
    password = ""
    for name in glob.glob('*.aes'):
        pyAesCrypt.decryptFile(name, "dec_files/{}.csv".format(name.split('.')[0]), password, bufferSize)


if __name__ == "__main__":
    get_files()
    dec_files()
