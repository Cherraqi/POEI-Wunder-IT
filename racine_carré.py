#!/usr/bin/python
# POEI-Wunder-IT
# -*- coding: utf-8 -*-
#created by Cherraqi 2019

def Heron_Algo_sqrt(NB,NB_iter):#NB est le nombre à calculer
    a=1                    #NB_iter c est le nombre d iteration necessaire pour avoir la bonne precision
    b=2                    #la méthode de Héron ou méthode babylonienne est un cas particulier de la méthode de Newton
    for i in range(NB_iter):
        b=(a+b)/2
        a=NB/b
    return round(a,3)

"""
test :
Heron_Algo_sqrt(2,10)
1.414


"""
"""
def Heron_Algo_sqrt(NB,NB_iter):#NB est le nombre à calculer
    a=1                    #NB_iter c est le nombre d iteration necessaire pour avoir la bonne precision
    b=2                    #la méthode de Héron ou méthode babylonienne est un cas particulier de la méthode de Newton
    for i in range(NB_iter):
        b=(a+b)/2
        a=NB/b
        print(a)
test:       
Heron_Algo_sqrt(2,10)

1.3333333333333333
1.411764705882353
1.41421143847487
1.4142135623715002
1.4142135623730951
1.4142135623730951
1.4142135623730951
1.4142135623730951
1.4142135623730951
1.4142135623730951

1.414
"""
