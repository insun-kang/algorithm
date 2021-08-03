package boj_java;

import java.util.*;

public class N2562 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] arr = new int[9];
		int max = Integer.MIN_VALUE;
		int id = 0;
		
		for(int i = 0; i<9;i++) {
			int num = sc.nextInt();
			arr[i] = num;
			if(num>max) {
				max = num;
				id = i+1;
			}
		}
		sc.close();
		System.out.print(max + "\n" + id);
		

	}

}
