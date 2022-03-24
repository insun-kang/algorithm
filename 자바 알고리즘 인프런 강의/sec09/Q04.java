package com.algorithm.sec09;

import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

class Lecture implements Comparable<Lecture>{
    public int cost, due;
    Lecture(int cost, int due){
        this.cost = cost;
        this.due = due;
    }

    @Override
    public int compareTo(Lecture ob){
        return ob.due - this.due;
    }
}
public class Q04 {
    public int solution(int n, ArrayList<Lecture> arr){
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = arr.get(0).due; i > 0; i--) {
            for (int j = 0; j < n; j++) {
                if(arr.get(j).due == i){
                    pq.offer(arr.get(j).cost);
                }
            }
            if(!pq.isEmpty()){
                answer += pq.poll();
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Q04 T = new Q04();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        ArrayList<Lecture> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int cost = kb.nextInt();
            int due = kb.nextInt();
            arr.add(new Lecture(cost, due));
        }
        Collections.sort(arr);
        System.out.println(T.solution(n, arr));
    }

}
