package com.algorithm.sec07;

import java.util.Scanner;

public class Q01 {
    public void DFS(int n){
        if(n == 0) return;
        else{
            DFS(n-1);
            System.out.print(n + " ");
        }
    }

    public void solution(int n){
        DFS(n);
    }
    public static void main(String[] args) {
        Q01 T = new Q01();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        T.solution(n);
    }
}
