class main_computer:
    def __init__(self,cpu,ram):
        self.cpu =cpu
        self.ram=ram

    def configuration(self):
        print("the configuration is",self.cpu,self.ram)
computer1 = main_computer("i5 cpu","8gb RAM")
computer2 =main_computer("AMD3 cpu","4gb RAM")


computer1.configuration()

