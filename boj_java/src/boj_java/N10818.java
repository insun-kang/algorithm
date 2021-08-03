package boj_java;

import java.util.Scanner;
import java.util.Arrays;

public class N10818 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] arr = new int[n];
		
		for(int i = 0; i<n;i++) {
			int num = sc.nextInt();
			arr[i] = num;
		}
		
		sc.close();
		
		Arrays.sort(arr);
		System.out.println(arr[0] + " " + arr[n-1]);
	}

}
