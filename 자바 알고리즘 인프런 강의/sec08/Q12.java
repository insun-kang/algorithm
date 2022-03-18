package com.algorithm.sec08;


import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Point_two{
    public int x, y, cnt;
    Point_two(int x, int y, int cnt){
        this.x = x;
        this.y = y;
        this.cnt = cnt;
    }
}
public class Q12 {
    static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0};
    static int n, m, cnt;
    static int[][] graph;
    static Queue<Point_two> q= new LinkedList<>();
    static boolean flag = false;
    public void BFS(){
        while(!q.isEmpty()){
            Point_two tmp = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + tmp.x;
                int ny = dy[i] + tmp.y;

                if(nx>=0 && nx<n && ny>=0 && ny<m && graph[nx][ny] == 0){
                    graph[nx][ny] = 1;
                    cnt = tmp.cnt+1;
                    q.offer(new Point_two(nx, ny, tmp.cnt+1));
                }
            }
        }
    }
    public static void main(String[] args) {
        Q12 T = new Q12();
        Scanner kb = new Scanner(System.in);
        m = kb.nextInt();
        n = kb.nextInt();
        graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                graph[i][j] = kb.nextInt();
                if(graph[i][j]==1) q.offer(new Point_two(i, j, 0));
            }
        }
        T.BFS();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(graph[i][j]==0){
                    flag = true;
                }
            }
        }
        if(flag){
            System.out.println(-1);
        }
        else {
            System.out.println(cnt);
        }

    }

}
