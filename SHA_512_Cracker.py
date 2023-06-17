#7SHA-512 (Secure Hash Algorithm 512-bit) password cracking program

import hashlib


def main():
    print("\n")
    print("\t\t\tPassword Cracker SHA-512 (Secure Hash Algorithm 512-bit)\n")
    print("============================================================================================\n")
    print("Enter the hash value and wordlist file name\n")
    print("Note that the hash value should be in the SHA-512 format\n")
    print("============================================================================================\n")
    hash = input("Enter hash value: ")
    wordlist = input("Enter wordlist file name: ")
    try:
        pass_file = open(wordlist, "r")
    except:
        print("No file found")
        quit()
    for word in pass_file:
        enc_word = word.encode('utf-8')
        digest = hashlib.sha512(enc_word.strip()).hexdigest()
        if digest == hash:
            print("Password found: " + word)
            break
        else:
            print("Password not found")

main()