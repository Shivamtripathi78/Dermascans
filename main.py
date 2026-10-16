import getpass
import string


def check_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Check character variety
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Include special characters.")

    # Assign strength rating
    if len(password) < 8:
        strength = "Very Weak"
    elif score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, suggestions


def main():
    print("=" * 40)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = getpass.getpass("Enter a password to check: ")

    if not password:
        print("Password cannot be empty.")
        return

    score, strength, suggestions = check_password(password)

    print("\n========== RESULTS ==========")
    print(f"Strength: {strength}")
    print(f"Score: {score}/6")

    if suggestions:
        print("\nSuggestions for improvement:")

        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("\nGreat! Your password meets all the checks.")

    print("\nNote: This is a basic educational checker.")


if __name__ == "__main__":
    main()