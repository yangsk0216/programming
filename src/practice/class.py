class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_coordinates(self):
        return (self.x, self.y)
    
# 在这个类中，我们定义了一个构造函数 __init__，用于初始化该类的实例，并将属性 x 和 y 赋值为传入的参数。
# 接下来，定义了一个成员方法 move，用于将点在二维平面上移动指定的水平和垂直距离。
# 最后，定义了另一个成员方法 get_coordinates，用于获取该点的坐标信息。
# 定义了这个类后，我们可以使用以下代码创建该类的实例并访问它的属性和方法：
# 实例化 Point 类

p = Point(1, 2)

# 获取该点的坐标
print(p.get_coordinates())

# 将该点向右上角移动 2 个单位长度
p.move(2, 2)

# 获取该点移动后的坐标
print(p.get_coordinates())