package com.algorithm.sec04;

import java.util.HashMap;
import java.util.Scanner;

public class Q04 {
    public int solution(String s1, String s2){
        int answer = 0;
        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();

        for(char x: s2.toCharArray()){
            map2.put(x, map2.getOrDefault(x, 0)+1);
        }
        for (int i = 0; i < s2.length()-1; i++) {
            map1.put(s1.charAt(i), map1.getOrDefault(s1.charAt(i), 0)+1);
        }
        for (int i = s2.length()-1; i < s1.length(); i++) {
            map1.put(s1.charAt(i), map1.getOrDefault(s1.charAt(i), 0)+1);
            if(check(map1, map2)){
//                System.out.println(answer);
                answer++;
            }
            map1.put(s1.charAt(i-s2.length()+1), map1.get(s1.charAt(i-s2.length()+1))-1);
            if(map1.get(s1.charAt(i-s2.length()+1))==0){
                map1.remove(s1.charAt(i-s2.length()+1));
            }
        }

        return answer;
    }
    public boolean check(HashMap<Character, Integer> map1, HashMap<Character, Integer> map2){
//        System.out.println("map1 : " + Arrays.toString(map1.keySet().toArray()));
//        System.out.println("map2 : " + Arrays.toString(map2.keySet().toArray()));


        if(map1.size()==map2.size()){
            for(char x: map1.keySet()){
                if(map1.get(x)!=map2.get(x)){
                    return false;
                }
            }
            return true;

        }
        return false;

    }

    public static void main(String[] args) {
        Q04 T = new Q04();
        Scanner kb = new Scanner(System.in);
        String s1 = kb.next();
        String s2 = kb.next();

        System.out.println(T.solution(s1, s2));
    }
}
