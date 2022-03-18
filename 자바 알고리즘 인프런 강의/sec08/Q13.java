package com.algorithm.sec08;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Point_three{
    public int y, x;
    public Point_three(int y, int x){
        this.y = y;
        this.x = x;
    }
}
public class Q13 {
    static int n, cnt;
    static int[][] graph;
    static int[] dx = {0,0,1,-1,1,-1,1,-1};
    static int[] dy = {1,-1,0,0,1,-1,-1,1};

    public void BFS(int y, int x){
        Queue<Point_three> q = new LinkedList<>();
        q.offer(new Point_three(y, x));
        while (!q.isEmpty()){
            Point_three tmp = q.poll();
            for (int i = 0; i < 8; i++) {
                int ny = dy[i] + tmp.y;
                int nx = dx[i] + tmp.x;

                if(nx>=0 && nx<n && ny>=0 && ny<n && graph[ny][nx] == 1){
                    graph[ny][nx] = 0;
                    q.offer(new Point_three(ny, nx));
                }
            }
        }
    }

    public static void main(String[] args) {
        Q13 T = new Q13();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        graph = new int[n][n];
        for (int y = 0; y < n; y++) {
            for (int x = 0; x <n ; x++) {
                graph[y][x] = kb.nextInt();
            }
        }
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                if(graph[y][x] == 1){
                    cnt++;
                    T.BFS(y, x);
                }
            }
        }
        System.out.println(cnt);
    }
}
