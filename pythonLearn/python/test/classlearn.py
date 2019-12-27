
class Student(object):
    def __init__(self, name, age, love):
        self.name = name
        self.age = age
        self.__love = love
    # 数据封装：在类内部定义方法来处理数据
    #与普通函数不同，类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    #实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问
    def getLove(self):
        return self.__love
    def setLove(self,love):
        self.__love = love



qianqian = Student('aqian', 24, 'tianyu') 
print(qianqian.getAge())
print(qianqian.getName())
print(qianqian.getLove())
#print(qianqian.__love)#无法访问————————访问限制



class Tianyu(Student):
    # 当子类和父类都存在相同的getName()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
    #覆盖重写不需要的方法，其它可以直接拿来用
    def getName(self):
        print('创建子类成功')
        return self.name
tian = Tianyu('tianyu', 25, 'qianqian')
print(tian.getName())
print(tian.getAge())
# 可以通过实例变量或者self给实例绑定属性
tian.hign = 170
print(tian.hign)
# 也可以给类本身绑定一个属性，其实例都可以访问该属性

#test：实例自动加1
class Students(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Students.count += 1
print(Students.count)
zhang = Students('zhang')
print('zhang_count', zhang.count)
li = Students('li')
print('li_count:', li.count)
print(Students.count)