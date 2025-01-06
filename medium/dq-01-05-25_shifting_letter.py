# my solution -- ran out of time 

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        fletters = "abcdefghijklmnopqrstuvwxyz"
        bletters = "zyxwvutsrqponmlkjihgfedcba"
        # create the forward dictionary first 
        fdict = {}
        bdict = {}
        for i in range(0,len(fletters)):
            fdict[fletters[i]] = i
            bdict[bletters[i]] = -i-1

        # now go through S and perform the shifts
        for i in range(0,len(shifts)):
            # set the parameters
            start = shifts[i][0]
            end = shifts[i][1]
            direct = shifts[i][2]
            # temp string
            temp = ""
            for j in s:
                


# leet code solution 
class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff_array = [
            0
        ] * n  # Initialize a difference array with all elements set to 0

        # Process each shift operation
        for shift in shifts:
            if shift[2] == 1:  # If direction is forward (1)
                diff_array[shift[0]] += 1  # Increment at the start index
                if shift[1] + 1 < n:
                    diff_array[
                        shift[1] + 1
                    ] -= 1  # Decrement at the end+1 index
            else:  # If direction is backward (0)
                diff_array[shift[0]] -= 1  # Decrement at the start index
                if shift[1] + 1 < n:
                    diff_array[
                        shift[1] + 1
                    ] += 1  # Increment at the end+1 index

        result = list(s)
        number_of_shifts = 0

        # Apply the shifts to the string
        for i in range(n):
            number_of_shifts = (
                number_of_shifts + diff_array[i]
            ) % 26  # Update cumulative shifts, keeping within the alphabet range
            if number_of_shifts < 0:
                number_of_shifts += 26  # Ensure non-negative shifts

            # Calculate the new character by shifting `s[i]`
            shifted_char = chr(
                (ord(s[i]) - ord("a") + number_of_shifts) % 26 + ord("a")
            )
            result[i] = shifted_char

        return "".join(result)

# even better solution, this is the one I am gonna use 

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_diff = [0] * (len(s) + 1)

        for left, right, d in shifts:
            prefix_diff[right + 1] += 1 if d else -1
            prefix_diff[left] += -1 if d else 1

        diff = 0
        res = [ord(c) - ord("a") for c in s]

        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]
            res[i - 1]  = (diff + res[i-1]) % 26

        s = [chr(ord("a") + n) for n in res]

        return "".join(s)
