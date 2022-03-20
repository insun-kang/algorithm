package com.algo.sec01;

import java.util.ArrayList;
import java.util.Scanner;

public class Q13 {
    public ArrayList<Integer> solution(int n, int[] arr){
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(arr[0]);
        for(int i = 0; i<n-1 ;i++){
            if(arr[i] < arr[i+1]){
                answer.add(arr[i+1]);
            }
        }
        return answer;
    }
    public static void main(String[] args){
        Q13 T = new Q13();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i<n; i++){
            arr[i] = kb.nextInt();
        }
        for(int x : T.solution(n, arr)){
            System.out.printf(x + " ");
        }
    }

}
