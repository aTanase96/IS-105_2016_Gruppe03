import timeit, functools # Imports the library that helps timing the tests

list = ["Martin", "Tor Ole", "Per-otto", "Tomas", "Andrei"] # The list which we will iterate through 


def search_fast(haystack, needle): # Defines the SearchFast method
    for item in haystack:
        if item == needle:
            return True
    return False

def search_slow(haystack, needle): # Defines the SearchSlow method
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value


testresultsFast = [] # Creates an Array which we can store our test results in
testresultsSlow = []


numberOfTests = 10 # The number of times the timeTests (loop) should run
numberOfCycles = 10000 # Search through the list for the keyword this amount of times. Not to be confused with numberOfTests


def timeTests(numberOfTests): 
    for i in range(numberOfTests): # We tell that the loop should run as many times as specified in the numberOfLoops variable
        
        t = timeit.Timer(functools.partial(search_fast, list, "Martin")) 
        fastResult = (t.timeit(numberOfCycles)) # Search through the list this amount of times to find "Martin"
        testresultsFast.append(fastResult)
        
        t = timeit.Timer(functools.partial(search_slow, list, "Martin")) 
        slowResult = (t.timeit(numberOfCycles)) 
        testresultsSlow.append(slowResult)
   
timeTests(numberOfTests) # Saves the time the system used to iterate through the list to find the keyword "Martin"


formatedFastList = map(lambda n: "%.4f" % n, testresultsFast) # Formats testresultsFast to round up the decimal to 4 diggits
formatedSlowList = map(lambda n: "%.4f" % n, testresultsSlow) # Formats testresultsSlow to round up the decimal to 4 diggits
    

print "FastList, times in seconds", formatedFastList # Return the fast list, formated and ready
print "SlowList, times in seconds", formatedSlowList # Return the slow list, formated and ready


print ""
print ""
print "Press enter to close program"
raw_input() # Closes the program  