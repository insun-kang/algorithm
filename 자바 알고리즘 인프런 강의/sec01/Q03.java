package com.algorithm.sec01;


import java.util.Scanner;

public class Q03 {
    public String solution(String str){
        String answer = "";
        int max = Integer.MIN_VALUE;
        String[] words = str.split(" ");

        for(String word: words){
            int len = word.length();
            if(len>max){
                answer = word;
                max = len;
            }
        }

        return answer;
    }

    public static void main(String[] args){
        Q03 T = new Q03();
        Scanner kb = new Scanner(System.in);
        String str = kb.nextLine();
        System.out.print(T.solution(str));
    }
}
