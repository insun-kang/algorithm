package com.algorithm.sec01;

import java.util.ArrayList;
import java.util.Scanner;

public class Q04 {
    public ArrayList<String> solution(int n, String[] words){
        ArrayList<String> answer = new ArrayList<>();
        for(String x : words){
            String tmp = new StringBuilder(x).reverse().toString();
            answer.add(tmp);
        }


        return answer;
    }

    public static void main(String[] args){
        Q04 T = new Q04();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        String[] words = new String[n];
        for(int i = 0;i<n;i++){
            words[i] = kb.next();
        }
        for(String x:T.solution(n, words)){
            System.out.println(x);
        }
    }
}
