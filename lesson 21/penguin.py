class bird:
    def __init__(self):
        print("Bird is ready")
    def whoisthis(self):
        print("Bird")
    def run(self):
        print("Run faster!")
class penguin(bird):
    def __init__(self):
        print("Penguin is ready")
        super().__init__()
    def whoisthis(self):
        super().whoisthis()
        print("Penguin")
    def swim(self):
        print("Swim faster!")
obj=penguin()
obj.whoisthis()
obj.run()
obj.swim()