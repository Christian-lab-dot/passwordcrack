import hashlib
import bcrypt
import sys

f = open('passwords.txt', 'r')

def plainCrack(password):
    for pw in f:
        passStrip = pw.strip()
        if passStrip == password:
            print('password found!\npassword is ' + passStrip)
            return
    print('password not found')

def md5Crack(hash):
    for pw in f:
        passw = pw.strip()
        word = pw.encode('utf-8')
        hashStrip = hashlib.md5(word.strip()).hexdigest()
        if hashStrip == hash:
            print('password found!\npassword is ' + passw)
            return
    print('password not found')

def bcryptCrack(hash):
    for pw in f:
        passw = pw.strip()
        if bcrypt.checkpw(passw.encode('utf-8'), hash.encode('utf-8')):
            print('password found!\npassword is ' + passw)
            return
    print('password not found')

def sha256Crack(hash):
    for pw in f:
        passw = pw.strip()
        word = pw.encode('utf-8')
        hashStrip = hashlib.sha256(word.strip()).hexdigest()
        if hashStrip == hash:
            print('password found!\npassword is ' + passw)
            return
    print('password not found')

def main():
    #python3 cracked.py hashtype hash
    args = sys.argv[1:]
    #1 is hash type, 2 is the hash/password,
    if len(args) == 3:
        if args[1] == 'plain':
            plainCrack(args[2])
        if args[1] == 'md5':
            md5Crack(args[2])
        if args[1] == 'bcrypt':
            bcryptCrack(args[2])
        if args[1] == 'sha256':
            sha256Crack(args[2])

    choice = input('what do?\n[1] plainCrack\n[2] md5Crack\n[3] bcryptCrack\n[4] sha256Crack\n')
    if choice == '1':
        plainCrack(input('Enter password\n'))
    if choice == '2':
        md5Crack(input('Enter md5 hash\n'))
    if choice == '3':
        bcryptCrack(input('Enter bcrypt hash\n'))
    if choice == '4':
        sha256Crack(input('Enter sha256 hash\n'))

if __name__ == '__main__':
    main()