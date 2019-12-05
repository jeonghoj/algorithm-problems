class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index,first_val in enumerate(nums):
            for second_index,second_val in enumerate(nums[first_index+1:]):
                if first_val+second_val == target :
                    return [first_index, first_index+1+second_index]

