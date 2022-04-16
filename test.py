cities = ['busan','seoul','jeonju','jeju','ulsan','incheon']
cities[::2]
other_cities = ['new york','toronto','washhington']
total_cities = cities + other_cities
total_cities
'busan' in cities
'new yotk' in cities

cities.append('new_city') # list 맨 뒤에 인덱스 추가
cities
cities.extend(['new1','new2']) # 다른 list를 기존 list에 추가
cities
cities.extend(other_cities)
cities

other_cities.insert(0,'first_city') # insert(n,m) n번째 인덱스에 m을 추가
other_cities

cities.remove('new2') # 해당 인덱스 제거
cities

cities[0] = 'del_index_new_index' # 특정 위치의 인덱스 변경
cities
del cities[0] # 특정 위치의 인덱스 제거
cities

t = [1,2,3]
a,b,c = t # a,b,c 순서대로 인덱스 0,1,2 위치의 값을 저장
print(t,a,b,c)

add_cities_t_list = [cities,other_cities,t]
add_cities_t_list # 2차원 배열
add_cities_t_list[0][1] # n번쩨 배열에서 m번째 인덱스 출력
add_cities_t_list[1][1]
add_cities_t_list[2][1]

other_cities[0] = '1000'
add_cities_t_list
cities is other_cities
a= 1
b=1
a is b

a = ['color',12,34.5]
color = ['red','blue','white']
a
a[0] = color
a
b = [1,5,7,10,2]
b.sort()
b

a=100
b=100
a is b
a ==b
a= 300
b=300
a == b
a is b
if 1:print("true")
else:print('false')

