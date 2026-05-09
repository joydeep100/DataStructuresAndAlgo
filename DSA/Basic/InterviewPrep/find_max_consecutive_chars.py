def find_max(s):
    # find max consecutive char
    max_val, max_char = 0, ''

    i, length = 0, len(s)

    while i < length - 1:
        
        char_count = 1
        
        while i < length - 1 and  s[i] == s[i+1]:
            char_count += 1
            i += 1
            
        if char_count > max_val:
            max_val = char_count
            max_char = s[i]
        
        i += 1
        
    return max_char, max_val

def find_max_better(s):
    max = 1
    char_count = 1
    max_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            char_count += 1
        else:
            char_count = 1

        if char_count > max:
            max = char_count
            max_char = s[i]

    return max_char, max


print(find_max("aaaaaabbcfgaaabbbbbbbbbb")) # 'b' , 10
print(find_max_better("aaaaaabbcfgaaabbbbbbbbbb")) # 'b' , 10
