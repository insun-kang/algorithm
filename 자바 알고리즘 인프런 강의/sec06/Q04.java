package com.algorithm.sec06;

import java.util.Scanner;

public class Q04 {
public int[] solution(int s, int n, int[] arr){
    int[] cache = new int[s];

    for(int x: arr){
        int idx = -1;
        for (int i = 0; i < s; i++) {
            if (cache[i]==x){
                idx = i;
            }
        }
        if(idx == -1){
            for (int i = s-2; i >= 0; i--) {
                cache[i+1] = cache[i];
            }
        }
        else{
            for (int i = idx-1; i >= 0; i--) {
                cache[i+1] = cache[i];
            }
        }
        cache[0] = x;
    }


    return cache;
}

    public static void main(String[] args) {
        Q04 T = new Q04();
        Scanner kb = new Scanner(System.in);

        int s = kb.nextInt();
        int n = kb.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        for(int x: T.solution(s, n, arr)){
            System.out.print(x + " ");
        }

    }

}
