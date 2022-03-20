package com.algo.sec09;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

class Room implements Comparable<Room>{
    public int start, end;
    Room(int start, int end){
        this.start = start;
        this.end = end;
    }

    @Override
    public int compareTo(Room r){
        if(r.end == this.end) return this.start - r.start;
        else return this.end - r.end;
    }

}
public class Q02 {
    public int solution(int n, ArrayList<Room> arr){
        int answer = 0;
        int time = 0;
        for(Room x: arr){
            if(x.start>=time){
                time = x.end;
                answer++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Q02 T = new Q02();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        ArrayList<Room> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int start = kb.nextInt();
            int end = kb.nextInt();
            arr.add(new Room(start, end));
        }
        Collections.sort(arr);
        System.out.println(T.solution(n, arr));

    }
}
