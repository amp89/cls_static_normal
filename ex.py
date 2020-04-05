class ThingDoer:
    
    stuff = "HI"
    
    def __init__(self,name_of_thing=None):
        self.name_of_thing = name_of_thing if name_of_thing else "Whatever"
    
    @classmethod
    def do_a_thing(cls):
        print(f"I'm doing a thing {cls.stuff}")
        
    @classmethod
    def get_a_thing(cls, name_of_thing):
        return cls(name_of_thing)
        
    @staticmethod
    def do_something():
        print(f"I'm doing something")
        
    def do_the_thing(self):
        print(f"I'm doing {self.name_of_thing}")
        
ThingDoer.do_a_thing() # prints I'm doing a thing HI
ThingDoer.do_something() # ThingDoer.do_something()
td = ThingDoer.get_a_thing("stuff")
td.do_the_thing() # I'm doing stuff
