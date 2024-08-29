def find_max(s):
    # find max consecutive char
    max_val = 0
    max_char = ''

    i = 0

    length = len(s)

    char_count = 1

    while i < length - 1:

        if s[i] == s[i+1]:
            char_count += 1
        else:
            if char_count > max_val:
                max_val = char_count
                max_char = s[i]

            char_count = 1

        i += 1

    return max_char, max_val


print(find_max("aaaaaabbcfgaaa")) # 'a' , 6
