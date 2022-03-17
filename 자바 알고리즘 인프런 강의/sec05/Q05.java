package com.algorithm.sec05;

import java.util.Scanner;
import java.util.Stack;

public class Q05 {
    public int solution(String str){
        int cnt=0;
        Stack<Character> stack=new Stack<>();
        for(int i=0; i<str.length(); i++){
            if(str.charAt(i)=='(') stack.push('(');
            else{
                stack.pop();
                if(str.charAt(i-1)=='(') cnt+=stack.size();
                else cnt++;
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        Q05 T = new Q05();
        Scanner kb = new Scanner(System.in);
        String s = kb.next();
        System.out.println(T.solution(s));
    }
}
