package com.algorithm.sec07;

import java.util.ArrayList;
import java.util.Scanner;

public class Q13 {
    static ArrayList<ArrayList<Integer>> graph;
    static int n, m, answer = 0;
    static int[] visit;
    public void DFS(int v){
        if (v==n){
            answer++;
        }
        else{
            for(int x:graph.get(v)){
                if(visit[x]==0){
                    visit[x] = 1;
                    DFS(x);
                    visit[x]=0;
                }
            }
        }

    }

    public static void main(String[] args) {
        Q13 T = new Q13();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        m = kb.nextInt();
        graph = new ArrayList<ArrayList<Integer>>();
        visit = new int[n+1];
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < m; i++) {
            int a = kb.nextInt();
            int b = kb.nextInt();
            graph.get(a).add(b);
        }
        visit[1] = 1;
        T.DFS(1);
        System.out.println(answer);
    }
}
