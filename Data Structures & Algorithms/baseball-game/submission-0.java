class Solution {
    public int calPoints(String[] operations) {
        ArrayList<Integer> nums = new ArrayList<>();
        
        for (int i = 0; i < operations.length; i++) {
            String op = operations[i];

            if (op.equals("+")) {
                // Sum of the last two valid scores
                int last = nums.get(nums.size() - 1);
                int secondLast = nums.get(nums.size() - 2);
                nums.add(last + secondLast);
            } else if (op.equals("D")) {
                // Double the last valid score
                nums.add(nums.get(nums.size() - 1) * 2);
            } else if (op.equals("C")) {
                // Remove the last valid score
                nums.remove(nums.size() - 1);
            } else {
                // If it's not a command, it's a number
                nums.add(Integer.parseInt(op));
            }
        }

        int sum = 0;
        for (int n : nums) {
            sum += n;
        }

        return sum;
    }
}