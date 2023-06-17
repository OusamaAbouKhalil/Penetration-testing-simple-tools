#generate possiple million password from the victim information and save it in a file

import itertools
import string

#enter the victim name
Name = input("\n\n\n\tEnter the victim name: ")
print("\n==========================================================\n")

def generate_passwords(victim_info):
    possible_passwords = []
    for i in range(1, len(victim_info) + 1):
        for combination in itertools.permutations(victim_info, i):
            possible_passwords.append(''.join(combination))
    return possible_passwords

def save_passwords(possible_passwords):
    with open(f'{Name}.txt', 'w') as file:
        for password in possible_passwords:
            file.write(password + '\n')

def main():
    victim_info = []
    print('\nEnter the victim information. Enter \'d\' when finished.')
    while True:
        info = input()
        if info == 'd':
            break
        #delete the spaces from the info
        info = info.replace(' ', '')
        victim_info.append(info)
    possible_passwords = generate_passwords(victim_info)
    save_passwords(possible_passwords)


if __name__ == '__main__':
    main()