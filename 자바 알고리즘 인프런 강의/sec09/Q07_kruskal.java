package com.algorithm.sec09;

import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Edge_a implements Comparable<Edge_a>{
    public int v1;
    public int v2;
    public int cost;
    Edge_a(int v1, int v2, int cost){
        this.v1 = v1;
        this.v2 = v2;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge_a o){
        return this.cost - o.cost;
    }
}
public class Q07_kruskal {
    static int[] unf;
    public int Find(int v){
        if(unf[v] == v) return v;
        else return unf[v] = Find(unf[v]);
    }
    public void Union(int a, int b){
        int fa = Find(a);
        int fb = Find(b);
        if(fa != fb){
            unf[fa] = fb;
        }
    }

    public static void main(String[] args) {
        Q07_kruskal T = new Q07_kruskal();
        Scanner kb = new Scanner(System.in);
        int v = kb.nextInt();
        int e = kb.nextInt();

        unf = new int[v+1];
        ArrayList<Edge_a> arr = new ArrayList<>();
        for (int i = 1; i <= v; i++) {
            unf[i] = i;
        }
        for (int i = 0; i < e; i++) {
            int a = kb.nextInt();
            int b = kb.nextInt();
            int c = kb.nextInt();
            arr.add(new Edge_a(a, b, c));
        }
        int answer = 0;
        Collections.sort(arr);

        for(Edge_a ed:arr){
            int fv1 = T.Find(ed.v1);
            int fv2 = T.Find(ed.v2);
            if(fv1 != fv2){
                answer += ed.cost;
                T.Union(ed.v1, ed.v2);
            }
        }
        System.out.println(answer);
    }

}
