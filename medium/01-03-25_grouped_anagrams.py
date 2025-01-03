# gave up on my solution which involved converting to ascii
# does not work well for all cases 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a defailt dict that takes a list
        groups = defaultdict(list)
        # check each element in the strs list
        for i in strs:
            key = ''.join(sorted(i))
            groups[key].append(i)
        # return the values only 
        return list(groups.values())

        
        
            
