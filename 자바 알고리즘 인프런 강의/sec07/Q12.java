package com.algorithm.sec07;

import java.util.Scanner;

public class Q12 {
    static int n, m, answer = 0;
    static int[] visit;
    static int[][] graph;
    public void DFS(int v){
        if(v == n) answer++;
        else{
            for (int i = 1; i <= n; i++) {
                if(graph[v][i] ==1 && visit[i] == 0){
                    visit[i]=1;
                    DFS(i);
                    visit[i]=0;
                }
            }
        }
    }
    public static void main(String[] args) {
        Q12 T = new Q12();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        m = kb.nextInt();
        visit = new int[n+1];
        graph = new int[n+1][n+1];
        for (int i = 0; i < m; i++) {
            int a = kb.nextInt();
            int b = kb.nextInt();
            graph[a][b] =1;
        }
        visit[1] = 1;
        T.DFS(1);
        System.out.println(answer);
    }
}
