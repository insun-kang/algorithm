package com.algo.sec01;

import java.util.Locale;
import java.util.Scanner;

public class Q07 {
    public String solution(String str){
        String answer = "YES";
        str = str.toLowerCase();

        for(int i = 0;i<str.length()/2;i++){
            if(str.charAt(i) != str.charAt(str.length()-i-1)){
                answer = "NO";
            }
        }

        return answer;
    }

    public static void main(String[] args){
        Q07 T = new Q07();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        System.out.println(T.solution(str));
    }
}
