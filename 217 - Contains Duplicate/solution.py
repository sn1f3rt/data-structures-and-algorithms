from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
