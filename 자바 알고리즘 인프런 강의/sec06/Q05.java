package com.algorithm.sec06;

import java.util.Arrays;
import java.util.Scanner;

public class Q05 {
    public char solution(int n, int[] arr){
        char answer = 'U';
        Arrays.sort(arr);
        for (int i = 0; i < n-1; i++) {
            if(arr[i]==arr[i+1]){
                return 'D';
            }

        }

        return answer;
    }

    public static void main(String[] args) {
        Q05 T = new Q05();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        System.out.println(T.solution(n, arr));
    }
}
