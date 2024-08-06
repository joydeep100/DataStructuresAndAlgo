s = "abcde"

def reverse(s):
    
    if len(s) == 1:
        return s
        
    return s[-1] + reverse(s[:-1])
    
print(reverse(s))

s2 = "aaaaaabbcfgaaa" # a, 6

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

print(find_max(s2))