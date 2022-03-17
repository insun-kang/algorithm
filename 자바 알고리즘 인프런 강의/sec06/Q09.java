package com.algorithm.sec06;

import java.util.Arrays;
import java.util.Scanner;

public class Q09 {
    public int count(int[] arr, int mid){
        int cnt = 1;
        int sum = 0;
        for(int x: arr){
            if(sum + x>mid){
                cnt++;
                sum = x;
            }
            else{
                sum+=x;
            }
        }

        return cnt;

    }
    public int solution(int n, int m, int[] arr){
        int answer = 0;
        int left = Arrays.stream(arr).max().getAsInt();
        int right = Arrays.stream(arr).sum();
        while(left<=right){
            int mid = (left+right)/2;
            if(count(arr, mid)<=m){
                answer = mid;
                right = mid-1;
            }
            else{
                left = mid+1;
            }

        }


        return answer;
    }
    public static void main(String[] args) {
        Q09 T = new Q09();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        System.out.println(T.solution(n, m, arr));
    }
}
