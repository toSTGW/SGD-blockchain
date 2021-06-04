ub = open("../user.bat", "w")
at = open("../account.txt", "r")

line = at.readline()
while line:
    strs = line.split(',')
    ub.write("start /b py ballot5.py %s %s %s" % (strs[0], strs[1], strs[2]))
    line = at.readline()

ub.close()
at.close()


