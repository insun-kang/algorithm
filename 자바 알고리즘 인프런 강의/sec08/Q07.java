package com.algorithm.sec08;

import java.util.Scanner;

public class Q07 {
    static int n, r;
    static int[][] dy = new int[35][35];
    public int DFS(int n, int r){
        if(dy[n][r]>0)return dy[n][r];
        if(n==r || r==0){
            return 1;
        }
        else{
            return dy[n][r] = DFS(n-1, r-1) + DFS(n-1,r);
        }
    }

    public static void main(String[] args) {
        Q07 T = new Q07();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        r = kb.nextInt();
        System.out.println(T.DFS(n, r));
    }
}
