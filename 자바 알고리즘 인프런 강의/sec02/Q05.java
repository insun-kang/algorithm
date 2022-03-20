package com.algo.sec02;

import java.util.ArrayList;
import java.util.Scanner;

public class Q05 {
    public int solution(int n){
        int[] arr = new int[n+1];
        int cnt = 0;

        for (int i = 2; i <=n ; i++) {
            if(arr[i]==0){
                cnt++;
                for (int j = i; j <=n ; j=j+i) {
                    arr[j]=1;
                }
            }
        }

        return cnt;
    }
    public static void main(String[] args) {
        Q05 T = new Q05();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        System.out.println(T.solution(n));
    }
}
