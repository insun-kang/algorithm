package com.algorithm.sec09;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

class Edge implements Comparable<Edge>{
    public int idx;
    public int cost;

    Edge(int idx, int cost){
        this.idx = idx;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge o){
        return this.cost - o.cost;
    }
}
public class Q05 {
    static int n, m;
    static ArrayList<ArrayList<Edge>> graph;
    static int[] dist;
    public void dijkstra(int v){
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        pq.offer(new Edge(v, 0));
        dist[v] = 0;

        while (!pq.isEmpty()){
            Edge tmp = pq.poll();
            int now = tmp.idx;
            int nowcost = tmp.cost;
            if(dist[now]<nowcost) continue;
            for(Edge o:graph.get(now)){
                if(dist[o.idx]>nowcost + o.cost){
                    dist[o.idx] = nowcost + o.cost;
                    pq.offer(new Edge(o.idx, nowcost + o.cost));
                }
            }
        }
    }

    public static void main(String[] args) {
        Q05 T = new Q05();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        m = kb.nextInt();
        graph = new ArrayList<ArrayList<Edge>>();
        dist = new int[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Edge>());
        }
        for (int i = 0; i < m; i++) {
            int a = kb.nextInt();
            int b = kb.nextInt();
            int c = kb.nextInt();

            graph.get(a).add(new Edge(b, c));
        }
        T.dijkstra(1);

        for (int i = 2; i <= n; i++) {
            if(dist[i] == Integer.MAX_VALUE){
                System.out.println(i + " : impossible");
            }
            else{
                System.out.println(i + " : " + dist[i]);
            }
        }

    }
}
