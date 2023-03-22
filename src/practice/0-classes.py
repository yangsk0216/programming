# import agentframework
# a = agentframework.Agent()

# class Agent():
#     def __init__(self):
#         self.x = 0
#         self.y = 0
        
# a = Agent()
# a.x = 3 # <-- Sets the values of a.x to be 3
# a.y = a.y + 1 # <-- Increases the value of a.y by 1
        
# print(a.x) # <-- Prints the value of a.x
# print(a.y) # <-- Prints the value of a.y

        
class Agent():
    def __init__(self, ax, ay):
        self._x = ax
        self._y = ay

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
    
a = Agent(0, 0)
a.x = 3
print(a.x) # <-- Prints 3
 
    





       