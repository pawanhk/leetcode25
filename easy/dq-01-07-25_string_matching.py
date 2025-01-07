# my solution -- runs in O(n^2)

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if(words[i] in words[j] and i != j):
                    if(words[i] not in res):
                        res.append(words[i])
        
        return res


                
