package �����ﰢ��;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);
		int n=sc.nextInt();//n: �ﰢ�� �ȿ��ִ� ������ �� ����
		int floor=n;//�ﰢ���� �� ��: 0������ ����
		for(int i=n-1;i>0;i--)
			n=n+i; 
		
		
		int[] arr=new int[n];//�Է¹��� cost�� ������ �迭
		int[][] dp=new int[floor][n];//
		for(int i=0;i<n;i++) {
			arr[i]=sc.nextInt();
		}//�����ϱ�
		int flag=1;
		dp[0][0]=arr[0];
		for(int i=1;i<floor;i++) {//i:���� �����̾�
			for(int j=0;j<i+1;j++) { //���� ���� ���° ���ھ�
				if(j>0 && j!=i)
					dp[i][j]=Math.max(dp[i-1][j], dp[i-1][j-1])+arr[flag];
				else if(j==0)//j==0:�� ���� ó�� ���ڴ� //outofindex����
					dp[i][0]=dp[i-1][0]+arr[flag];
				else//�� ���� ������ ���ڴ� //j==i�� ��
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
