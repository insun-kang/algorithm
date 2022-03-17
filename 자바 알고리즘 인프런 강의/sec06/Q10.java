package com.algorithm.sec06;

import java.util.Arrays;
import java.util.Scanner;

public class Q10 {
    public int count(int[] arr, int mid){
        int cnt = 1;
        int ep = arr[0] ;
        for (int i = 1; i < arr.length; i++) {
            if(arr[i] - ep>=mid){
                cnt++;
                ep = arr[i];
            }
        }

        return cnt;
    }
    public int solution(int n, int m, int[] arr){
        int answer = 0;
        Arrays.sort(arr);
        int left = 1, right = arr[n-1];

        while(left<=right){
            int mid = (left+right)/2;
            if(count(arr, mid) >= m){
                answer = mid;
                left = mid+1;
            }
            else{
                right = mid-1;
            }

        }

        return answer;
    }
    public static void main(String[] args) {
        Q10 T = new Q10();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        System.out.println(T.solution(n, m, arr));
    }

}
