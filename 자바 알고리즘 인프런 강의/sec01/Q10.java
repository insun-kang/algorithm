package com.algo.sec01;

import java.util.ArrayList;
import java.util.Scanner;

public class Q10 {
    public int[] solution(String s, char t){
        int[] answer = new int[s.length()];
        int dist = 1000;

        for(int i = 0;i<s.length();i++){
            if(s.charAt(i)==t){
                dist = 0;
                answer[i] = 0;
            }
            else{
                dist++;
                answer[i] = dist;
            }
        }
        dist = 1000;
        for(int i = s.length()-1;i>=0;i--){
            if(s.charAt(i)==t){
                dist = 0;
                answer[i] = 0;
            }
            else{
                dist++;
                if(dist<answer[i]){
                    answer[i] = dist;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args){
        Q10 T = new Q10();
        Scanner kb = new Scanner(System.in);
        String s = kb.next();
        char t = kb.next().charAt(0);

        for(int c:T.solution(s,t)){
            System.out.print(c + " ");
        }



    }
}
