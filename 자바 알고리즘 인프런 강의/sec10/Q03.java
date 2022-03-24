package com.algorithm.sec10;

import java.util.Scanner;

public class Q03 {
    static int[] dp;
    public int solution(int n, int[] arr){
        int answer = 0;

        dp[0]=1;
        for (int i = 1; i < n; i++) {
            int max = 0;
            for (int j = i-1; j >=0 ; j--) {
                if(arr[i]>arr[j] && max<dp[j]){
                    max = dp[j];
                }
            }
            dp[i] = max+1;
            answer = Math.max(answer, dp[i]);
        }

        return answer;
    }

    public static void main(String[] args) {
        Q03 T = new Q03();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] arr = new int[n];
        dp = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        System.out.println(T.solution(n, arr));
    }

}
