user_data = {"name" : "김성민", 
        "age" : "20", 
        "email" : "sungmin@gmail.com"}
        
# 1 리스트 형태.
# for data in user_data:
#   print(f"{data} : {user_data[data]}")


# 2 튜플로는 인덱스 사용
for data in user_data.items():
  print(f"{data[0]} : {data[1]}")


  