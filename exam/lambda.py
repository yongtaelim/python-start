# encoding: utf-8

def sum(x, y):
	return x + y
	
print 'general function sum :: ', sum(4, 50)

print 'lambda sum :: ', (lambda x,y: x+y)(4,50)

'''map(함수, 리스트)'''
print 'lambda map :: ', map(lambda x: x ** 2, range(5)) 
print 'lambda list map :: ', list(map(lambda x: x ** 2, range(5))) 

'''reduce(함수, 순서형 자료)'''
from functools import reduce
print 'reduce :: ', reduce(lambda x, y: x + y, range(5))

'''filter(함수, 리스트)'''
print 'filter :: ', filter(lambda x: x < 5, range(10))
print 'list filter :: ', list(filter(lambda x: x < 5, range(10)))