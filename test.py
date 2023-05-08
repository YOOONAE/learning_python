#----------------------- 1. Parameter 없는 클래스, 간단한 메소드 3개
from random import randint

class MyFirstClass:
    # the convention for naming methods is to use lowercase letters and underscores
    # to separate words in the method name. 
    # This convention is known as snake_case.
    # the parentheses are required in the method definition
    def first_method(self):
        print("my first_method working")
        return 1+2+3+4+5

    # method: associated with an object(an instance of a class) or a class
    # function: a standalone block of code that can be called by name and may or may not return a value
    def second_method(self):
        print("my second method working")
        return 5/2*4+3

    # When you call a method on an instance of a class, Python automatically passes in the instance 
    # as the first argument, which is why self is often called the "instance parameter". 
    # This allows the method to access and modify the instance's attributes, 
    # and to interact with other methods and attributes of the instance.
    def third_method(self):
        print("my third method working")
        return None

# print('###### MyFirstClass - result ######')
# when creating an instance of a class, use (). Also, starting with uppercase is a convention
my_object_1 = MyFirstClass()
# print('==> return value (first_method):', my_object_1.first_method())
# print('==> return value (second):', my_object_1.second_method())
# print('==> return value (third_method):', my_object_1.third_method())

#----------------------- 2. Parameter 존재하는 클래스, 메소드도 Parameter 받고, init 안에 Parameter 받기

class MySecondClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calculate_sum(self):
        return self.x + self.y
    
    def calculate_random_between(self):
        #use randint() method of Random class as a function by importing it directly from there
        rand = randint(self.x, self.y)
        return rand
    
    def calculate_multiplying_sum_by_z(self, z):
        result =  self.calculate_sum() * z
        return result

# print('###### MySecondClass - result ######')
# my_object_2 = MySecondClass(2,6)
# print('==> return value (sum):', my_object_2.calculate_sum())
# print('==> return value (rand between integer):', my_object_2.calculate_random_between())
# print('==> return value (multiply sum by z value):', my_object_2.calculate_multiplying_sum_by_z(4))

#----------------------- 3. MySecond 클래스와 같은데, try except 예외처리 포함하기, int가 아닌 string을 넣으면 value error가 나도록

class MyThirdClass:
    def __init__(self, x, y):
        try:
            self.x = int(x)
            self.y = int(y)
            self.value_error = False
        except:
            print('** Value Error : Please input valid integer values')
            self.value_error = True
        
    def calculate_sum(self):
        if(self.value_error):
            return 'Not a valid input in MyThirdClass'
        return self.x + self.y
    
    def calculate_random_between(self):
        if(self.value_error):
            return 'Not a valid input in MyThirdClass'
        #use randint() method of Random class as a function by importing it directly from there
        rand = randint(self.x, self.y)
        return rand
    
    def calculate_multiplying_sum_by_z(self, z):
        if(self.value_error):
            return 'Not a valid input in MyThirdClass'
        result =  self.calculate_sum() * z
        return result

# print('###### MyThirdClass - result ######')
# my_object_3 = MyThirdClass(y='aa',x='bb')
# print('==> return value (sum):', my_object_3.calculate_sum())
# print('==> return value (rand between integer):', my_object_3.calculate_random_between())
# print('==> return value (multiply sum by z value):', my_object_3.calculate_multiplying_sum_by_z(4))


#----------------------- 4. Python Default API - lower() method 를 inherit, 클래스안에 메소드 3개, init에 param 넣어서 super로 inherit
#                           lower() 메소드 활용해서 모든 space 없애서 합쳐주는.. 한단어로 나오는.. 거 만들기?


# "STRING".lower() => Python creates something like an instance automatically under the hood and returns lowercased string.
# If I override the lower() method, I can add more functionalities I want which means I can change the return value

# varable = MyFourthClass("STRING") ===>  variable.lower() ==>>> will return something different, if I override the builtin method.
# the builtin str class with an argument like str("STRING") will return "STRING" itself by default.
# Inherits str class which is the built-in class by default in Python
class MyFourthClass(str):
    def __init__(self, text):
        self.text = text

    # override the builtin lower() method
    def my_custom_lower(self):
        # inherit the original lower()'s return value..? which is from the built-in str class
        init_txt = super().lower()

        # space removal function added to my_custom_lower() method that inherits lower() builtin method from str class 
        nospace_txt = ""
        for c in init_txt:
            if c != " ":
                nospace_txt = nospace_txt + c

        return nospace_txt

    def my_custom_camelcase(self):
        custom_txt = ""
        for c in range(0, len(self.text)):
            if c % 2 == 0:
                custom_txt = custom_txt + self.text[c].swapcase()
            else:
                custom_txt = custom_txt + self.text[c]

        return custom_txt

    def my_custom_space_added(self):
        custom_txt = ""

        for c in self.text:
            custom_txt += c + "   "

        return custom_txt


# obj = MyFourthClass('HELLO WORLD!!')

# print('[ 1 ] : ', obj)
# print('[ 2 ] : ', obj.my_custom_lower())
# print('[ 3 ] : ', obj.my_custom_camelcase())
# print('[ 4 ] : ', obj.my_custom_space_added())



#----------------------- 5. 5. 리스트, 리스트 컴프리헨션 / 딕셔너리, 딕셔너리 컴프리헨션 요거 이해. 여거 활용해서 네번째 클래스를 다섯번째 클래스로 만들어라


class MyFifthClass():
    def __init__(self, text):
        self.text = text

    # lower() + space removal
    def my_custom_lower(self):
        txt = [c.lower() for c in self.text if c != " "]
        nospace_txt = ''.join(txt)
        return nospace_txt

    def my_custom_camelcase(self):
        # expression_1 if (condition) else expression_2, for loop with if (condition)
        # if yes -> expression_1, if else -> expression_2, for loop if yes
        txt = [self.text[i].swapcase() if i % 2 == 0 else self.text[i] for i in range(0, len(self.text))]
        custom_txt = ''.join(txt)
        return custom_txt

    def my_custom_space_added(self):
        txt = [c + "   " for c in self.text]
        custom_txt = ''.join(txt)

        return custom_txt


obj = MyFifthClass('HELLO WORLD!!')

print('[ 1 ] : ', obj)
print('[ 2 ] : ', obj.my_custom_lower())
print('[ 3 ] : ', obj.my_custom_camelcase())
print('[ 4 ] : ', obj.my_custom_space_added())

# ------------------------------


"""

**** 3번부터 키워드 아규먼트, 아규먼트(포지셔널 아규먼트) 받을 수 잇는 이닛 메소드 만들기

이거 말이 잘 이해가 안됐어요 ㅠㅠ 클래스안에 

    def __init__(self, *args, **kwargs)
        self.args = args
        self.kwargs = kwargs

위에처럼 받아서, 위에 arguments들 활용해서 str클래스 상속받은 메소드를 만드는게 맞나요?


"""