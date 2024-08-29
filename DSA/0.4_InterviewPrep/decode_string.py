def process_string(input_str):
    output_str = ""
    i = 0
    while i < len(input_str):
        char = input_str[i]
        i += 1
        num_str = ""
        while i < len(input_str) and input_str[i].isdigit():
            num_str += input_str[i]
            i += 1
        if num_str:
            output_str += char * int(num_str)
    return output_str

output = process_string("a1b10")
print(output)  # Output: abbbbbbbbbb

# when for a single count, the count value is omitted
def process_string_v2(input_str):
    output_str = ""
    i = 0
    while i < len(input_str):
        char = input_str[i]
        if i + 1 < len(input_str) and input_str[i + 1].isdigit():
            num_str = ""
            i += 1
            while i < len(input_str) and input_str[i].isdigit():
                num_str += input_str[i]
                i += 1
            output_str += char * int(num_str)
        else:
            output_str += char
            i += 1
    return output_str

output = process_string_v2("ab10c")
print(output)  # Output: abbbbbbbbbbc
