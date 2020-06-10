class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, v in enumerate(nums):
            if (v_comp := target - v) not in my_dict:
                # cannot find the complement, store the current value with index
                my_dict[v] = i
            else:
                # found the complement, retrive the index
                return [my_dict[v_comp], i]