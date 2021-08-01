package boj_java;

import java.util.Scanner;

public class N8393 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int result = 0;
		
		for(int i=1;i<n+1;i++) {
			result += i;
		}
		
		sc.close();
		
		System.out.println(result);

	}

}
