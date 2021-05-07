# 주석
# js: console.log('test')
print('test')

# let const 없음
number = 1
float_number = 1.1  # js에서는 일반적으로 floatNumber
string = '문자열'
boolean = True  # js에서는 true

# list, dict 거의 똑같음
number_list = [1, 2, 3, 4]
print(number_list[0])  # 1
number_list.append(5)  # js에서는 number_list.push(5)

string_dict = {'name': 'kim', 'age': 30}
print(string_dict['name'])  # kim

# python의 특징
# 들여쓰기가 아주 중요함
if number > 10:
    print('10보다 큽니다')
else:
    print('10보다 작습니다')
print('상관없음')

for num in number_list:
    print(num)

# 함수
def func(num):
    print(num)

def sum(num1, num2):
    result = num1 + num2
    return result

print(sum(10, 20))

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

count = 0
for fruit in fruits:
    if fruit == '사과':  # js와 다르게 == 사용
        count = count + 1
print(count)
