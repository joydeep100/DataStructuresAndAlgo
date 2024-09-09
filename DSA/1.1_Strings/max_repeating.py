''' 1668. Maximum Repeating Substring
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. 
The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. 
If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.
'''
def maxRepeatingWR(sequence, word):

    left = 0
    len_of_seq = len(sequence)
    len_of_word = len(word)

    count = 0
    max_len = 0
    
    while left < len_of_seq - len_of_word:

        if sequence[left:left + len_of_word] == word:
            count += 1
            left += len_of_word
        else:
            left += 1
            count = 0
        if count > max_len:
            max_len = count

    return max_len

# print(maxRepeating('aaabaaaabaaabaaaabaaaabaaaabaaaaba', 'aaaba'))
# a a a b a a a a b a a  a  b  a  a  a  a  b  a  a  a  a  b  a  a  a  a  b  a  a  a  a  b  a
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33

''' This failed just two test case of the test cases because we need congruent (k-repeating) sequence
TC1 - a , a
TC2 - aaabaaaabaaabaaaabaaaabaaaabaaaaba, aaaba
aaaba 0 5
aaaba 5 10 <--
aaaba 14 19 <--
aaaba 19 24
aaaba 24 29
aaaba 29 34

see how from 10 to 14th index there is a gap
'''

def maxRepeating(sequence, word):

    count = 0
    k = 1
    while (word * k) in sequence:
        k += 1
        count += 1

    return count

print(maxRepeating('aaabaaaabaaabaaaabaaaabaaaabaaaaba', 'aaaba')) # 5 is correct o/p