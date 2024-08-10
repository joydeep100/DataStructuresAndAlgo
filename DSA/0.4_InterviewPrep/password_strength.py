def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"

    res = []

    for password in passwords:

        dict = {
            "has_length": False,
            "has_digit": False,
            "has_upper": False,
            "has_lower": False,
            "has_spl": False,
        }

        if len(password) >= 8:
            dict["has_length"] = True

        for char in password:
            if char.isdigit():
                dict["has_digit"] = True
            if char.isupper():
                dict["has_upper"] = True
            if char.islower():
                dict["has_lower"] = True
            if char in special_characters:
                dict["has_spl"] = True

        res.append(all(dict.values()))
        
    return res


passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)
