class Solution {
    public int calPoints(String[] operations) {
        ArrayList<Integer> nums = new ArrayList<>();
        int sum = 0;
        for (int i = 0; i < operations.length; i++) {
            String op = operations[i];

            if (op.equals("+")) {
                int last = nums.get(nums.size() - 1);
                int secondLast = nums.get(nums.size() - 2);
                nums.add(last + secondLast);
                sum += nums.get(nums.size() - 1);
            } else if (op.equals("D")) {
                nums.add(nums.get(nums.size() - 1) * 2);
                sum += nums.get(nums.size() - 1);
            } else if (op.equals("C")) {
                sum -= nums.get(nums.size() - 1);
                nums.remove(nums.size() - 1);
            } else {
                nums.add(Integer.parseInt(op));
                sum += nums.get(nums.size() - 1);
            }
        }

        return sum;
    }
}