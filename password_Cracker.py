#Crack password hash using wordlist brute force
import hashlib


def main():
    print("\n")
    print("\t\t\t\tPassword Cracker\n")
    print("============================================================================================\n")
    print("Enter the hash value and wordlist file name\n")
    print("Note that the hash value should be in the md5 format\n")
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
        digest = hashlib.md5(enc_word.strip()).hexdigest()
        if digest == hash:
            print("Password found: " + word)
            break
        else:
            print("Password not found")

main()
