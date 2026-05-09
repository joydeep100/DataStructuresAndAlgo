def nxt_num(n):
    # sum of n + all its digits
    return n + sum(int(digit) for digit in str(n))

def meets(s1, s2):
    count, max_iterations = 0, 1000
    while (count < max_iterations):
        if (s1 == s2):
            return True
        elif s1 < s2:
            s1 = nxt_num(s1)
        else:
            s2 = nxt_num(s2)
        count += 1
    return False

# print(meets(620, 260))
# print(meets(31, 13))
print(meets(1711, 1117))