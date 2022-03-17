package com.algorithm.sec07;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Q08 {
    int answer = 0;
    int[] dis = {-1, 1, 5};
    int[] visit = new int[10001];
    Queue<Integer> q = new LinkedList<>();
    public int BFS(int s, int e){
        visit[s] = 1;
        q.offer(s);
        int cnt = 0;
        while(!q.isEmpty()){
            int len = q.size();

            for (int i = 0; i < len; i++) {
                int x = q.poll();
                for (int j = 0; j < 3; j++) {
                    int nx = x+dis[j];
                    if(nx == e){
                        return cnt+1;
                    }
                    if(nx>=1 && nx<=10000 && visit[nx] == 0){
                        visit[nx] = 1;
                        q.offer(nx);
                    }
                }
            }
            cnt++;
        }
        return 0;
    }
    public static void main(String[] args) {
        Q08 T = new Q08();
        Scanner kb = new Scanner(System.in);
        int S = kb.nextInt();
        int E = kb.nextInt();
        System.out.println(T.BFS(S, E));
    }
}
