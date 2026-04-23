
email = input("Enter official email: ")

if "@" in email and "." in email:
    username = email.split("@")[0]
    domain = email.split("@")[1]

    print("Valid Email")
    print("Username:", username)
    print("Domain:", domain)

else:
    print("Invalid Email")
