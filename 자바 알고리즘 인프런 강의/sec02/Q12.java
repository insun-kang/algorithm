package com.algo.sec02;

import java.util.Scanner;

public class Q12 {
    public int solution(int n, int m, int[][] arr){
        int answer = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= m; j++) {
                int cnt = 0;
                for (int k = 0; k < n; k++) {
                    int pi = 0;
                    int pj = 0;
                    for (int l = 0; l < m; l++) {
                        if(i == arr[k][l]) pi = l;
                        if(j == arr[k][l]) pj = l;
                    }
                    if(pi<pj){
                        cnt++;
                    }
                }
                if(cnt ==n){
                    answer++;
                }
            }
        }
        return answer;

    }
    public static void main(String[] args) {
        Q12 T = new Q12();
        Scanner kb = new Scanner(System.in);
        int m = kb.nextInt();
        int n = kb.nextInt();
        int[][] arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = kb.nextInt();
            }
        }
        System.out.println(T.solution(n, m, arr));
    }
}
