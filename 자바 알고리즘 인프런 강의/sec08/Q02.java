package com.algorithm.sec08;

import java.util.Scanner;

public class Q02 {
    static int c, n, sum, answer;
    static int[] arr;
    public void DFS(int L, int sum){
        if(sum>c){
            return;
        }
        if(L==n){
            answer = Math.max(answer, sum);
        }
        else{
            DFS(L+1, sum+arr[L]);
            DFS(L+1, sum);
        }
    }

    public static void main(String[] args) {
        Q02 T = new Q02();
        Scanner kb = new Scanner(System.in);
        c = kb.nextInt();
        n = kb.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        T.DFS(0, 0);
        System.out.println(answer);
    }
}
