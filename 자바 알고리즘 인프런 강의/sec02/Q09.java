package com.algo.sec02;

import java.util.Scanner;

public class Q09 {
    public int solution(int n, int[][] arr){
        int answer = 0;
        int sum3 = 0;
        int sum4 = 0;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            int sum1 = 0;
            int sum2 = 0;
            sum3 += arr[i][i];
            sum4 += arr[i][n-1-i];
            
            for (int j = 0; j < n; j++) {
                sum1 += arr[i][j];
                sum2 += arr[j][i];
            }
            answer = Integer.max(answer, Integer.max(Integer.max(sum1, sum2), Integer.max(sum3, sum4)));
        }
        
        return answer;
    }
    public static void main(String[] args) {
        Q09 T = new Q09();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = kb.nextInt();
            }
        }
        System.out.println(T.solution(n, arr));
    }
}
