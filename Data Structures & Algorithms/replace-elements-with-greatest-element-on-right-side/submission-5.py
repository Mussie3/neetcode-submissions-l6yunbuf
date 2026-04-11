class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        i = 0
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return [-1]
        greatest_number = arr[1]
        index_of_greatest_number = 1
        while i < len(arr) - 1:
            for j in range(i + 1, len(arr)):
                if greatest_number < arr[j]:
                    greatest_number = arr[j]
                    index_of_greatest_number = j
                elif greatest_number == arr[j]:
                    greatest_number = arr[j]
                    index_of_greatest_number = j
            
            for k in range(i, index_of_greatest_number):
                arr[k] = greatest_number
            i = index_of_greatest_number
            greatest_number = 0
            index_of_greatest_number = 0

        arr[len(arr) - 1] = -1

        return arr