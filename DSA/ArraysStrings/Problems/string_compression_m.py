'''
* this problem is easy if we have create a separate array to store output
'''
from typing import List
import pdb

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        i = 0
        write_idx = 0 # pointer to store where to write
        while (i < n):

            curr_char = chars[i]
            count = 0
            while (i < n and chars[i] == curr_char):
                i += 1
                count += 1

            chars[write_idx] = curr_char
            write_idx += 1

            if count > 1:
                # we need to do this because say count of c is 12, then we should do ["c", "1", "2"]
                for ch in str(count):
                    chars[write_idx] = ch
                    write_idx += 1

        return write_idx


# Example usage
sol = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"] 
print(sol.compress(chars))  # Output: 6 and the chars arr after in place operations is ['a', '2', 'b', '2', 'c', '3', 'c']