package com.algo.sec01;

import java.util.Calendar;
import java.util.Scanner;

public class Q09 {
    public int solution(String str){
        int answer = 0;
        String tmp = "";
        for(char c :str.toCharArray()){
            if(Character.isDigit(c)){
                tmp += c;
            }
        }
        answer = Integer.parseInt(tmp);

        return answer;
    }

    public  static void main(String[] args){
        Q09 T = new Q09();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        System.out.println(T.solution(str));

    }
}
