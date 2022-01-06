def email_slicer(email):
    name = email[:email.index("@")] # gets characters before "@"
    domain = email[email.index("@")+1:] # gets characters after "@"

    print(f"Your name is {name}, and domain is {domain}")

if __name__ == "__main__":
    email = input("Email Address :> ").strip()
    email_slicer(email)
