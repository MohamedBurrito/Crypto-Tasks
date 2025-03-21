import random
import string

def cipher_encryption():
    msg = input("Enter Plain Text: ").replace(" ", "").upper()
    key = input("Enter keyword: ").upper()

    # Assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    print("Keyword:", key)
    print("Key Numbers:", kywrd_num_list)
    print("-------------------------")

    # Padding the message to fit the grid size with random alphabets if needed
    extra_letters = len(msg) % len(key)
    if extra_letters != 0:
        padding_length = len(key) - extra_letters
        msg += ''.join(random.choices(string.ascii_uppercase, k=padding_length))

    num_of_rows = len(msg) // len(key)

    # Filling the grid
    arr = [[msg[row * len(key) + col] for col in range(len(key))] for row in range(num_of_rows)]

    print("Grid:")
    for row in arr:
        print(" ".join(row))

    # Sorting columns based on keyword numeric values
    sorted_indices = sorted(range(len(key)), key=lambda x: kywrd_num_list[x])

    # Forming the ciphertext by reading columns in sorted order
    cipher_text = "".join("".join(arr[row][idx] for row in range(num_of_rows)) for idx in sorted_indices)

    print("\nCipher Text:", cipher_text)


def keyword_num_assign(key):
    """
    Assigns numbers to keyword letters based on alphabetical order.
    Example: '4312567' -> [3, 1, 2, 0, 4, 5, 6]
    """
    return [sorted(key).index(k) for k in key]


def cipher_decryption():
    msg = input("Enter Cipher Text: ").replace(" ", "").upper()
    key = input("Enter keyword: ").upper()

    kywrd_num_list = keyword_num_assign(key)
    num_of_rows = len(msg) // len(key)

    # Sorting columns based on keyword numeric values
    sorted_indices = sorted(range(len(key)), key=lambda x: kywrd_num_list[x])

    # Filling the grid in the sorted column order
    arr = [[None] * len(key) for _ in range(num_of_rows)]
    pos = 0
    for idx in sorted_indices:
        for row in range(num_of_rows):
            arr[row][idx] = msg[pos]
            pos += 1

    print("\nGrid:")
    for row in arr:
        print(" ".join(row))

    # Forming the plaintext by reading row-wise
    plain_text = "".join("".join(arr[row][col] for col in range(len(key))) for row in range(num_of_rows))
    print("\nPlain Text:", plain_text.replace(".", ""))


def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose (1 or 2): "))
    if choice == 1:
        print("Encryption")
        cipher_encryption()
    elif choice == 2:
        print("Decryption")
        cipher_decryption()
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()
