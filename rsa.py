# This is an RSA Cryptosystem. The user will enter the public key(n,e) and the encrypted code. Then the program will
# use prime factorization, linear algebra and modular arithmetic to find the private key(x) and decrypt the given code

from math import gcd  # gcd used for Euler Totient function
from sympy import mod_inverse as minv  # minv to find private key, the inverse of e modulo phi


def rsa():  # driver function
    option = input("Press <enter> to continue or q to quit: ")
    while option != 'q':  # while loop used for 'infinite' user entries
        card = int(input("\nHow many items are in your legend? "))
        while card == 0:  # ensuring non-empty legend
            print("Invalid input, legend must be non-empty")
            card = int(input("\nHow many items are in your legend? "))
        public_key = input("\nEnter the public key: ").split()  # public key list
        while len(public_key) != 2:  # ensuring proper length of public key (n,e) is entered
            print("Invalid public key, must have 2 elements")
            public_key = input("\nEnter the public key: ").split()
        code_block = input("Enter the encrypted code: ").split()  # code block list
        print(f"\nPhi: {phi(public_key)}")  # calling phi function
        if private_key(public_key) != 0:
            print(f"Private key: {private_key(public_key)}\n")  # calling private key function
        else:
            print("Private key does not exist")
        decrypt(code_block, private_key(public_key), public_key, legend(card))  # calling decrypt function
        option = input("\nPress <enter> to continue or q to quit: ")
    print("\nThank you for using RSA Cryptosystem.")  # break out of while loop when user enters 'q'


def legend(card):  # function populates a dictionary and returns the legend to be called upon
    legend = dict()
    for i in range(1, card + 1):
        key = input(f"Enter key {i}: ")
        value = input(f"Enter value {i}: ").upper()
        legend[key] = value
    return legend


def phi(public_key):
    count = 0  # Euler totient value
    n = int(public_key[0])
    for j in range(1, n + 1):  # finding the number of elements coprime to n of N/nN
        if gcd(j, n) == 1:
            count += 1  # increment count by 1
        else:
            continue  # ignore elements of N/nN if gcd != 1
    return count


def private_key(public_key):
    x = 0  # private key
    e = int(public_key[1])
    try:
        x = minv(e, phi(public_key))  # multiplicative inverse of e modulo phi (x * e == 1modphi)
    except Exception as err:  # try and except used in case user inputs an e that is not invertible modulo phi
        print(f"Error: {err}")
    return x


def decrypt(code_block, private_key, public_key, legend):
    for code in code_block:  # looping through every code in code block list
        if private_key != 0:  # x is never 0 when the try statement executes because 0 is never invertible
            code = int(code)
            d_code = str((code ** private_key) % int(public_key[0]))  # raise code to the power of the
            # private key and reduce modulo n to decrypt
            if len(d_code) == 1:
                d_code = '0' + d_code  # in case d_code is a single digit
            for k in range(len(d_code)):
                print(f"Decrypted code for {code}: {d_code[k]} ==> {legend[d_code[k]]}")  # translating decrypted
                # code key to value in legend
        else:
            print("Error")


if __name__ == '__main__':  # special variable __name__
    rsa()  # call to rsa
