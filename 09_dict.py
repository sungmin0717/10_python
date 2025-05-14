user = {"name" : "김성민", 
        "jop" : "프로그래머", 
        "email" : "sungmin@gmail.com"}
#벨류 형태는 숫자,문자,리스트 준부 삽입 가능
#{"키" : "벨루"}

print(user)

user["age"] = 15
#추가 가능

print(user)

# del user["name"]
# 삭제 가능

print(user)

print(user["name"])
print(user["jop"])
print(user["email"])
#key를 삽입해서 벨류 가져옴


keys_list = user.keys()
keys_list = list(keys_list)
#list 형태로 변경 가능

print(keys_list)
#dict_keys

print(type(keys_list))
#type = dict_keys 키만 들어있는 것. list와는 다름



value_list = user.values()

print(value_list)
#value만 나옴
print(type(value_list))
#dict_values
value_list = list(value_list)
print(value_list)
#list 변경 가능


item_list = user.items()
item_list = list(item_list)
#dict_values 에서 list 형태로 변경 가능

print(item_list)
print(type(item_list))


print(item_list[0])
print(type(item_list[0]))
#tuple 타입으로 확인
