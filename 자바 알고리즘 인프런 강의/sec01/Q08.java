package com.algo.sec01;

import java.util.Scanner;

public class Q08 {
    public String solution(String str){
        String answer = "NO";
        str = str.toUpperCase().replaceAll("[^A-Z]", "");
        String rstr = new StringBuilder(str).reverse().toString();
        if(str.equals(rstr)){
            answer = "YES";
        }

        return answer;
    }

    public static void main(String[] args){
        Q08 T = new Q08();
        Scanner kb = new Scanner(System.in);
        String str = kb.nextLine();
        System.out.println(T.solution(str));
    }
}
