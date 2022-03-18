package com.algorithm.sec08;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Point{
    public int y, x;
    Point(int y, int x){
        this.y = y;
        this.x = x;
    }
}

public class Q11 {
    static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0};
    static int[][] graph, dist;

    public void BFS(int y, int x){
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(y, x));
        graph[y][x] = 1;
        while (!q.isEmpty()){
            Point tmp = q.poll();
            for (int i = 0; i < 4; i++) {
                int ny = dy[i] + tmp.y;
                int nx = dx[i] + tmp.x;
                if(nx>=0 && nx<=6 && ny>=0 && ny<=6 && graph[ny][nx]==0){
                    graph[ny][nx] = 1;
                    q.offer(new Point(ny, nx));
                    dist[ny][nx] = dist[tmp.y][tmp.x]+1;
                }

            }

        }

    }

    public static void main(String[] args) {
        Q11 T = new Q11();
        Scanner kb = new Scanner(System.in);
        graph = new int[7][7];
        dist = new int[7][7];
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                graph[i][j] = kb.nextInt();
            }
        }
        T.BFS(0, 0);
        int answer = dist[6][6];
        if(answer == 0){
            System.out.println(-1);
        }
        else{
            System.out.println(answer);
        }

    }

}
