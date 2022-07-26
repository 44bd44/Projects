from math import gcd
from sympy import mod_inverse as minv


def main():
    option = input("Press <enter> to continue or press q to quit: ")
    while option != 'q':
        public_key = input("\nEnter the public key: ").split()
        while len(public_key) != 2:
            print("Invalid public key, try again")
            public_key = input("\nEnter the public key: ").split()
        code_block = input("Enter the encrypted code: ").split()
        n = int(public_key[0])
        e = int(public_key[1])
        RSA(n, e, code_block)
        option = input("\nPress <enter> to continue or press q to quit: ")
    print("\nThank you for using RSA Cryptosystem.")


def RSA(n, e, code_block):
    x = 0
    phi = 0
    for j in range(1, n + 1):
        if gcd(j, n) == 1:
            phi += 1
        else:
            continue
    print(f"Phi: {phi}")
    try:
        x = minv(e, phi)
        print(f"Private key: {x}")
    except Exception as err:
        print(f"Error: {err}")
    for code in code_block:
        code = int(code)
        if x != 0:
            print(f"Decrypted code for {code}: {int((code ** x) % n)}")
        else:
            print("Error")


if __name__ == '__main__':
    main()
