package com.algorithm.sec03;

import java.util.Scanner;

public class Q04 {
    public int solution(int n, int m, int[] arr){
        int answer= 0;
        int sum = 0;
        int left = 0, right = 0;
        for (int r = 0; r < n; r++) {
            sum += arr[r];
            if(sum == m){
                answer++;
            }
            while(sum>=m){
                sum -= arr[left++];
                if(sum==m){
                    answer++;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Q04 T = new Q04();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        System.out.println(T.solution(n, m, arr));
    }
}
