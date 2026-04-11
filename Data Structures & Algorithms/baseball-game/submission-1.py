class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        for i in range(0, len(operations)):
            print(i)
            print(operations[i])
            if operations[i] == "+":
                print(nums)
                nums.append(nums[len(nums) - 1] + nums[len(nums) - 2])
                print(nums)
            elif operations[i] == "C":
                print(nums)
                nums.pop()
                print(nums)
            elif operations[i] == "D" and i >= 1:
                print(nums)
                nums.append(nums[len(nums) - 1] * 2)
                print(nums)
            else:
                print(nums)
                nums.append(int(operations[i]))
                print(nums)

        print(nums)

        sum = 0
        for num in nums:
            sum += num
        
        return sum