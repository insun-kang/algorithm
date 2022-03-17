package com.algorithm.sec03;

import java.util.Scanner;

public class Q03 {
    public int solution(int n, int m, int[] arr){
        int p1 = 0;
        int answer = 0;
        int sum = 0;
        for (int i = 0; i < m; i++) {
            answer += arr[i];
            sum = answer;
        }
        for (int i = 0; i < n-m; i++) {
            sum -= arr[i];
            sum += arr[i+m];
            if(sum>answer){
                answer = sum;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Q03 T = new Q03();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        System.out.print(T.solution(n, m, arr));

    }

}
