package 괄호의값;

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
			
			char c  = temp.charAt(i);//현재
			
			if((c == ')' || c == ']') && (previous ==')'|| previous == ']'))
				 flag = 1;
			else flag = 0;
			
			previous = c;//과거꺼
			
			if ( c == '(' || c == '[') { //여는 괄호 일 떄,
				bracket.push(c);
				
				if( c == '(')
					n[size++] = 2;
				else n[size++] = 3; // {
			}
				
			
			else if ( c ==')' || c ==']') { // 닫는 괄호 일 때, 
				if(bracket.isEmpty()) {bracket.push('x'); break;}
				
				tmp = (char) bracket.pop(); //스택에 남아 있던게
				
				if( tmp == '('&& c ==')') 	// ), }일 때 따로해서 에러 잡기
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
