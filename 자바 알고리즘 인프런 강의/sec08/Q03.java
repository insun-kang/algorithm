package com.algorithm.sec08;

import java.util.Scanner;

public class Q03 {
    static int n, m, answer;
    static int[] score, time;
    public void DFS(int L, int s_sum, int t_sum){
        if(t_sum>m){
            return;
        }
        if(L==n){
            answer = Math.max(answer, s_sum);
        }
        else{
            DFS(L+1, s_sum+score[L], t_sum+time[L]);
            DFS(L+1, s_sum, t_sum);
        }
    }
    public static void main(String[] args) {
        Q03 T = new Q03();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        m = kb.nextInt();
        score = new int[n];
        time = new int[n];

        for (int i = 0; i < n; i++) {
            score[i] = kb.nextInt();
            time[i] = kb.nextInt();
        }
        T.DFS(0, 0, 0);
        System.out.println(answer);
    }
}
