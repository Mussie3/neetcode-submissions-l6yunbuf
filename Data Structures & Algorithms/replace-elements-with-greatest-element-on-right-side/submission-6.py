class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # inital max = -1
        # inverse iteration
        # newMax = max(oldMax, arr[i])

        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        
        return arr