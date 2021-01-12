class Paddle(object):
    def __init__(self,length,height,width,color,position,opacity):
        self.length = length
        self.height = height
        self.width = width
        self.color = color
        self.position = position
        self.opacity = opacity

    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
paddle1 = Paddle(10,14,20,"Red",15,20)
paddle1color=paddle1.getColor()     
print(paddle1color)    
paddle1.setColor('green')
print(paddle1.color)