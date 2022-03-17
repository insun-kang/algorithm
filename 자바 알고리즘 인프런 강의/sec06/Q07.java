package com.algorithm.sec06;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Point implements Comparable <Point>{
    public int x, y;
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
    @Override
    public int compareTo(Point o){
        if(this.x==o.x)return this.y-o.y;
        else return this.x-o.x;
    }
}

public class Q07 {
    public static void main(String[] args) {
        Q07 T = new Q07();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        ArrayList<Point> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int x = kb.nextInt();
            int y = kb.nextInt();
            arr.add(new Point(x, y));
        }
        Collections.sort(arr);
        for(Point x:arr){
            System.out.println(x.x + " " + x.y);
        }

    }

}
