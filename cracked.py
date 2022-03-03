import hashlib
import bcrypt

f = open('passwords.txt', 'r')

def plainCrack(password):
    for pw in f:
        passStrip = pw.strip()
        if passStrip == password:
            print('password found!\npassword is ' + password)
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


def main():
    choice = input('what do?\n[1] plainCrack\n[2] md5Crack\n')
    if choice == '1':
        plainCrack(input('input password\n'))
    if choice == '2':
        md5Crack(input('input md5 hash\n'))

if __name__ == '__main__':
    main()