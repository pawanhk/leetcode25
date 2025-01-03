class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        lsum = 0
        # get the sum of all the elements in the list first
        tsum = sum(nums)
        rsum = tsum
        # store the number of legal splits
        leg_split = 0
        for i in range(0,len(nums)-1):
            # add to the lsum at each split and check
            lsum += nums[i]
            if(lsum < 0):
                rsum = tsum + (-lsum)
            else:
                rsum = tsum - lsum
            if(lsum >= rsum):
                leg_split += 1
        return leg_split
            