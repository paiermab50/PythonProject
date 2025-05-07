def emailValidation(email):
    try:
        if '@' in email and '.' in email:
            username = email.split("@")[0]
            domain = email.split("@")[1]

            if username.isalnum() and domain:
                parts = domain.split(".")
                domain1 = parts[0]
                domain2 = parts[1]

                if domain1 and domain2:
                    return f"{email} is a valid email"
        return f"{email} is not a valid email"

    except IndexError:
        return f"{email} is not a valid email (invalid domain structure)"
    except Exception as e:
        return f"An error occurred during validation: {e}"

# Input
Email = input("Enter your Email without any dots in username field: ").strip()
print(emailValidation(Email))
