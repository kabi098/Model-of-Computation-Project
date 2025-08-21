import re
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def validate_email_regex(email):
    return EMAIL_REGEX.fullmatch(email) is not None

def validate_email_fa(email):
    state = 0

    for char in email:
        if state == 0:
            if char.isalnum():
                state = 1
            else:
                return False
        elif state == 1:
            if char.isalnum() or char in ['.', '_', '+', '-']:
                continue
            elif char == '@':
                state = 2
            else:
                return False
        elif state == 2:
            if char.isalnum():
                state = 3
            else:
                return False
        elif state == 3:
            if char.isalnum() or char == '-':
                continue
            elif char == '.':
                state = 4
            else:
                return False
        elif state == 4:
            if char.isalpha():
                state = 5
            else:
                return False
        elif state == 5:
            if char.isalpha():
                continue
            else:
                return False
    return state == 5

def main():
    print("Email Validator Tool")
    while True:
        email = input("Enter an email to validate (or 'q' to quit): ")
        if email.lower() == 'q':
            break
        is_valid = validate_email_regex(email)  # or use validate_email_fa(email)
        print("Valid email!" if is_valid else "Invalid email.")

if __name__ == "__main__":
    main()

def test_dataset(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            email, label = line.strip().split(',')
            result = validate_email_regex(email)
            print(f"{email}: {'Correct' if result == (label == 'valid') else 'Incorrect'}")

print(test_dataset('/Users/sweta_personal1/Desktop/toc/sample_email.txt'))