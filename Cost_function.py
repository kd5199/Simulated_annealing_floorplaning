class module:
    def __init__(self, h: int, w: int, name: None, sub = 0):
        self.height = h
        self.width = w
        self.name = name
        self.submodule = sub 

    def area(self):
        return self.height*self.width

    

class calculators:

    def __init__(self) -> None:
        pass

    def subexpression(m1: module, m2: module, operator: str) -> module:

        return module(max(m1.height, m2.height), m1.width+m2.width, None) if operator == 'V' else module(m1.height + m2.height, max(m1.width, m2.width), None)


class modifier:
    minimized = 0
    initial_updated = []

    def __init__(self) -> None:
        pass

    def subexpressionMinimizer(initial: list) -> module:
        # while len(initial)!=1:
        i = 0
        while len(initial) != 3:
            if(isinstance(initial[i], module) and isinstance(initial[i+1], module) and type(initial[i+2]) == str):
                buff = calculators.subexpression(
                    initial[i], initial[i+1], initial[i+2])
                initial[i] = buff
                initial.pop(i+1)
                initial.pop(i+1)
                # self.minimized+=1
                if(i > 0):
                    i -= 1
            else:
                i += 1

        return calculators.subexpression(initial[0], initial[1], initial[2])


#module_1 = module(1, 2, 1)
#module_2 = module(2, 3, 2)
#module_3 = module(1, 3, 3)
#module_4 = module(3, 4, 4)
#module_5 = module(2, 4, 5)
#module_6 = module(3, 2, 6)
#
#
#initial_tree = [module_1, module_2, 'V', module_3,
#                'H', module_5, module_6, 'V', module_4, 'H', 'V']
#
#
#single_module = modifier.subexpressionMinimizer(initial_tree)
#print(single_module.area())
