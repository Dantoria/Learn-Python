username = input("enter username: ")
password = input("enter password: ")

password_length = len(password)
hidden_password = "*" * password_length

print(f"hey, {username}, your password is {hidden_password} is {password_length} alphabets long")