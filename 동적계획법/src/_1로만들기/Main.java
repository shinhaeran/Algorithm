package _1�θ����;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int dp[] = new int[1000001];
		
		dp[1] = 0; dp[2] = 1; dp[3] = 1;
		
		if(dp[n]!=0 || n==1) System.out.println(dp[n]);  
		else System.out.println(Find1Cost(dp,n));
		
	}
	
	
	public static int Find1Cost(int[] dp, int n) { //dp[n]�� ���ϴ� �Լ�: n�� 1�� ����� �ּҿ���Ƚ��
		int div3=0;
		int div2=0;
		int minus=0;
		int max = 99999999;
		
		if (n%3!=0) div3=max; 
		else if (dp[n/3]==0) div3 = Find1Cost(dp,n/3); //������ ã��
		else div3=dp[n/3];//������ �ִ°� ����
		
		if (n%2!=0) div2=max;
		else if (dp[n/2]==0) div2 = Find1Cost(dp,n/2);
		else div2=dp[n/2];
		
		if(dp[n-1]!=0) minus = dp[n-1];
		else minus = Find1Cost(dp,n-1); //������ ã�ƾ� ����?
		
		dp[n] = Math.min(div3, Math.min(div2, minus)) + 1;
		
		return dp[n];
	}
}



