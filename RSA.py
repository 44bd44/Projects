# This is an RSA Cryptosystem. The user will enter the public key(n,e) and the encrypted code. Then the program will
# use prime factorization, linear algebra and modular arithmetic to find the private key(x) and decrypt the given code

from math import gcd  # gcd used for Euler Totient function
from sympy import mod_inverse as minv  # minv to find private key, the inverse of e modulo phi


def main():  # driver function
    option = input("Press <enter> to continue or press q to quit: ")
    while option != 'q':  # while loop used for 'infinite' user entries
        legend = dict()
        card = int(input("\nHow many items are in your legend? "))
        while card == 0:  # ensuring non-empty legend
            print("Invalid input, legend must be non-empty")
            card = int(input("\nHow many items are in your legend? "))
        for i in range(1, card + 1):  # populating legend
            key = input(f"Enter key {i}: ")
            value = input(f"Enter value {i}: ").upper()
            legend[key] = value
        print(legend)
        public_key = input("\nEnter the public key: ").split()  # public key list
        while len(public_key) != 2:  # ensuring proper length of public key (n, e) entered
            print("Invalid public key, try again")
            public_key = input("\nEnter the public key: ").split()
        code_block = input("Enter the encrypted code: ").split()  # code block list
        n = int(public_key[0])  # indexing public key for n and e
        e = int(public_key[1])
        RSA(n, e, code_block, legend)  # calling RSA function
        option = input("\nPress <enter> to continue or press q to quit: ")
    print("\nThank you for using RSA Cryptosystem.")  # break out of while loop after user enters 'q'


def RSA(n, e, code_block, legend):
    x = 0  # private key
    phi = 0  # Euler totient value
    for j in range(1, n + 1):  # finding the number of elements coprime to n of N/nN
        if gcd(j, n) == 1:
            phi += 1  # increment phi by 1
        else:
            continue  # ignore elements of N/nN if gcd != 1
    print(f"\nPhi: {phi}")
    try:
        x = minv(e, phi)  # multiplicative inverse of e modulo phi (x * e == 1modphi)
        print(f"Private key: {x}")
    except Exception as err:  # try and except used in case user inputs an e that is not invertible modulo phi
        print(f"Error: {err}")
    for code in code_block:  # looping through every code in code block list
        if x != 0:  # x is never 0 when the try statement executes because 0 is never invertible
            code = int(code)
            d_code = str((code ** x) % n)  # raise code to the power of the
            # private key
            # and reduce modulo n to decrypt
            if len(d_code) == 1:  # in case d_code is a single digit
                d_code = '0' + d_code
            for k in range(len(d_code)):
                print(f"Decrypted code for {code}: {d_code[k]} ==> {legend[d_code[k]]} ")  # translating decrypted
                # code key to value in legend
        else:
            print("Error")  # x is 0 when there is an exception


if __name__ == '__main__':  # special variable __name__
    main()  # call to main
