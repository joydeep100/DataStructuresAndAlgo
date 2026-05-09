def decode_string(input_str):
    output_str = ""
    i = 0
    while i < len(input_str):
        char = input_str[i]
        i += 1
        num_str = ""
        while i < len(input_str) and input_str[i].isdigit():
            # imp point, .isdigit() is a string method not a int method
            num_str += input_str[i]
            i += 1
        if num_str:
            output_str += char * int(num_str)
    return output_str

print(decode_string("a1b10")) # Output: abbbbbbbbbb

# when for a single count, the count value is omitted, ex ab2cd3
def decode_string_v2(str):

    i = 0
    res = ''
    while(i < len(str) - 1):
        char = str[i]
        # check if next char in digit or not, if digit same flow as above
        if (i < len(str) - 1 and str[i+1].isdigit()):
            i += 1
            num_str = ''
            while(i < len(str) and str[i].isdigit()):
                num_str += str[i]
                i += 1
            if num_str:
                res += char * int(num_str)
        # if not append and increment res
        else:
            res += char
            i += 1

    return res

print(decode_string_v2("abcd3"))  # Output: abcddd
