class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ind = 0;
        l = len(nums)
        if target>nums[l-1]:
            return l;
        elif target==nums[l-1]:
            return l-1;
        else:
            for i in range(l-1):
                if nums[i]==target:
                    ind=i;
                elif target>nums[i] and target<nums[i+1]:
                    ind = i+1;
            return ind;