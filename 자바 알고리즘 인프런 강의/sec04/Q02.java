package com.algorithm.sec04;

import java.util.HashMap;
import java.util.Scanner;

public class Q02 {
    public String solution(String s1, String s2){
        String answer = "YES";
        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();

        for(char x: s1.toCharArray()){
            map1.put(x, map1.getOrDefault(x, 0)+1);
        }
        for(char x: s2.toCharArray()){
            map2.put(x, map2.getOrDefault(x, 0)+1);
        }

        for(char key:map1.keySet()){
            if(map1.get(key) != map2.get(key)){
                answer = "NO";
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Q02 T = new Q02();
        Scanner kb = new Scanner(System.in);
        String s1 = kb.next();
        String s2 = kb.next();
        System.out.println(T.solution(s1, s2));
    }
}
