# my solution :(

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    print(nums[i] + nums[j])
                    return([i,j])


# best optimized solution 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create the final dict 
        fin_dict = {}
        for index,number in enumerate(nums):
            # find the complement for each number
            complement = target - number
            # first check if the complement already exists 
            if(complement in fin_dict):
                return [fin_dict[complement],index]
            # if not add to the complement
            fin_dict[number] = index 


