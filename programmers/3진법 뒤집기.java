import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int solution(int n) {
        int answer = 0;
        ArrayList<Integer> box = new ArrayList<>();
        int r = 0;
        int q = n;
        
        if(n<3){
            answer = n;
        }
        else{
            while (true){
                r = q%3;
                q = q/3;
                if(q<3){
                    box.add(r);
                    box.add(q);
                    break;
                }
                else{
                    box.add(r);
                }
            }
        }
        for(int i=0;i<box.size();i++){
            
            answer += box.get(i)*Math.pow(3, box.size()-i-1);

        }
        return answer;
    }
}