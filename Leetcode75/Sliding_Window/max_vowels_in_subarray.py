''' 1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
 
Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
'''
def maxVowels(s, k):

    vowels = set("aeiou") # did a set to improve efficiency

    # get the initial window vowel count
    vowel_count = 0
    for ch in s[:k]:
        if ch in vowels:
            vowel_count += 1

    left = 0
    right = k - 1
    max_vowel_count = vowel_count

    while right < len(s) - 1:  # This -1 is important

        if s[left] in vowels:
            vowel_count -= 1

        left += 1
        right += 1

        if s[right] in vowels:
            vowel_count += 1

        if vowel_count > max_vowel_count:
            max_vowel_count = vowel_count

    return max_vowel_count

print(maxVowels("abciiidef", 3))