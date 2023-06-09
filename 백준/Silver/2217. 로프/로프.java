import java.util.*;
public class Main{

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] ropes = new int[n];
		for (int i = 0; i < n; i++) ropes[i] = sc.nextInt();
		sc.close();
		
		Arrays.sort(ropes);
		for (int i = n-1; i >= 0; i--) ropes[i] *= (n-i);
		Arrays.sort(ropes);
		System.out.println(ropes[n-1]);
		
	}

}