package com.algorithm.sec07;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Q14 {
    static int n, m, answer = 0;
    static ArrayList<ArrayList<Integer>> graph;
    static int[] visit, cnt;
    public void BFS(int v){
        visit[v] =1;
        cnt[v] = 0;
        Queue<Integer> q = new LinkedList<>();
        q.offer(v);
        while (!q.isEmpty()) {
            int x = q.poll();
            for(int nx:graph.get(x)){
                if(visit[nx]==0){
                    visit[nx] = 1;
                    q.offer(nx);
                    cnt[nx] = cnt[x]+1;
                }
            }
        }
    }

    public static void main(String[] args) {
        Q14 T = new Q14();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        m = kb.nextInt();
        visit = new int[n+1];
        cnt = new int[n+1];
        graph = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < m; i++) {
            int a = kb.nextInt();
            int b = kb.nextInt();
            graph.get(a).add(b);
        }
        T.BFS(1);
        for (int i = 2; i <=n ; i++) {
            System.out.println(i+" : " + cnt[i]);
        }
    }
}
