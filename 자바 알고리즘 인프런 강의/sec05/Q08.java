package com.algorithm.sec05;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Person{
    int id;
    int priority;
    public Person(int id, int priority){
        this.id = id;
        this.priority = priority;
    }
}

public class Q08 {
    public int solution(int n, int m, int[] arr){
        int answer = 0;
        Queue<Person> q = new LinkedList<>();

        for (int i = 0; i < arr.length; i++) {
            q.offer(new Person(i, arr[i]));
        }
        while (!q.isEmpty()){
            Person tmp = q.poll();
            for(Person person:q){
                if(tmp.priority<person.priority){
                    q.offer(tmp);
                    tmp = null;
                    break;
                }
            }
            if(tmp != null){
                answer++;
                if(tmp.id == m){
                    return answer;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Q08 T = new Q08();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }
        System.out.println(T.solution(n, m, arr));
    }

}
