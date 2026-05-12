class Finger:
    def __init__(self,name):
        self.name=name
    
    def __repr__(self):
        return f"Finger({self.name})"
    
class Hand:
    def __init__(self,side,str):
        self.side=side
        self.fingers=[("thumb"),("index"),("middle"),("ring"),("pinky")]

    def __repr__(self):
        return f"Hand({self.side}, Fingers={self.fingers})"
    
class Foot:
    def __init__(self,side:str):
        self.side= side
        self.toes=[("big toe"),("second toe"),("third toe"),("fourth toe"),("little toe")]

    def __repr__(self):
        return f"Foot({self.side}, Toes={self.toes})"
    
class Eye:
    def __init__(self,side:str):
        self.side=side

    def __repr__(self):
        return f"Eye({self.side})"
    
class Ear:
    def __init__(self,side:str):
        self.side=side
    def __repr__(self):
        return f"Ear({self.side})"
    
class Mouth:
    def __init__(self):
        pass


    def __repr__(self):
        return f"Mouth()"

class Arm:
    def __init__(self,side:str):
        self.side=side
        self.hand=Hand(side,"hand")

    def __repr__(self):
        return f"Arm({self.side}, Hand={self.hand})"
    
class Leg:
    def __init__(self,side:str):
        self.side=side
        self.foot=Foot(side)    

    def __repr__(self):
        return f"Leg({self.side}, Foot={self.foot})"
    
class Head:
    def __init__(self):
        self.eyes=[Eye("left"),Eye("right")]
        self.ears=[Ear("left"),Ear("right")]
        self.mouth=Mouth()

    def __repr__(self):
        return f"Head(Eyes={self.eyes}, Ears={self.ears}, Mouth={self.mouth})"
    
class torso:
    def __init__(self):
        self.arms=[Arm("left"),Arm("right")]
        self.legs=[Leg("left"),Leg("right")]
    def __repr__(self):
        return f"Torso(Arms={self.arms}, Legs={self.legs})"
    
class Human:
      def __init__(self,name:str,age:int):
          self.name=name
          self.age=age
          self.head=Head()
          self.torso=torso()
      def __repr__(self):
        return f"Human({self.name}, {self.age}, Head={self.head}, Torso={self.torso})"
human1=Human("Josue", 25)
print(human1)

