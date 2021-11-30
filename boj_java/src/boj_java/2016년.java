class Solution {
    public String solution(int a, int b) {
        String answer = "";
        String[] date = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
        int[] day = {31,29,31,30,31,30,31,31,30,31,30,31};
        int cnt = 0;
        for(int i=0;i<a-1;i++){
            cnt+=day[i];
        }
        cnt += b-1;
        
        answer = date[(5+cnt%7)%7];
        return answer;
    }
}