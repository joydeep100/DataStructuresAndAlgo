''' 1668. Maximum Repeating Substring
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. 
The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. 
If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.
'''
def maxRepeating(sequence, word):
    # My solution
    left = 0
    res = 0
    ls = len(sequence)
    lw = len(word)
    while left + lw <= ls:

        if sequence[left : left + lw] == word:
            res += 1
            left += lw
        else:
            left += 1

    return res

print(maxRepeating('aaabaaaabaaabaaaabaaaabaaaabaaaaba', 'aaaba'))
# a a a b a a a a b a a  a  b  a  a  a  a  b  a  a  a  a  b  a  a  a  a  b  a  a  a  a  b  a
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33

''' This failed one of the test cases because we need congruent (k-repeating) sequence
aaaba 0 5
aaaba 5 10 <--
aaaba 14 19 <--
aaaba 19 24
aaaba 24 29
aaaba 29 34

see how from 10 to 14th index there is a gap
'''

def maxRepeatingCorrect(sequence, word):

    res = 0
    k = 1
    while word * k in sequence:
        res = k
        k += 1

    return res

print(maxRepeatingCorrect('ababc', 'ab'))
print(maxRepeatingCorrect('aaabaaaabaaabaaaabaaaabaaaabaaaaba', 'aaaba')) # 5 is correct o/p