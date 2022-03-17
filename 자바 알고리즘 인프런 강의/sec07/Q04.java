package com.algorithm.sec07;

import java.util.Scanner;

public class Q04 {
    public int DFS(int n){
        if(n==1) return 1;
        else if(n==2) return 1;
        else{
            return DFS(n-1)+DFS(n-2);
        }
    }
    public static void main(String[] args) {
        Q04 T = new Q04();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        for (int i = 1; i <= n; i++) {
            System.out.print(T.DFS(i) + " ");
        }
    }
}
