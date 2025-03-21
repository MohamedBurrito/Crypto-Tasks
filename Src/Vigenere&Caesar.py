import string

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def vigenere_cipher(text, key, encrypt=True):
    key = key.lower()
    key_length = len(key)
    result = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('a')
            shift = shift if encrypt else -shift
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char
    return result

def main():
    print("Choose a cipher:\n1. Caesar Cipher\n2. Vigenère Cipher")
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))
        mode = input("Encrypt or Decrypt? (e/d): ")
        encrypt = mode.lower() == 'e'
        print("Result:", caesar_cipher(text, shift, encrypt))
    
    elif choice == "2":
        text = input("Enter the text: ")
        key = input("Enter the key: ")
        mode = input("Encrypt or Decrypt? (e/d): ")
        encrypt = mode.lower() == 'e'
        print("Result:", vigenere_cipher(text, key, encrypt))
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
