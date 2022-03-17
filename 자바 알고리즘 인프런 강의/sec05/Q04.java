package com.algorithm.sec05;

import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Q04 {
    public int solution(String s){
        int answer = 0;
        char[] op = {'*', '-', '+', '/'};
        Stack<Integer> stack = new Stack<>();
        for(char c: s.toCharArray()){
            int val = 0;
            if(c == '*'){
                val = stack.pop() * stack.pop();
                stack.push(val);
            }
            else if(c == '/'){
                val = stack.pop() / stack.pop();
                stack.push(val);
            }
            else if(c == '-'){
                int f1 = stack.pop();
                int f2 = stack.pop();
                val = f2-f1;
                stack.push(val);
            }
            else if(c == '+'){
                val = stack.pop() + stack.pop();
                stack.push(val);
            }
            else{
                stack.push(c-48);
            }

        }

        return stack.pop();
    }

    public static void main(String[] args) {
        Q04 T = new Q04();
        Scanner kb = new Scanner(System.in);
        String s = kb.next();
        System.out.println(T.solution(s));
    }

}
