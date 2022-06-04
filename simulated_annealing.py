
from random import randint
from movement import Movement
from Cost_function import module, modifier
import math
import numpy as np
from vis_updated import *


def SAF(initial_tree, initial_temparature, cooling_rate, beta, maxtime, m):
    good_tree = initial_tree
    t = initial_temparature
    time = 0

    while (time <= maxtime):
        good_tree = metropolis(good_tree, t, m)
        time = time+m
        t = cooling_rate*t
        m = beta*m

    # for i in good_tree:
        # if isinstance(i, module):
        # print(i.name, end=' ')
        # else:
        # print(i, end=' ')
    # print('\n')
    # print(modifier.subexpressionMinimizer(good_tree.copy()).area())
    # functions = funcs()
    # functions.drawFinal(good_tree)

    return good_tree


def metropolis(tree, t, m):
    # print(tree)
    while (m != 0):

        i = randint(0, 2)

        switcher = {
            0: Movement.M1,
            1: Movement.M2,
            2: Movement.M3
        }

        new_tree = switcher.get(i)(tree)
        # print(new_tree)

        new_area = modifier.subexpressionMinimizer(new_tree.copy()).area()
        old_area = modifier.subexpressionMinimizer(tree.copy()).area()

        # print(single_module.area())
        del_h = new_area-old_area

        if(del_h < 0) or (np.random.uniform(0, 1) < math.pow(math.e, (-del_h/t))):
            tree = new_tree
            m = m-1
    return tree


module_1 = module(1, 2, 1)
module_2 = module(2, 3, 2)
module_3 = module(1, 3, 3)
module_4 = module(3, 4, 4)
module_5 = module(2, 4, 5)
module_6 = module(3, 2, 6)

initial_tree = [module_1, module_2, module_3, 'V',
                'H', module_5, module_6, 'V', module_4, 'H', 'V']

tree_dict = {}
best_tree = []
for i in range(20):
    good_tree = SAF(initial_tree=initial_tree,
                    cooling_rate=0.1,
                    initial_temparature=4,
                    beta=0.01,
                    maxtime=200,
                    m=1000)

    best_tree = good_tree
    if(modifier.subexpressionMinimizer(
            good_tree.copy()).area()) < modifier.subexpressionMinimizer(
            best_tree.copy()).area():
        best_tree = good_tree

    for item in good_tree:
        if isinstance(item, module):
            print(item.name, end=' ')
            # good_tree_simplified.append(item.name)
        else:
            # good_tree_simplified.append(tree)
            print(item, end=' ')
    print("  :  "+str(modifier.subexpressionMinimizer(good_tree.copy()).area()))
    print('\n')
    
    # tree_dict[str(good_tree)] = modifier.subexpressionMinimizer(
        # good_tree.copy()).area()
# print(tree_dict)
#functions = funcs()
#functions.drawFinal(best_tree)

# print(tree_dict)
