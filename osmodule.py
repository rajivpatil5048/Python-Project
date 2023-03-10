# OS Module:=
#=========== use of OS module is provides a portable way of using operating system dependant functionality.
#            Use utility provided by os

# Methods in OS Module:=
#=====================

# 1] To know current working directory:=
# -------------------------------------
import os
print(os.getcwd())

# 2] To change working directory:=
# -------------------------------
import os
os.chdir(directory path)
print(os.getcwd())

# 3] To create directory (single directory):=
# -------------------------------------------
import os
os.mkdir(dir name)

# 4] How to delete directory:=
# ----------------------------
import os
os.rmdir(dir name)

# 5] How to make multiple dir:=
# ----------------------------

import os
os.makedirs(dir name)

# 6] How to transfer all data in list:=
#-------------------------------------
import os
data=os.listdir(".")
print(data)


# 7] Executing python file from other python file:=
# ------------------------------------------------

import os
os.chdir(dir path)
os.system(filename)


