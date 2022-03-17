package com.algorithm.sec08;

import java.util.Scanner;

public class Q01 {
    static String answer = "NO";
    static int n, total;
    static int[] arr;
    public void DFS(int L, int sum){
        if(total-sum == sum){
            answer = "YES";
        }
        if(L==n){
            return;
        }
        else{
            DFS(L+1, sum+arr[L]);
            DFS(L+1, sum-arr[L]);
        }
    }

    public static void main(String[] args) {
        Q01 T = new Q01();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
            total += arr[i];
        }
        T.DFS(0,0);
        System.out.println(answer);
    }
}
