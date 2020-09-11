def Sort_Tuple(tup):
    return(sorted(tup, key = lambda x: x[1]))
tup = [('Raja',39,30),('Rani',29,20),('Babu',28,11),('Gopiji',20,20)]
print(Sort_Tuple(tup))

import operator
mytuple  = [('Raja',39,30),('Rani',29,29),('Babu',28,11),('Gopiji',20,20)]
mytuple.sort(key = operator.itemgetter(0,0))
print(mytuple)


[('Babu', 28, 11), ('Gopiji', 20, 20), ('Raja', 39, 30), ('Rani', 29, 29)]
mytuple.sort(key = operator.itemgetter(1,1))
print(mytuple)
mytuple.sort(key = operator.itemgetter(2,2))
print(mytuple)