

#클래스 활용법
class User : 
  def __init__(self, name, age):
    #__init__ 
    self.name = name
    self.age = age

  def hello(self):
    print(f"hello!! My name is {self.name}")


user_1 = User("김성민", 20)
user_2 = User("김철수", 14)
#유저 추가를 하여 객체 생성.

# user_1.hello()
#    print("hello!!")

print(user_2.name)
print(user_2.age)



