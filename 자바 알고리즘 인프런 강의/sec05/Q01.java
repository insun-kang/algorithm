package com.algorithm.sec05;

import java.util.Scanner;
import java.util.Stack;

public class Q01 {
    public String solution(String s){
        String  answer = "YES";
        Stack<Character> stack = new Stack<>();
        for(char x:s.toCharArray()){
            if(x =='('){
                stack.push(x);
            }
            else{
                if(stack.isEmpty()){
                    return "NO";
                }
                stack.pop();
            }
        }
        if(!stack.isEmpty()){
            return "NO";
        }

        return answer;
    }

    public static void main(String[] args) {
        Q01 T = new Q01();
        Scanner kb = new Scanner(System.in);
        String s = kb.next();
        System.out.println(T.solution(s));
    }
}
