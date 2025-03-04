# https://blog.csdn.net/hanguofei/article/details/90718604
# Python大球吃小球

from enum import Enum, unique
from math import sqrt
from random import randint

import pygame

# @unique
class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class Ball(object):
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)

def main():
    balls = []                                      # 定义用来装所有球的容器
    pygame.init()                                   # 使用 pygame 某些功能(比如 音频、文字)必须的操作
    screen = pygame.display.set_mode((800, 600))    # 初始化用于显示的窗口并设置窗口尺寸
    pygame.display.set_caption('大球吃小球')         # 设置当前窗口的标题
    
    running = True
    while running:                                  # 开启一个事件循环处理发生的事件
        for event in pygame.event.get():            # 从消息队列中获取事件并对事件进行处理
            if event.type == pygame.QUIT:
                running = False
                
            # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表容器中
                balls.append(ball)
        
        screen.fill((255, 255, 255))
        
        # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        
        pygame.display.flip()
        
        # 每隔50毫秒就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    main()
