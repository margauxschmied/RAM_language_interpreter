class Register():
    def __init__(self, register, next=None):
        self.register = register
        self.next = next

    def good_number_of_register(self, register):
        currentRegister=self
        while currentRegister!=None and register!=None:
            currentRegister=currentRegister.next
            register= register.next

        if currentRegister==None and register==None:
            return True
        return False

    def register_is_contain(self, registerName):
        for name in registerName:
            if not self.in_register(name):
                return False
        return True

    def in_register(self, name):
        currentRegister = self
        while currentRegister != None:
            if currentRegister.register==name:
                return True
            currentRegister = currentRegister.next

        return False

    def list_register(self):
        list = []
        currentRegister = self
        while currentRegister != None:
            list.append(currentRegister.register)
            currentRegister = currentRegister.next

        return list

    def list_register_str(self):
        list = []
        currentRegister = self
        while currentRegister != None:
            list.append(str(currentRegister.register))
            currentRegister = currentRegister.next

        return list

    def __str__(self) -> str:
        return str(self.register)