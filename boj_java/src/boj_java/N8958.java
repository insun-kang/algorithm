package boj_java;

import java.util.*;
public class N8958 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		String[] arr = new String[n];
		
		for(int i=0;i<n;i++) {
			arr[i] = sc.next();
		}
		
		sc.close();
		
		for(int i=0;i<n;i++) {
			int cnt = 0;
			int sum = 0;
			
			for(int j=0;j<arr[i].length();j++) {
				if(arr[i].charAt(j)=='O') {
	
					cnt++;
					sum += cnt;
				}
				else
					cnt = 0;
				
			}
			
			System.out.println(sum);
		}

	}

}
