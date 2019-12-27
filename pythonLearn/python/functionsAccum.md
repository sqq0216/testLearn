1. items（）函数，将一个字典以列表的形式返回，因为字典是无序的，所以返回的列表也是无序的。
2. Iteration（）：判断是否可迭代----isinstance('abc', Iterable) # str是否可迭代 from collections import Iterator,此外，isinstance也可以判断一个对象是否是该类型本身
3. 列表生成式：[x * x for x in range(1, 11)]----import os
4. 生成器（generator）：g = (x * x for x in range(10)) 或者通过yield关键字构造generator
    通过next(g)或者for循环来打印元素
5. 迭代器（Iterator）: 使用iter()函数可以把list、dict、str等Iterable变成Iterator
5. .count(元素):计算某个元素在列表中的个数sum.count(num2) == 1
6. .index()：查看某个元素的索引，可以指定搜索范围j = sum.index(num2,i+1)
## 高阶函数
1. map(f, Iterable) :将函数f功能作用于可迭代对象生成一个新的可迭代对象
2. reduce(f, []): reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
3. filter(f, iterable)---筛选函数: 类似map，通过函数判断并筛选iterable
4. sorted():排序函数  sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)——> ['about', 'bob', 'Credit', 'Zoo'](可以传入多个参数作为条件)
5. 返回函数
6. 装饰器（Decorator）：在代码运行期间动态增加功能的方式，不必修改函数定义(@functools.wraps(fn))
7. 偏函数（functools.partial）：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。比如：int2 = functools.partial(int, base=2)