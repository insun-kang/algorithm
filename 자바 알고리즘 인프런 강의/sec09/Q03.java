package com.algorithm.sec09;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Time implements Comparable<Time>{
    public int time;
    public char state;
    Time(int time, char state){
        this.time = time;
        this.state = state;
    }
    @Override
    public int compareTo(Time t){
        if(t.time==this.time) return this.state-t.state;
        else return this.time-t.time;
    }
}
public class Q03 {
    public int solution(int n, ArrayList<Time> arr){
        int answer = 0;
        int cnt = 0;
        for(Time t: arr){
            if(t.state == 's'){
                cnt++;
            }
            else{
                cnt--;
            }
            answer = Math.max(answer, cnt);
        }

        return answer;
    }

    public static void main(String[] args) {
        Q03 T = new Q03();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        ArrayList<Time> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int start = kb.nextInt();
            arr.add(new Time(start, 's'));

            int end = kb.nextInt();
            arr.add(new Time(end, 'e'));
        }
        Collections.sort(arr);
        System.out.println(T.solution(n, arr));
    }

}
