package com.algorithm.sec08;

import java.util.Scanner;

public class Q04 {
    static int n, m;
    static int[] answer;
    public void DFS(int L){
        if(L==m){
            for(int x: answer) System.out.print(x+" ");
            System.out.println();
        }
        else{
            for (int i = 1; i <= n; i++) {
                answer[L] = i;
                DFS(L+1);
            }
        }
    }

    public static void main(String[] args) {
        Q04 T = new Q04();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        m = kb.nextInt();
        answer = new int[m];
        T.DFS(0);
    }
}
