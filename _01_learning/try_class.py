class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print('%s正在学习%s.' % (self.name,course_name))

    def watch_movie(self):
        if self.age<18:
            print('%s只能快乐熊宝' % self.name)
        else:
            print('%s可以玩亚索了' % self.name)

def main():
    stu1 =Student('小李',28)
    stu1.study('化学')
    stu1.watch_movie()

    stu2 = Student('小王',15)
    stu2.study('生物')
    stu2.watch_movie()

if __name__ == "__main__":
    main()


    #我们通常会将对象的属性设置为私有的（private）或受保护的（protected），简单的说就是不允许外界访问，而对象的方法通常都是公开的（public），因为公开的方法就是对象能够接受的消息
    #在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
'''
class Test:

    def __init__(self,foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print('test.__foo')

if __name__ == '__main__':
    main()
'''
    #Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，事实上如果你知道更换名字的规则仍然可以访问到它们
    #大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重

class Test1:

    def __init__(self,foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test1 = Test1('baby')
    test1._Test1__bar()
    print(test1._Test1__foo)

if __name__ == '__main__':
    main()

'''
#定义一个类描述数字时钟

from time import sleep

class Clock(object):

    def __init__(self,hour=0,minute=0,second=0):

        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):

        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' %(self._hour,self._minute,self._second)

def main():
    clcok = Clock(23,59,58)
    while True:
        print(clcok.show())
        sleep(1)
        clcok.run()

if __name__ == '__main__':
    main()
'''

#定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

from math import sqrt

class Point(object):

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def move_to(self,x,y):
        self.x = x
        self.y = y

    def move_by(self,dx,dy):
        self.x += dx
        self.y += dy

    def distance_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return ('%s,%s') % (str(self.x),str(self.y))

def main():
    point1 = Point(3,5)
    point2 = Point()
    print(point1)
    print(point2)
    point1.move_by(-1,3)
    print(point1)
    print(point2.distance_to(point1))


if __name__ == '__main__':
    main()











