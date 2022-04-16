import random
from tkinter import N

## 함수 선언 부분 ##
def isStackFull() :
	global SIZE, stack, top
	if (top >= SIZE-1) :
		return True
	else :
		return False

def isStackEmpty() :
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

def push(data) :
	global SIZE, stack, top
	if (isStackFull()) :
		return
	top += 1
	stack[top] = data

def pop() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

def peek() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		return None
	return stack[top]

## 전역 변수 선언 부분 ##
SIZE = 10
stack = [ None for _ in range(SIZE) ]
top = -1

## 메인 코드 부분 ##
if __name__ == "__main__" :
	push('주황') # top = 0
	push('초록') # top = 1
	push('파랑') # top = 2
	push('보라') # top = 3
	push('빨강') # top = 4
	push('노랑') # top = 5
	
	print('과자집에 가는 길: ',end='')
	for i in range(top+1):
		print(stack[i],end='-->')
		if i == 5:
			push('과자집')
			print(pop())
			break

	print('우리집에 오는 길: ',end='')
	for i in range(len(stack)):
		retData = pop()
		print(retData,end='-->')
		if stack[top]==None:
			push('우리집')
			print(pop())
			break