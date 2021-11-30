import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int max = nums.length/2;
        HashSet<Integer> numSet = new HashSet<>();
        
        for(int num: nums){
            numSet.add(num);
        }
        
        if(max<numSet.size()){
            return max;
        }
        else{
            return numSet.size();
        }
            
    }
}