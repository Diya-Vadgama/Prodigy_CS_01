def caesar_cipher(text, shift, mode):
    if mode == "decrypt":
        shift = -shift
    
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result


def main():
    print("Caesar Cipher Program")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            mode = 'encrypt'
        elif choice == '2':
            mode = 'decrypt'
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        text = input("Enter the message: ").strip()
        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid input for shift. Please enter an integer.")
            continue
        
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
