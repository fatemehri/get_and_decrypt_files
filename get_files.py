from ftplib import FTP
import pyAesCrypt
import os
import datetime
import glob


def get_files():
    path = 'livestock/'
    ftp = FTP()
    ftp.connect('partow.rdps.ir', 5021)
    ftp.login('admin', 'A@123456')
    ftp.cwd(path)
    ftp.pwd()
    files_name = ftp.nlst()

    for name in files_name:
        print(name)
        ftp.retrbinary("RETR " + name, open(name, 'wb').write)


def dec_files():
    bufferSize = 64 * 1024
    password = "foopassword"
    for name in glob.glob('*.aes'):
        print(name)
        pyAesCrypt.decryptFile(name, "dw_ftp_files/dec_files/{}.csv".format(name.split('.')[0]), password, bufferSize)


if __name__ == "__main__":
    get_files()
    dec_files()
