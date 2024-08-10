def add_spaces(s):
    result = []
    for i, char in enumerate(s):
        if char.isupper() and i != 0:
            result.append(' ')
        result.append(char)
    return ''.join(result)


s = "IAmASoftwareTestEngineer"
output = add_spaces(s)
print(output)  # Output: I Am A Software Test Engineer
