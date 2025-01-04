# my horrible solution, does not work

# loop throug all the elements 
count = 0
'''
for i in range(len(s)-1):
    if(len(s) == 3):
        if(s[:-1 != s]):
            return 0
    # creat an fsc string, so first second third elm
    first = s[i] + s[i+1]
    print("first element: " + first)
    second = s[i+2:]
    if(not second):
        second = s 
    # check if there is only element in the string
    print("remaining string: " + second)
    # check if the third element is in the substring
    if(s[i] in second):
        count += 1
    print(count)
return count
'''

# better solution that works

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # create a set first 
        sset = set(s)
        count = 0 

        # loop through removed duplicates
        for i in sset:
            # first index
            p = s.index(i)
            # last index 
            q = s.rindex(i)

            # between set
            bset = set()
            # everything in between is a palindrom
            for k in range(p+1,q):
                bset.add(s[k])

            # final count is the legth of everything between
            count += len(bset)
        return count



            

        