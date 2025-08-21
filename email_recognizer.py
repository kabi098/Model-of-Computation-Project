import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$")

def validate_email_regex(email):
   
    return EMAIL_REGEX.fullmatch(email) is not None

def validate_email_fa(email):
   
    state = 0
    for char in email:
        if state == 0:  # Initial state - expecting start of local part
            if char.isalnum():
                state = 1
            else:
                return False
        elif state == 1:  # In local part
            if char.isalnum() or char in ['.']:
                continue
            elif char == '@':
                state = 2
            else:
                return False
        elif state == 2:  # After @ - expecting start of domain
            if char.isalnum():
                state = 3
            else:
                return False
        elif state == 3:  # In domain name
            if char.isalnum() :
                continue
            elif char == '.':
                state = 4
            else:
                return False
        elif state == 4:  # After dot - expecting TLD
            if char.isalpha():
                state = 5
            else:
                return False
        elif state == 5:  # In TLD
            if char.isalpha():
                continue
            else:
                return False
    
    return state == 5  # Must end in a valid state (TLD)

def test_dataset(file_path):
    """
    Tests both validation methods against a dataset file.
    
    Args:
        file_path (str): Path to the test dataset file.
    """
    print("Testing Email Validation Methods")
    print("=" * 50)
    
    try:
        with open(file_path, 'r') as f:
            total_tests = 0
            regex_correct = 0
            fa_correct = 0
            
            print(f"{'Email':<35} {'Expected':<10} {'Regex':<10} {'FA':<10} {'Regex OK':<10} {'FA OK'}")
            print("-" * 90)
            
            for line in f:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                    
                try:
                    email, label = line.split(',')
                    expected = (label == 'valid')
                    
                    regex_result = validate_email_regex(email)
                    fa_result = validate_email_fa(email)
                    
                    regex_match = regex_result == expected
                    fa_match = fa_result == expected
                    
                    if regex_match:
                        regex_correct += 1
                    if fa_match:
                        fa_correct += 1
                    
                    total_tests += 1
                    
                    print(f"{email:<35} {label:<10} {str(regex_result):<10} {str(fa_result):<10} {str(regex_match):<10} {str(fa_match)}")
                    
                except ValueError:
                    print(f"Skipping malformed line: {line}")
            
            print("\n" + "=" * 50)
            print("SUMMARY:")
            print(f"Total tests: {total_tests}")
            print(f"Regex method accuracy: {regex_correct}/{total_tests} ({regex_correct/total_tests*100:.1f}%)")
            print(f"Finite Automaton accuracy: {fa_correct}/{total_tests} ({fa_correct/total_tests*100:.1f}%)")
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        print("Please make sure the sample_email.txt file exists in the correct location.")
    except Exception as e:
        print(f"Error reading file: {e}")

def interactive_test():
    """
    Interactive mode for testing individual emails.
    """
    print("\n" + "=" * 50)
    print("Interactive Email Validator")
    print("=" * 50)
    
    while True:
        email = input("\nEnter an email to validate (or 'q' to quit): ")
        if email.lower() == 'q':
            break
        
        regex_result = validate_email_regex(email)
        fa_result = validate_email_fa(email)
        
        print(f"\nEmail: {email}")
        print(f"Regex validation: {'Valid' if regex_result else 'Invalid'}")
        print(f"Finite Automaton validation: {'Valid' if fa_result else 'Invalid'}")
        
        if regex_result != fa_result:
            print("⚠️  Warning: Methods disagree!")

def main():
    """
    Main function with menu options.
    """
    print("Email Validator Tool")
    print("=" * 30)
    print("1. Test with dataset file")
    print("2. Interactive validation")
    print("3. Exit")
    
    while True:
        choice = input("\nSelect an option (1-3): ")
        
        if choice == '1':
            file_path = input("Enter path to test file (or press Enter for default 'sample_email.txt'): ")
            if not file_path:
                file_path = 'sample_email.txt'
            test_dataset(file_path)
        elif choice == '2':
            interactive_test()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()