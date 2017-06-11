from pxl_vector import PxlVector

class PxlObject():
    instances = {}

    def __init__(self, id=None, className=None):
        self.id = id
        self.className = className
        self.events = {} 

    def on(self, event, action):
        if event not in self.events:
            self.events[event] = []
            self.events[event].append(action)
            
        else:
            self.events[event].append(action)

    def emit(self, event, data=None):
        if event in self.events:
            for action in self.events[event]:
                action(data=data)
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "PxlObject(size={0}, position={1})".format(self.size, self.position)
