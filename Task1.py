def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters unchanged

    return result


def main():
    print("=== Caesar Cipher ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    mode = input("Choose mode (encrypt/decrypt): ").lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
        return

    output = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed): {output}")


if __name__ == "__main__":
    main()
