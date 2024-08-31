import re

def assess_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        score += min(len(password), 20)  # Max 20 points for length
    if re.search(r'[A-Z]', password):
        score += 10
    else:
        feedback.append("Add uppercase letters for a stronger password.")
    if re.search(r'[a-z]', password):
        score += 10
    else:
        feedback.append("Add lowercase letters for a stronger password.")
    if re.search(r'\d', password):
        score += 10
    else:
        feedback.append("Add numbers for a stronger password.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 10
    else:
        feedback.append("Add special characters for a stronger password.")
    if len(set(re.findall(r'\d|\W|[A-Z]|[a-z]', password))) > 3:
        score += 10
    if score < 30:
        strength = "Weak"
    elif score < 50:
        strength = "Moderate"
    elif score < 70:
        strength = "Strong"
    else:
        strength = "Very Strong"
    return score, strength, feedback

def main():
    print("This tool will assess the strength of your password.")
    print()
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Done!")
            break
        score, strength, feedback = assess_password_strength(password)
        print(f"\nPassword Strength: {strength}")
        print(f"Score: {score}/70")
        if feedback:
            print("\nSuggestions for improvement:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("\nFull Marks")

        print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()