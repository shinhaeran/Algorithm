package ��ȣ�ǰ�;

import java.util.Scanner;
import java.util.Stack;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		String temp = scan.nextLine();
		
		Stack bracket = new Stack<Character>();

		int flag;
		int total=0; int size =0; char tmp; char previous=1;
		int n[] = new int[(int)temp.length()+1];
		
		for(int i=0; i<temp.length(); i++) {
			
			char c  = temp.charAt(i);//����
			
			if((c == ')' || c == ']') && (previous ==')'|| previous == ']'))
				 flag = 1;
			else flag = 0;
			
			previous = c;//���Ų�
			
			if ( c == '(' || c == '[') { //���� ��ȣ �� ��,
				bracket.push(c);
				
				if( c == '(')
					n[size++] = 2;
				else n[size++] = 3; // {
			}
				
			
			else if ( c ==')' || c ==']') { // �ݴ� ��ȣ �� ��, 
				if(bracket.isEmpty()) {bracket.push('x'); break;}
				
				tmp = (char) bracket.pop(); //���ÿ� ���� �ִ���
				
				if( tmp == '('&& c ==')') 	// ), }�� �� �����ؼ� ���� ���
				{	
					int a = 1;
					for(int j =0; j<size; j++)
						a *= n[j];
					if(flag!=1) total+=a;
					size--;
				}
				
				else if( tmp == '['&& c ==']')
				{
					int a=1;
					for(int j =0; j<size; j++)
						a *= n[j];
					if(flag!=1) total+=a;
					size--;
				}
				
				else  break;
				
			}
				
		}
		
		if(bracket.isEmpty()) System.out.println(total);
		else System.out.println("0");
		
	
	}

}
