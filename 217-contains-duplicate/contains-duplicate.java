class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        boolean target = false;
        int count = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                count++;
            }
        }
        if(count >= 1){
            target = true;
            return target;
        }else{
            return target;
        }   
    } 
}