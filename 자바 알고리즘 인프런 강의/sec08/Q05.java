package com.algorithm.sec08;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Q05 {
    static int n, m, answer = Integer.MAX_VALUE;
    static ArrayList<Integer> coin;
    public void DFS(int L, int sum){
        if(sum>m)return;
        if(L>=answer)return;
        if(sum==m) answer = Math.min(answer, L);
        else{
            for (int i = 0; i < n; i++) {
                DFS(L+1, sum+coin.get(i));
            }
        }
    }

    public static void main(String[] args) {
        Q05 T = new Q05();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        coin = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            coin.add(kb.nextInt());
        }
        coin.sort(Comparator.reverseOrder());
        m = kb.nextInt();
        T.DFS(0, 0);
        System.out.println(answer);
    }
}
