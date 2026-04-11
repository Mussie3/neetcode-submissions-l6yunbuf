class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        sum = 0
        for i in range(0, len(operations)):
            if operations[i] == "+":
                nums.append(nums[len(nums) - 1] + nums[len(nums) - 2])
                sum += nums[len(nums) - 1]
            elif operations[i] == "C":
                sum -= nums[len(nums) - 1]
                nums.pop()
            elif operations[i] == "D":
                nums.append(nums[len(nums) - 1] * 2)
                sum += nums[len(nums) - 1]
            else:
                nums.append(int(operations[i]))
                sum += nums[len(nums) - 1]

        return sum