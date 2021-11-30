import java.util.ArrayList;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] one = {1,2,3,4,5};
        int[] two = {2,1,2,3,2,4,2,5};
        int[] three = {3,3,1,1,2,2,4,4,5,5};
        int ans1 = 0;
        int ans2 = 0;
        int ans3 = 0;
        
        for(int i=0;i<answers.length;i++){
            if(one[i%one.length] == answers[i]){
                ans1 ++;
            }
            if(two[i%two.length] == answers[i]){
                ans2 ++;
            }
            if(three[i%three.length] == answers[i]){
                ans3 ++;
            }
        }
        
        int max = Math.max(Math.max(ans1, ans2),ans3);
        ArrayList<Integer> temp = new ArrayList<Integer>();
        if(max==ans1){
            temp.add(1);
        }
        if(max==ans2){
            temp.add(2);
        }
        if(max==ans3){
            temp.add(3);
        }
        
        answer = new int[temp.size()];
        
        for(int i = 0;i<answer.length;i++){
            answer[i] = temp.get(i);
        }
        
        return answer;
    }
}