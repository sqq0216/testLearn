class Screen(object):
    # slots:限制可以绑定的属性。实例只能绑定以下两个属性
    #__slots__ = ('wid', 'hei')
    #通过set get方法对属性进行检查，但是实例访问不便（需要调用这两个方法才可以），通过装饰器property将getter方法变成属性，实例可以直接访问和设置width
    @property
    #相当于get
    def width(self):
        return self._width

    @width.setter
    #相当于set，这里可以加入检查
    def width(self, value):
        if 0 < value < 1025:
            self._width = value
        print("请输入0-50内的数字")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0 or value > 800:
            print("请输入0-100内的数字")
        self._height = value

    @property
    def resolution(self):
        return self._height*self._width

if __name__ == "__main__":
    # screen1 = Screen()
    # screen1.wid = 153
    # screen1.hei = 46
    # print(screen1.wid)
    # print(screen1.hei)
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')

