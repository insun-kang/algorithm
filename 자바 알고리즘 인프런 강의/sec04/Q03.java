package com.algorithm.sec04;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Q03 {
    public ArrayList<Integer> solution(int n, int m, int[] arr){
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < m; i++) {
            map.put(arr[i], map.getOrDefault(arr[i],0)+1);
        }
        answer.add(map.size());
        for (int i = m; i <n ; i++) {

            map.put(arr[i], map.getOrDefault(arr[i],0)+1);
            map.put(arr[i-m], map.get(arr[i-m])-1);
            if(map.get(arr[i-m])==0){
                map.remove(arr[i-m]);
            }
            answer.add(map.size());
        }
        return answer;
    }

    public static void main(String[] args) {
        Q03 T = new Q03();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i]=kb.nextInt();
        }
        for(int x:T.solution(n, m, arr)){
            System.out.print(x + " ");
        }
    }
}
