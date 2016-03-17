import mmap

with open("hello.txt", "wb") as f:
    f.write( "THING" )

with open("hello.txt", "r+b") as f:
    
    mm = mmap.mmap(f.fileno(), 0)
    
    print mm.readline()
    
    mm.close()

