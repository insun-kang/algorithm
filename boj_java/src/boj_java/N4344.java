package boj_java;

import java.util.*;

public class N4344 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] input = new int[n];
		
		for(int i=0;i<n;i++) {
			int cla = sc.nextInt();
			double[] scores = new double[cla];
			
			double sum = 0;
			double avg = 0;
			for(int j=0;j<cla;j++) {
				scores[j] = sc.nextDouble();
				sum += scores[j];
			}
			avg = sum/cla;
			int cnt = 0;
			for(int j=0;j<cla;j++) {
				if(scores[j] > avg) 
					cnt ++;
			}
				
			System.out.printf("%.3f%%\n", (double)cnt/(double)cla*100);
			
		}
		
		sc.close();
	}

}
