package RGB거리;

import java.util.Scanner;

public class Main {
	static long total=0;
	static int secondaryP=0;//prev
	static int secondaryN=0;
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		
		int color[]=new int[n];//무슨 색 칠했는지 저장-> 빨 초 파 0 1 2
		long arg[][]=new long[n][3];// 색 칠하는 비용 저장
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
		
		for(int i=1;i<n;i++) {//색 정하기 i:몇번째집
			colorMatch(i,color,arg);//빨파초인지
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
		
		if(arg[i][prevColorIndex]<arg[i][color[i]]) { //현재집의 최솟값이 전 집의 색과 겹쳐서 제외됐다면
			if(arg[i][prevColorIndex]+ arg[i-1][secondaryP]<arg[i][color[i]]+arg[i-1][prevColorIndex]) {//지금 최솟값과 전 집의 2번째 비용과 비교 ->같으면 swap
				color[i-1]=secondaryP;//전의 집 색을 두번째로 작은색으로 바꾸고
				secondaryP=color[i];//secondaryP 다음꺼를 위해 update, 여기서 color[i]는 두번째로 작은 색
				color[i]=prevColorIndex;//현재 집의 색을 최솟값으로
			}
			else secondaryP=secondaryN;//secondaryP:전 집의 2번째로 작은 색(index) 0 1 2
		}
		else secondaryP=secondaryN;
		
	}
}