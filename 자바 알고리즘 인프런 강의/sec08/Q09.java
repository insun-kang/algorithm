package com.algorithm.sec08;

import java.util.Scanner;

public class Q09 {
    static int[][] graph;
    static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0};
    static int answer=0;

    public void DFS(int y, int x){
        if(x==6 && y==6){
            answer++;
        }
        else{
            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if(nx>=0 && nx<=6 && ny>=0 && ny<=6 && graph[ny][nx]==0){
                    graph[ny][nx]=1;
                    DFS(ny, nx);
                    graph[ny][nx]=0;
                }
            }
        }
    }

    public static void main(String[] args) {
        Q09 T = new Q09();
        Scanner kb = new Scanner(System.in);
        graph = new int[7][7];
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                graph[i][j] = kb.nextInt();
            }
        }
        graph[0][0] = 1;
        T.DFS(0,0);
        System.out.println(answer);
    }
}
