package 계단오르기;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();//계단의 갯수
		int dp[][]=new int[n][3];//마지막 1은 계단중복검사(1칸씩 오른 count 세는거)
		
		for(int i=0;i<n;i++)
			dp[i][0]=sc.nextInt();//dp 0번째는 시작에서 바로인 값이니까->cost와 동일
		
		dp[1][1]=dp[0][0]+dp[1][0];
		dp[1][2]=dp[1][0];
		dp[2][1]=dp[2][0]+dp[1][0];
		dp[2][2]=dp[2][0]+dp[0][0];
		
		//모든 경로 계산-> 메모이제이션
		for(int i=3;i<n;i++) {
			dp[i][1]=dp[i-1][2]+dp[i][0];//바로 전꺼의 경로 +원래꺼 cost
			dp[i][2]=Math.max(dp[i-2][1], dp[i-2][2])+dp[i][0];
			
		}
		System.out.println(Math.max(dp[n-1][1], dp[n-1][2]));

	}

}
