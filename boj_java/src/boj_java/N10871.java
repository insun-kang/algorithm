package boj_java;

import java.io.*;
import java.util.*;

public class N10871 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		
		int n = Integer.parseInt(st.nextToken());
		int x = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine(), " ");
		for(int i=0;i<n;i++) {
			int result = Integer.parseInt(st.nextToken());
			
			if (result<x) {
				System.out.print(result+" ");
			}
		}
		bw.flush();
		
	}

}
