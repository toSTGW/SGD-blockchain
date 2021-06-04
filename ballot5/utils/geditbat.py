ub = open("../guser.bat", "w")

for i in range(15):
    ub.write("start /b py gballot6.py %d\n" % (i + 1))

ub.close()


