package com.algorithm.sec05;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Q07 {
    public String solution(String s1, String s2){
        String answer = "YES";
        Queue<Character> q = new LinkedList<>();
        for(char x: s1.toCharArray()){
            q.offer(x);
        }
        for(char x: s2.toCharArray()){
            if(q.contains(x)){
                if(x!=q.poll()){
                    answer = "NO";
                }
            }

        }
        if(!q.isEmpty()){
            answer = "NO";
        }

        return answer;
    }

    public static void main(String[] args) {
        Q07 T = new Q07();
        Scanner kb = new Scanner(System.in);
        String s1 = kb.next();
        String s2 = kb.next();
        System.out.println(T.solution(s1, s2));

    }
}
