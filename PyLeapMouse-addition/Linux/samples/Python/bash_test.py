"""import subprocess
print "start"
#subprocess.call("./screen 2")
subprocess.check_call(['./screen.sh'], shell = True)
print "end" """

import os
os.system("./screen 2")
