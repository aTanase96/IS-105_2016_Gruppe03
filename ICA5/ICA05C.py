import timeit, functools

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




testresultsFast = []
testresultsSlow = []
numberOfLoops = 5

def timeTests(numberOfLoops):
    for i in range(numberOfLoops):
        
        t = timeit.Timer(functools.partial(search_fast, list, "Martin")) 
        fastResult = (t.timeit(10))
        testresultsFast.append(fastResult)
        
        t = timeit.Timer(functools.partial(search_slow, list, "Martin")) 
        slowResult = (t.timeit(10)) 
        testresultsSlow.append(i)
   
timeTests(numberOfLoops)
        
for i in range(len(testresultsFast)):
    print(testresultsFast[i])




a = 2141251.51255123
print("%.4f" % a)

print(testresultsFast[0])