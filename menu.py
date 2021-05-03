# --------------------------------------------------------------
#  
#  Pietro Abati
#  Version: 1.0.0
#  Last Updated: 2021 - 05 - 03 
# --------------------------------------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import platform

# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:\Users\Pietro\.nuke'
MacOSX_Dir = '/Users/Pietro/.nuke'
Linux_Dir = '/home/Pietro/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None
