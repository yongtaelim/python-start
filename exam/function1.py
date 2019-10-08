print('function practice')

def sum(a,b):
	print(a+b)
	
def multi(a,b):
	print(a*b)
	
def test(a,b):
	sum(a,b)
	multi(a,b)
	
test(10, 40)	

def countDown(n):
    if n == 0:
        print("count down end...")
    else:
        print(n)
        countDown(n-1)
        
print('count down start')
countDown(5)