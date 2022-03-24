package com.algorithm.sec09;

import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Q07_prim {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();
        ArrayList<ArrayList<Edge>> graph = new ArrayList<ArrayList<Edge>>();
        int[] visit = new int[n+1];
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Edge>());
        }
        for (int i = 0; i < m; i++) {
            int a = kb.nextInt();
            int b = kb.nextInt();
            int c = kb.nextInt();

            graph.get(a).add(new Edge(b, c));
            graph.get(b).add(new Edge(a, c));
        }
        int answer = 0;
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        pq.offer(new Edge(1, 0));
        while (!pq.isEmpty()){
            Edge tmp = pq.poll();
            int nv = tmp.idx;
            int ncost = tmp.cost;
            if(visit[nv] == 0){
                visit[nv] = 1;
                answer += tmp.cost;
                for(Edge o: graph.get(nv)){
                    if(visit[o.idx] == 0){
                        pq.offer(new Edge(o.idx, o.cost));
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
