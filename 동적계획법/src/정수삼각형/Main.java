package 정수삼각형;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);
		int n=sc.nextInt();//n: 삼각형 안에있는 숫자의 총 갯수
		int floor=n;//삼각형의 층 수: 0층부터 시작
		for(int i=n-1;i>0;i--)
			n=n+i; 
		
		
		int[] arr=new int[n];//입력받은 cost를 저장할 배열
		int[][] dp=new int[floor][n];//
		for(int i=0;i<n;i++) {
			arr[i]=sc.nextInt();
		}//저장하구
		int flag=1;
		dp[0][0]=arr[0];
		for(int i=1;i<floor;i++) {//i:현재 몇층이야
			for(int j=0;j<i+1;j++) { //현재 층의 몇번째 숫자야
				if(j>0 && j!=i)
					dp[i][j]=Math.max(dp[i-1][j], dp[i-1][j-1])+arr[flag];
				else if(j==0)//j==0:그 층의 처음 숫자는 //outofindex방지
					dp[i][0]=dp[i-1][0]+arr[flag];
				else//그 층의 마지막 숫자는 //j==i일 때
					dp[i][i]=dp[i-1][i-1]+arr[flag];
					
				flag++;
			} 
		}
		int max=dp[floor-1][0];
		for(int i=1;i<floor;i++) {
			if(dp[floor-1][i]>max)
				max=dp[floor-1][i];
		}
		System.out.println(max);	
		
	}

}
