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