package com.algo.sec02;

import java.util.ArrayList;
import java.util.Scanner;

public class Q04 {
    public ArrayList<Integer> solution(int n){
        ArrayList<Integer> answer= new ArrayList<>();
        answer.add(1);
        answer.add(1);
        for (int i = 2; i < n; i++) {
            answer.add(answer.get(i-1)+answer.get(i-2));
        }
        return answer;
    }
    public static void main(String[] args) {
        Q04 T = new Q04();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        for (int i : T.solution(n)) {
            System.out.print(i + " ");
        }
    }
}
