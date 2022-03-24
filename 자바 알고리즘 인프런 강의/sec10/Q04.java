package com.algorithm.sec10;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

class Brick implements Comparable<Brick>{
    public int s, h, w;
    Brick(int s, int h, int w){
        this.s = s;
        this.h = h;
        this.w = w;
    }
    @Override
    public int compareTo(Brick b){
        return b.s - this.s;
    }
}

public class Q04 {
    static int[] dp;
    public int solution(int n, ArrayList<Brick> arr){
        int answer = 0;

        for (int i = 1; i < n; i++) {
            int max_h = 0;
            for (int j = i-1; j >= 0 ; j--) {
                if(arr.get(i).w < arr.get(j).w && max_h < dp[j]){
                    max_h = dp[j];
                }
            }
            dp[i] = max_h + arr.get(i).h;
            answer = Math.max(answer, dp[i]);
        }


        return answer;
    }
    public static void main(String[] args) {
        Q04 T = new Q04();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        ArrayList<Brick> arr = new ArrayList<Brick>();

        for (int i = 0; i < n; i++) {
            int a = kb.nextInt();
            int b = kb.nextInt();
            int c = kb.nextInt();

            arr.add(new Brick(a, b, c));
        }
        Collections.sort(arr);

        dp = new int[n];
        dp[0] = arr.get(0).h;

        System.out.println(T.solution(n, arr));
    }
}
