# couldnt find a solution - - wrong idea

# best solution
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # answer array
        answer = [0] * len(boxes)
        # total
        n = len(boxes)

        # moves to the left and right
        ml = 0
        mr = 0

        # balls remaining
        bl = 0
        br = 0

        for i in range(n):
            answer[i] += ml
            bl += int(boxes[i])
            ml += bl
            j = n - 1 - i
            answer[j] += mr
            br += int(boxes[j])
            mr += br
            print("index j: " + str(answer[j]))
        
        return answer

        
           
        