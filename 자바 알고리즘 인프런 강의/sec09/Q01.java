package com.algo.sec09;

import java.util.*;

class Body implements Comparable<Body>{
    public int h, w;
    Body(int h, int w){
        this.h = h;
        this.w = w;
    }
    @Override
    public int compareTo(Body o){
        return o.h - this.h;
    }

}


public class Q01 {

    public int solution(int n,  ArrayList<Body> arr){
        int answer = 0;
        int max = Integer.MIN_VALUE;
        for(Body b: arr){
            if(b.w>max){
                max = b.w;
                answer++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Q01 T = new Q01();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        ArrayList<Body> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int h = kb.nextInt();
            int w = kb.nextInt();
            arr.add(new Body(h, w));
        }
        Collections.sort(arr);
        System.out.println(T.solution(n, arr));
    }
}
