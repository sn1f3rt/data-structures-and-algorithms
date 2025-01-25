from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in idx_map:
                return [i, idx_map.get(diff)]
            idx_map[nums[i]] = i


# NeetCode (requires returned indexes to be in ascending order)
# class Solution:
#     # noinspection PyPep8Naming,PyMethodMayBeStatic
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         idx_map = dict()
#
#         for i in range(len(nums)):
#             diff = target - nums[i]
#             if diff in idx_map:
#                 i2 = idx_map.get(diff)
#                 return [i, i2] if i < i2 else [i2, i]
#             idx_map[nums[i]] = i
