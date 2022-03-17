package com.algorithm.sec05;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Q06 {
    public int solution(int n, int m){
        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            q.offer(i+1);
        }
        while (!q.isEmpty()) {
            for (int i = 0; i < m-1; i++){
                q.offer(q.poll());
            }
            q.poll();
            if(q.size()==1){
                answer = q.poll();
            }

        }

        return answer;
    }

    public static void main(String[] args) {
        Q06 T = new Q06();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();
        System.out.println(T.solution(n, m));
    }

}
