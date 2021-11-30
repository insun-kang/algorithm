import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        int[] student= new int[n];
        
        // 잃어버린 사람
        for(int i: lost){
            student[i-1]--;
        }
        
        // 여분 가진 사람
        for(int i: reserve){
            student[i-1]++;
        }
        
        // 체육복 빌리기
        for(int i=0;i<n;i++){
            if(student[i]<0){
                if(i!=0 && student[i-1]==1){
                    student[i-1]--;
                    student[i]++;
                }
                else if(i!=n-1 && student[i+1]==1){
                    student[i+1]--;
                    student[i]++;
                }
            }
        }
        for(int i:student){
            if(i==-1){
                answer--;
            }
        }
        
        return answer;
    }
}