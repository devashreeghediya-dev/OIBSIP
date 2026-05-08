import random
import string
def generate_password(length, use_letters, use_digits, use_symbols):
    characters= ""
    if use_letters:
        characters +=string.ascii_letters
    if use_digits:
        characters +=string.digits
    if use_symbols:
        characters +=string.punctuation
    if not characters:
        return "Error: No character set selected."
    password=''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("=== Random Password generator ===")
    try:
        length=int(input("Enter passwrod length:"))
        if length<=0:
            print("Invald length.")
            return
        use_letters=input("Include letters? (y/n): ").lower() == 'y'
        use_digits=input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols=input("Include symbols? (y/n): ").lower() == 'y'
        password=generate_password(length, use_letters, use_digits, use_symbols)
        print("\nGenerated Password:", password)
    except:
        print("Invalid input.")
if __name__ == "__main__":
    main()
