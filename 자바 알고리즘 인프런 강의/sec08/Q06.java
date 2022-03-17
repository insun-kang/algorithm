package com.algorithm.sec08;

import java.util.Scanner;

public class Q06 {
    static int n, m;
    static int[] arr, answer, visit;
    public void DFS(int L){
        if(L==m){
            for (int x:answer) {
                System.out.print(x + " ");
            }
            System.out.println();
        }
        else{
            for (int i = 0; i < n; i++) {
                if(visit[i] == 0){
                    visit[i]=1;
                    answer[L] = arr[i];
                    DFS(L+1);
                    visit[i]=0;
                }
            }
        }
    }

    public static void main(String[] args) {
        Q06 T = new Q06();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        m = kb.nextInt();
        arr = new int[n];
        visit = new int[n];
        answer = new int[m];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        T.DFS(0);
    }
}
