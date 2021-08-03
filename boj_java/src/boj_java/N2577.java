package boj_java;

import java.util.*;

public class N2577 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int mul = sc.nextInt()*sc.nextInt()*sc.nextInt();
		
		String s = Integer.toString(mul);
		
		int[] arr = new int[10];
		
		for(int i=0;i<s.length();i++) {
			arr[s.charAt(i)-'0'] += 1;
		}
		
		for(int i:arr) {
			System.out.println(i);
		}
	}

}
