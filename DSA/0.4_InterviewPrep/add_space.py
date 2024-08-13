def add_spaces(s):
    result = []

    ''' Python concept, Try using string concat it is not time efficient. O(n2)
    In python we can use string builder by using a list (append each time) and then join it back
    '''
    for i, char in enumerate(s):
        if char.isupper() and i != 0:
            result.append(' ')
        result.append(char)
    return ''.join(result)


s = "IAmASoftwareTestEngineer"
output = add_spaces(s)
print(output)  # Output: I Am A Software Test Engineer
