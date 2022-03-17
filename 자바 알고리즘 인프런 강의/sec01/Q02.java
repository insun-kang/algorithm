package com.algorithm.sec01;

import java.util.Scanner;

public class Q02 {
    public String solution(String str){
        String answer = "";
        for(char c: str.toCharArray()){
            if(Character.isUpperCase(c)){
                answer += Character.toLowerCase(c);
            }
            else{
                answer += Character.toUpperCase(c);
            }
        }
        return answer;
    }

    public static void main(String[] args){
        Q02 T = new Q02();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        System.out.print(T.solution(str));
    }
}
