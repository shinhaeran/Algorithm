package ��ܿ�����;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();//����� ����
		int dp[][]=new int[n][3];//������ 1�� ����ߺ��˻�(1ĭ�� ���� count ���°�)
		
		for(int i=0;i<n;i++)
			dp[i][0]=sc.nextInt();//dp 0��°�� ���ۿ��� �ٷ��� ���̴ϱ�->cost�� ����
		
		dp[1][1]=dp[0][0]+dp[1][0];
		dp[1][2]=dp[1][0];
		dp[2][1]=dp[2][0]+dp[1][0];
		dp[2][2]=dp[2][0]+dp[0][0];
		
		//��� ��� ���-> �޸������̼�
		for(int i=3;i<n;i++) {
			dp[i][1]=dp[i-1][2]+dp[i][0];//�ٷ� ������ ��� +������ cost
			dp[i][2]=Math.max(dp[i-2][1], dp[i-2][2])+dp[i][0];
			
		}
		System.out.println(Math.max(dp[n-1][1], dp[n-1][2]));

	}

}
