package com.algo.sec02;

import java.util.Scanner;

public class Q07 {
    public int solution(int n, int[] arr){
        int answer = 0;
        int[] score = new int[n];
        int point = 0;
        for (int i = 0; i < n; i++) {
            if(arr[i]==0){
                point = 0;
            }
            else{
                point++;
                answer += point;
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        Q07 T = new Q07();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        System.out.println(T.solution(n, arr));

    }
}
