name = "김성민"
jop = "프로그래밍"
age = 23

print("이름은 " + name + "하는일은 " + jop + "나이는 " + str(age))



print("이름은 {0} 하는일은 {1} 나이는 {2}".format(name, jop, age))
#.format을 이용하여 인덱스 할당해서 출력 가능

print(f"이름은 {name} 하는일은 {jop} 나이는 {age}")
#print(f"이름은 {name}") 스트링 문자열을 이용하여 출력 가능 
#직관적이게 출력 가능
