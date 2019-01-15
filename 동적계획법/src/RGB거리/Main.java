package RGB�Ÿ�;

import java.util.Scanner;

public class Main {
	static long total=0;
	static int secondaryP=0;//prev
	static int secondaryN=0;
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		
		int color[]=new int[n];//���� �� ĥ�ߴ��� ����-> �� �� �� 0 1 2
		long arg[][]=new long[n][3];// �� ĥ�ϴ� ��� ����
		for(int i=0;i<n;i++) {
			for(int j=0;j<3;j++)
				arg[i][j]=sc.nextLong();
		}
		
		color[0]=(arg[0][0]>arg[0][1])?1:0;
		color[0]=(arg[0][color[0]]>arg[0][2])? 2:color[0];
		switch (color[0]) {
		case 0: {secondaryP=(arg[0][1]>arg[0][2])?2:1;} break;
		case 1: {secondaryP=(arg[0][0]>arg[0][2])?2:0;}break;
		case 2: {secondaryP=(arg[0][1]>arg[0][0])?0:1;};
	}
		
		for(int i=1;i<n;i++) {//�� ���ϱ� i:���°��
			colorMatch(i,color,arg);//����������
		}
		
		for(int i=0;i<n;i++) {
			total=total+arg[i][color[i]];
			
		}
		System.out.println(total);
	}
	
	static void colorMatch(int i,int[] color,long[][] arg) {
		int prevColorIndex=color[i-1];
		switch (prevColorIndex) {
			case 0: {color[i]=(arg[i][1]>arg[i][2])?2:1;  secondaryN=(arg[i][1]<arg[i][2])?2:1;} break;
			case 1: {color[i]=(arg[i][0]>arg[i][2])?2:0;  secondaryN=(arg[i][0]<arg[i][2])?2:0;}break;
			case 2: {color[i]=(arg[i][1]>arg[i][0])?0:1;  secondaryN=(arg[i][1]<arg[i][0])?0:1;};
		}
		
		if(arg[i][prevColorIndex]<arg[i][color[i]]) { //�������� �ּڰ��� �� ���� ���� ���ļ� ���ܵƴٸ�
			if(arg[i][prevColorIndex]+ arg[i-1][secondaryP]<arg[i][color[i]]+arg[i-1][prevColorIndex]) {//���� �ּڰ��� �� ���� 2��° ���� �� ->������ swap
				color[i-1]=secondaryP;//���� �� ���� �ι�°�� ���������� �ٲٰ�
				secondaryP=color[i];//secondaryP �������� ���� update, ���⼭ color[i]�� �ι�°�� ���� ��
				color[i]=prevColorIndex;//���� ���� ���� �ּڰ�����
			}
			else secondaryP=secondaryN;//secondaryP:�� ���� 2��°�� ���� ��(index) 0 1 2
		}
		else secondaryP=secondaryN;
		
	}
}