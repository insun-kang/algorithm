class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        boolean check = false;
        
        for(int i=0;i<10;i++){
            for(int j = 0; j<numbers.length; j++){
                if(i==numbers[j]){
                    check = true;
                    break;
                }
            }
            if(check){
                check = false;
                continue;
            }
            else{
                answer += i;
            }
            
        }
        
        return answer;
    }
}