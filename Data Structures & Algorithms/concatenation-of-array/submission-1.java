class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] newNums = new int[2 * nums.length];
        for(int i = 0; i < (2 * nums.length); i++){
            if (i >= nums.length){
                newNums[i] = nums[i - nums.length];
                continue;
            }
            newNums[i] = nums[i];
        }

        return newNums;
    }
}