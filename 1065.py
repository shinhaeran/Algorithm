#1000보다 작거나 같은 자연수
def find_x(n):
    if n<100: #한자릿수, 두자릿수
        return True

    elif n>100: #세자릿수
        a = n//100
        b = (n-(a*100))//10
        c = n%10
        if (a-b) == (b-c):
            return True
        else:
            return False
    elif n == 1000:

        return False


n = int(input())
total = int()
for i in range(1,n+1):
    if find_x(i):
        total += 1
print(total)
        