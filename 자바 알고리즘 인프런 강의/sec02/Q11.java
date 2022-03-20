package com.algo.sec02;

import java.util.Scanner;

public class Q11 {
    public int solution(int n, int[][] arr){
        int answer = 0;
        int max = 0;

        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {

                for (int k = 0; k < 5; k++) {
                    if(arr[i][k] == arr[j][k]){
                        cnt++;
                        break;
                    }
                }

            }
            System.out.println(cnt);
            if(cnt > max){
                max = cnt;
                answer = i;
            }
        }

        return answer+1;
    }
    public static void main(String[] args) {
        Q11 T = new Q11();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[][] arr = new int[n][5];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 5; j++) {
                arr[i][j] = kb.nextInt();
            }
        }
        System.out.println(T.solution(n, arr));
    }
}
