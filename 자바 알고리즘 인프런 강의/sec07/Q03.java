package com.algorithm.sec07;

import java.util.Scanner;

public class Q03 {
    public int DFS(int n){
        if(n==1) return 1;
        else{
            return n*DFS(n-1);
        }
    }
    public void solution(int n){
        System.out.println(DFS(n));
    }

    public static void main(String[] args) {
        Q03 T = new Q03();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        T.solution(n);
    }
}
