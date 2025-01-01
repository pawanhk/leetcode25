#my solution 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fin_dict = dict.fromkeys(s)
        tin_dict = dict.fromkeys(t)
        if(len(s) != len(t)):
            return False
        # set everything to 0 first
        for i in range(0,len(s)):
            fin_dict[s[i]] = 0
            tin_dict[t[i]] = 0
        # count the occurances 
        for i in range(0,len(s)):
            fin_dict[s[i]] += 1
            tin_dict[t[i]] += 1

        return fin_dict == tin_dict

# best solution -- just sort first

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t