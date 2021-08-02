package boj_java;

import java.util.Scanner;

public class N1110 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int answer = n;
		int cnt = 0;
		
		while(true) {
			
			int f = answer/10;
			int s = answer%10;
			answer = s*10 + (f+s)%10;
			cnt += 1;
			if(answer == n) {
				System.out.println(cnt);
				sc.close();
				break;
			}
		}
		
	}

}
