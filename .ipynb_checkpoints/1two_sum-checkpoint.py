# two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind, i in enumerate(nums[:-1]):
            rest_set = set(nums[ind+1:])
            if (target - i) in rest_set:
                ind2 = nums[ind+1:].index(target - i)
                break
        return [ind, ind2+ind+1]
