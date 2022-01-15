class Register():
    def __init__(self, register, next=None):
        self.register = register
        self.next = next

    def goodNumberOfRegister(self, register):
        currentRegister=self
        while currentRegister!=None and register!=None:
            currentRegister=currentRegister.next
            register= register.next

        if currentRegister==None and register==None:
            return True
        return False

    def registerIsContain(self, registerName):
        for name in registerName:
            if not self.inRegister(name):
                return False
        return True

    def inRegister(self, name):
        currentRegister = self
        while currentRegister != None:
            if currentRegister.register==name:
                return True
            currentRegister = currentRegister.next

        return False