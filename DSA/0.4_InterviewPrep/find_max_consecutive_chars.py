def find_max(s):
    # find max consecutive char
    max_val = 0
    max_char = ''

    left = 0

    length = len(s)

    char_count = 1

    while left < length - 1:

        if s[left] == s[left+1]:
            char_count += 1
        else:
            if char_count > max_val:
                max_val = char_count
                max_char = s[left]

            char_count = 1

        left += 1

    return max_char, max_val


print(find_max("aaaaaabbcfgaaa")) # 'a' , 6
