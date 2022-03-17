package com.algorithm.sec08;

import java.util.Scanner;

public class Q08 {
    static boolean flag = false;
    static int n, f;
    static int[] visit, b, p;
    static int[][] dy = new int[35][35];
    public int combi(int n, int r){
        if(dy[n][r]>0) return dy[n][r];
        if(n==r || r==0){
            return 1;
        }
        else{
            return dy[n][r] = combi(n-1, r-1) + combi(n-1, r);
        }
    }
    public void DFS(int L, int sum){
        if(flag) return;
        if(L==n){
            if(sum==f){
                for(int x: p) System.out.print(x + " ");
                flag = true;
            }
        }
        else{
            for (int i = 1; i <= n; i++) {
                if(visit[i] == 0){
                    visit[i] = 1;
                    p[L] = i;
                    DFS(L+1, sum+(p[L]*b[L]));
                    visit[i] = 0;
                }

            }
        }
    }

    public static void main(String[] args) {
        Q08 T = new Q08();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        f = kb.nextInt();
        p = new int[n];
        b = new int[n];
        visit = new int[n+1];
        for (int i = 0; i < n; i++) {
            b[i] = T.combi(n-1, i);
        }
        T.DFS(0, 0);
    }
}
