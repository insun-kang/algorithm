package com.algorithm.sec03;

import java.util.Scanner;

public class Q05 {
    public int solution(int n){
        int answer = 0;
        int sum = 0;
        int tmp = 1;
        for (int i = 0; i < n; i++) {
            sum += i;
            if(sum==n){
                answer++;
            }
            while(sum>n){
                sum -= tmp;
                tmp++;
                if(sum ==n){
                    answer++;
                    break;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Q05 T = new Q05();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        System.out.println(T.solution(n));

    }
}
