class Asker :
    @staticmethod
    def askall(lst) :
        for i in lst :
            i.report()
        return

class Sender :
    counter = 0
    def report(self) :
        if Sender.counter == 0 :
            print("Greetings!")
        else :
            print("Get away!")
        Sender.counter += 1


a, b, c = Sender(), Sender(), Sender()
Asker.askall((a,b,c, a, b, c, a, a, a, a, a, a))
