package boj_java;

class Test{
	long sum(int[] a) {
		int sum = 0;
		for(int i =0;i<a.length;i++) {
			sum += a[i];
		}
		
		return sum;
		
	}
}

public class N15596 {

	public static void main(String[] args) {
		int[] a = {1, 2, 3, 4};
		int result = sum(a);
		System.out.println(result);

	}


}
