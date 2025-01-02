# I dont have a solution for this, learned about prefix sums today 

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a','e','i','o','u'}
        ans = [0] * len(queries)
        prefix_sum = [0] * len(words)

        # create the prefix array first 
        sum = 0 
        for i in range(len(words)):
            curr = words[i]
            if(curr[0] in vowels and curr[len(curr) - 1] in vowels):
                sum += 1
            prefix_sum[i] = sum 

        # loop through queries 
        for i in range(len(queries)):
            currq = queries[i]
            ans[i] = prefix_sum[currq[1]] - (0 if currq[0] == 0 else prefix_sum[currq[0] -1])
        
        return ans

        
        
