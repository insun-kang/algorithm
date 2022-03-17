package com.algorithm.sec03;

import java.util.Scanner;

public class Q07 {
    public int solution(int n, int m, int[] arr){
        int answer = 0;
        int left = 0, right = 0;
        int max = 0;
        int cnt =0;
        while(true){
            int result = find(left, right, arr);
            int gap = right - left;
            if(result == m){
                if(gap > max){
                    max = gap;
                }
                right++;
            }
            else if(result > m){
                left++;
            }
            else{
                right++;
            }
            if(left>=n || right>=n){
                break;
            }
            System.out.println("left :" + left);
            System.out.println("right :"+ right);
            System.out.println("max :" + max);

        }

        return max+1;
    }
    public int find(int left, int right, int[] arr){
        int cnt =0;
        for (int i = left; i <= right; i++) {
            if(arr[i]==0){
                cnt++;
            }
        }
        return cnt;
    }
    public static void main(String[] args) {
        Q07 T = new Q07();
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
