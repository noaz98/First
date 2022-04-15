# 앞뒤 어느쪽에서 읽어도 동일한 단어 ex.eye
# 회문인지 아닌지 작성
#조건#1. 'input' 등의 함수를 사용하여 사용자로 부터 임의의 단어를 입력받고, 그 단어가 회문인지 아닌지를 출력해야한다.
#조건#2. 연결리스트를 활용해야하므로 반드시 아래의 클래스를 사용하시오.
# class Node():
# def __init__(self):
# self.data=None
# self.link=None
# 조건#3. 최종출력은 '회문입니다.' 또는 '회문이 아닙니다.' 가 출력되어야한다.
from platform import node
from requests import head


class Node:
    def __init__(self):    
        self.data = None
        self.link = None
        self.next = next
    
head,current,pre,tail = None,None,None,None
dataArray = input('문자를 입력하세요:')
dataArray = list(dataArray)

node = Node() #node라는 임의의 Node 생성
node.data = dataArray[0]# node 안에 dataArray[0]의 데이터 삽입
head = node # head에 node 저장, 0배열의 데이터

for data in dataArray[1:]: # dataArray[1]이상으로 슬라이싱, 안에 data가
    #존재할 때까지 반복문 실행
   pre = node # pre에 node 저장
   node = Node() # node를 Node로 선언하여 기존의 node는 리셋
   node.data = data # node에 슬라이싱된 데이터 저장
   pre.link = node # pre에 node 연결
   
if current.link == pre.link:
    print('회문입니다.')
else:
    print('회문이 아닙니다.')