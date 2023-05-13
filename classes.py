
    
# a = A()
# a.say_hi(input('Type your name: '))
# # Չի կարելի սենց անել
# # a.setting = 'Setting'
# # a.setting1 = 'Settings1'
# print(a.setting)

# with open('script.txt', 'r+') as f:
#     f.write('01234')

class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 20
    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')
    # def get_age(self):
    #     return self.__age
    # def set_age(self, value):
    #     if value in range(1, 101):
    #         self.__age = value
    #     else:
    #         print('Error')

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def set_age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Error')