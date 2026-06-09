from collections import List

class Solution:
    def numIdenticalPairsBF(self, nums: List[int]) -> int:

        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

        return count

    def numIdenticalPairs(self, nums: List[int]) -> int:

        from collections import defaultdict

        helper_map = defaultdict(list)

        for num in nums:
            # this is the right way to append to defaultdict321qwsz
            helper_map[num].append(num)

        count = 0
        for v in helper_map.values():
            n = len(v)
            # formula
            count += (n*(n-1))//2

        return count