package com.algo.sec03;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Q01 {
    public ArrayList<Integer> solution(int n, int[] arr1, int m, int[] arr2){
        ArrayList<Integer> answer = new ArrayList<>();
        for(int x: arr1){
            answer.add(x);
        }
        for(int x: arr2){
            answer.add(x);
        }

        answer.sort(Comparator.naturalOrder());
        return answer;
    }
    public static void main(String[] args) {
        Q01 T = new Q01();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] arr1 = new int[n];
        for (int i = 0; i < n; i++) {
            arr1[i] = kb.nextInt();
        }
        int m = kb.nextInt();
        int[] arr2 = new int[m];

        for (int i = 0; i < m; i++) {
            arr2[i] = kb.nextInt();
        }

        for(int x: T.solution(n, arr1, m, arr2)){
            System.out.print(x + " ");
        }

    }
}
