package com.algorithm.sec07;

import java.util.Scanner;

public class Q02 {
    public void DFS(int n){
        if(n == 0) return;
        else{
            DFS(n/2);
            System.out.print(n%2);
        }
    }
    public void solution(int n){
        DFS(n);
    }
    public static void main(String[] args) {
        Q02 T = new Q02();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        T.solution(n);
    }
}
