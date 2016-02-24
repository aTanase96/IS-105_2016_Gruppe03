"""

A short program to evaluate execution times of algoritmhs

Written by Martin Venaas 23.feb.2016


"""


import timeit, functools

# List to search
list = ["Martin", "Tor Ole", "Per-otto", "Tomas", "Andrei"]

def search_fast(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
    return False

def search_slow(haystack, needle):
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value


"""
t = timeit.Timer(functools.partial(search_fast, list, "Martin")) 
print(t.timeit(1000000))

t = timeit.Timer(functools.partial(search_slow, list, "Martin")) 
print(t.timeit(1000000))
"""


# numberOfLoops is the amounts of times you want to run timeTests 

numberOfLoops = 5

testresultsFast = []
testresultsSlow = []

def timeTests(numberOfLoops):
    for i in range(numberOfLoops):
        
        t = timeit.Timer(functools.partial(search_fast, list, "Martin")) 
        fastResult = (t.timeit(1000000))
        testresultsFast.append(i)
        
        
        t = timeit.Timer(functools.partial(search_slow, list, "Martin")) 
        slowResult = (t.timeit(1000000)) 
        testresultsSlow.append(i)
        
        


        