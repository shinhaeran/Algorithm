package RGB�Ÿ�;
//rgb�Ÿ� �ٽ�~~~~~~~~~~~~~ �Ф̤�

import java.util.Scanner;

public class Main2 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int arg[][]=new int[n][3];// �� ĥ�ϴ� ��� ����
		for(int i=0;i<n;i++) {
			for(int j=0;j<3;j++)
				arg[i][j]=sc.nextInt();
		}
		
		int totalC[][]=new int[n][3];
		
		for(int i=0;i<3;i++) {//n-1������ total�� ���� �������� �� total
			totalC[0][i]=arg[0][i]; //ù��°�ϱ� ���� ��� �־��ְ�
		}
		int total=0;
		
		for(int i=1;i!=n ;i++) {
			totalC[i][0]=Math.min(totalC[i-1][1], totalC[i-1][2])+arg[i][0];
			totalC[i][1]=Math.min(totalC[i-1][2], totalC[i-1][0])+arg[i][1];
			totalC[i][2]=Math.min(totalC[i-1][0], totalC[i-1][1])+arg[i][2];
		}
		total=Math.min(totalC[n-1][0], totalC[n-1][1]);
		total=Math.min(totalC[n-1][2], total);
		
		System.out.println(total);
	}
		

}
	
	


