package com.algorithm.sec05;

import java.util.Scanner;
import java.util.Stack;

public class Q03 {
    public int solution(int n, int[][] board, int m, int[] moves){
        int answer = 0;
        Stack<Integer> box = new Stack<>();

        for(int pos:moves){
            int x = pos-1;
            for (int y = 0; y < n; y++) {
                if(board[y][x] != 0){
                    if(!box.isEmpty() && box.peek()==board[y][x]){
                        box.pop();
                        answer += 2;
                    }
                    else{
                        box.push(board[y][x]);
                    }
                    board[y][x] =0;
                    break;

                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Q03 T = new Q03();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = kb.nextInt();
            }
        }
        int m = kb.nextInt();
        int[] moves = new int[m];
        for (int i = 0; i < m; i++) {
            moves[i] = kb.nextInt();
        }

        System.out.println(T.solution(n, board, m, moves));
    }

}
