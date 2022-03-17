package com.algorithm.sec05;

import java.util.Scanner;
import java.util.Stack;

public class Q02 {
    public String solution(String s){
        String answer = "";
        Stack<Character> stack = new Stack<>();

        for(char x: s.toCharArray()){
            if(x == ')'){
                while(true){
                    if(stack.pop() =='('){
                        break;
                    }
                }
            }
            else{
                stack.push(x);
            }
        }
        for(char x:stack){
            answer +=x;
        }

        return answer;
    }

    public static void main(String[] args) {
        Q02 T = new Q02();
        Scanner kb = new Scanner(System.in);
        String s = kb.next();
        System.out.println(T.solution(s));
    }
}
