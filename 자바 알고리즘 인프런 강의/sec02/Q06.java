package com.algo.sec02;

import java.util.ArrayList;
import java.util.Scanner;

public class Q06 {
    public ArrayList<Integer> solution(int n, int[] arr){
        ArrayList<Integer> answer = new ArrayList<>();
        int flag = 0;
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(new StringBuilder(Integer.toString(arr[i])).reverse().toString());
            if(num == 1){
                continue;
            }
            for (int j = 2; j < num; j++) {
                if(num%j == 0){
                    flag = 1;
                    break;
                }
            }
            if(flag == 0){
                answer.add(num);
            }
            else{
                flag = 0;
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        Q06 T = new Q06();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        for(int x: T.solution(n, arr)){
            System.out.print(x + " ");
        }
    }
}
