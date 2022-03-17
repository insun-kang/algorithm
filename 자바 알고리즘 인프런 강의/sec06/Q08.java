package com.algorithm.sec06;

import java.util.Arrays;
import java.util.Scanner;

public class Q08 {
    public int solution(int n, int m, int[] arr){
        int answer = 0;
        Arrays.sort(arr);
        int left = 0, right = n-1;

        while(left<=right){
            int mid = (left+right)/2;
            if(arr[mid]==m){
                answer = mid+1;
                break;

            }
            if(arr[mid]<=m){
                left = mid+1;
            }
            else{
                right = mid-1;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Q08 T = new Q08();
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
