package boj_java;

import java.util.*;

public class N1546 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		double[] scores = new double[n];
		double res = 0;
		for(int i=0;i<n;i++) {
			scores[i] = sc.nextDouble();
		}
		
		Arrays.sort(scores);
		for(int i=0;i<n;i++) {
			res += (scores[i]/scores[n-1])*100;
		}
		System.out.println(res/n);
	}

}
