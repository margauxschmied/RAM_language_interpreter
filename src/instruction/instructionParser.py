from src.instruction.instruction import RAM, RawInstruction
from src.instruction.register import Register
from src.interpreter import Interpreter
from src.instruction.instruction import Macro as MacroInstruction


class Instruction:
        def __init__(self, num_instr: int, register: Register, n=None, next=None, is_macro=False):
            self.num_instr = num_instr
            self.register = register
            self.n = n
            self.next = next
            self.is_macro=is_macro



        def setNext(self, next):
            self.next=next

        def list_intruction(self):
            list=[]
            dic={}
            currentInstruction = self
            while currentInstruction != None :
                if currentInstruction.is_macro:
                    dic[currentInstruction.num_instr] = MacroInstruction(currentInstruction.num_instr,
                                                                         currentInstruction.register.list_register(),
                                                                         currentInstruction.instruction.list_intruction())
                else:
                    list.append(RawInstruction(self.num_instr, self.register.list_register(), self.n, is_macro=isinstance(currentInstruction.num_instr, str)))


                currentInstruction = currentInstruction.next
            return list, dic

        def transform_for_interpreter(self):
            return Interpreter(*self.list_intruction(), RAM())