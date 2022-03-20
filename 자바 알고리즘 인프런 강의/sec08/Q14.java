package com.algo.sec08;

import java.util.ArrayList;
import java.util.Scanner;

class Point{
    public int x, y;

    Point(int x, int y){
        this.y = y;
        this.x = x;
    }
}

public class Q14 {
    static int n , m, len, answer = Integer.MAX_VALUE;
    static ArrayList<Point> hs, pz;
    static int[] combi;
    public void DFS(int L, int s){
        if(L == m){
            int sum = 0;
            for(Point h:hs) {
                int dis = Integer.MAX_VALUE;
                for (int i : combi) {
                    dis = Math.min(dis, Math.abs(h.y - pz.get(i).y)+Math.abs(h.x - pz.get(i).x));
                }
                sum += dis;
            }
            answer = Math.min(answer, sum);

        }
        else{
            for (int i = s; i < len; i++) {
                combi[L] = i;
                DFS(L+1, i+1);
            }
        }
    }

    public static void main(String[] args) {
        Q14 T = new Q14();
        Scanner kb = new Scanner(System.in);
        n = kb.nextInt();
        m = kb.nextInt();
        combi = new int[m];
        hs = new ArrayList<>();
        pz = new ArrayList<>();
        for (int y = 0; y < n; y++) {
            for (int x= 0; x < n; x++) {
                int tmp = kb.nextInt();
                if(tmp == 1){
                    hs.add(new Point(y,x));
                }
                else if(tmp == 2){
                    pz.add(new Point(y, x));
                }
            }

        }
        len = pz.size();
        T.DFS(0,0);;
        System.out.println(answer);

    }

}
