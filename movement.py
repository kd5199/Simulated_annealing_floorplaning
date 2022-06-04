from audioop import tostereo
from mimetypes import init
import random
from Cost_function import calculators, module, modifier


class Movement:
    def __init__(self) -> None:
        pass

    def M1(initial: list):
        adjacent_operand = []

        for i in range(len(initial)):
            if(isinstance(initial[i], module) and isinstance(initial[i+1], module)):
                adjacent_operand.append((i, i+1))
                pass
            elif (isinstance(initial[i], module) and not isinstance(initial[i+1], module)):
                for j in range(len(initial)-i):

                    if(isinstance(initial[i+j], module)) and j != 0:
                        adjacent_operand.append((i, i+j))
                        break
        if(len(adjacent_operand)>0):                    
            to_swap = adjacent_operand[random.randint(0, len(adjacent_operand)-1)]
            initial[to_swap[0]], initial[to_swap[1]
                                         ] = initial[to_swap[1]], initial[to_swap[0]]
        return initial

    def M2(initial: list):
        chain = []

        for i in range(len(initial)):
            if(isinstance(initial[i], str)):
                chain.append(i)
        if(len(chain)>0):
            to_invert = chain[random.randint(0, (len(chain)-1))]
            if(initial[to_invert] == 'H'):
                initial[to_invert] = 'V'
            elif(initial[to_invert] == 'V'):
                initial[to_invert] = 'H'
        return initial

    def M3(initial: list):

        adjacent_operator_operand = []
        operand=0
        operator = 0
        for i in range(len(initial)-1):
            # Count operand and operator no.

            if(isinstance(initial[i], module)):
                operand+=1
            else:
                operator+=1    

            # Save index if balloting property holds
            if( operand-2>operator and  isinstance(initial[i], module) and isinstance(initial[i+1], str)):
                adjacent_operator_operand.append((i, i+1))
                pass
            
        if(len(adjacent_operator_operand)>0):
            to_swap = adjacent_operator_operand[random.randint(0, (len(adjacent_operator_operand)-1))]
            initial[to_swap[0]], initial[to_swap[1]] = initial[to_swap[1]], initial[to_swap[0]]
        #print(adjacent_operator_operand)
        return initial


#module_1 = module(1, 2, 1)
#module_2 = module(2, 3, 2)
#module_3 = module(1, 3, 3)
#module_4 = module(3, 4, 4)
#module_5 = module(2, 4, 5)
#module_6 = module(3, 2, 6)
#
##m = Movement()
##print([module_1, module_2, 'V', module_3, 'H',module_5, module_6, 'V', module_4, 'H', 'V'])
#mlist = [module_1, module_2, 'V', module_3, 'H',module_5, module_6, 'V', module_4, 'H', 'V']
#
##print(Movement.M1(mlist))