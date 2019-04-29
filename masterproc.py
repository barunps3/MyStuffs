import time
import numpy as np  
import copy
import glob
import re
from collections import Counter
import operator
import json
#import pandas as pd
import os
import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE



#############################################
# INPUT:

#############################################
# Get the path list!
# Read the json file with the data on the simulation scenario#

# Now load both json Files with the joined data: 
jsonFilePath_virtScen = 'VirtualScenario.json'
with open(jsonFilePath_virtScen) as json_data:
  VirtualScenario = json.load(json_data)
# END with


# Now create the setLists required forExtraction: 
# A the Paths of the simulation folders to be extracted is: 
PathList = VirtualScenario['PathsSimFolders_rel']

# Initialize the other parameter list: 
ExtractNsetNameList_allSim = []  # --> List of node sets to be extracted
ExtractEsetNameList_allSim = []  # --> List of element sets to be extracted
# Also define the respective fields to be extracted
MechFieldListN_allSim = []
MechFieldListE_allSim = []
# 2) For the thermal-electrical odbs
# Also define the respective fields to be extracted
ElekFieldListN_allSim = []
ElekFieldListE_allSim = []


bool_execute_D3_OperateOnData = 0  # Bool specifying whether the file data operation shall be executed in the for loop (0 --> no, 1 --> yes)


#Determine the current work directory (= the folder from which this script has been executed)
cwd_raw=os.getcwd()



# Now cycle through the path list to create lists for 
for path_Sim in PathList:
	# now create the respective sets for Extraction:
	# a) read the respective data from json:
	jsonFilePath_SimRun = cwd_raw + path_Sim + '\Model_Input_Parameters.json'
	with open(jsonFilePath_SimRun) as json_data:
	  Model_Input_Parameters = json.load(json_data)
	 # END with
	  
	exec(open('D0_create_setList_forExtraction.py').read())
	
	# Now save the list in the global list.
	ExtractNsetNameList_allSim.append(ExtractNsetNameList_SimRun)
	ExtractEsetNameList_allSim.append(ExtractEsetNameList_SimRun)
	MechFieldListN_allSim.append(MechFieldListN_SimRun)
	MechFieldListE_allSim.append(MechFieldListE_SimRun)
	ElekFieldListN_allSim.append(ElekFieldListN_SimRun)
	ElekFieldListE_allSim.append(ElekFieldListE_SimRun)
	
# END for


#############################################
# Now save the data required for post-Processing to json file: 
# This data will later be loaded to the automated "for-loop" performing the data extraction ('D1_Extraction_Loop_PostProcessing.py')
Input_D1_Extraction_Loop = {}
Input_D1_Extraction_Loop['ExtractNsetNameList_allSim'] = ExtractNsetNameList_allSim
Input_D1_Extraction_Loop['ExtractEsetNameList_allSim'] = ExtractEsetNameList_allSim
Input_D1_Extraction_Loop['MechFieldListN_allSim'] = MechFieldListN_allSim
Input_D1_Extraction_Loop['MechFieldListE_allSim'] = MechFieldListE_allSim
Input_D1_Extraction_Loop['ElekFieldListN_allSim'] = ElekFieldListN_allSim
Input_D1_Extraction_Loop['ElekFieldListE_allSim'] = ElekFieldListE_allSim
Input_D1_Extraction_Loop['PathList'] = PathList
Input_D1_Extraction_Loop['bool_execute_D3_OperateOnData'] = bool_execute_D3_OperateOnData



#############################################
# Save in file. 
JsonObj = json.dumps(Input_D1_Extraction_Loop)
name_jason_file = cwd_raw + '\\Input_D1_Extraction_Loop.json'
ExtractFile = open(name_jason_file, 'w')
ExtractFile.write(JsonObj)
ExtractFile.close()
#############################################



#############################################
# Extract the specified set & field data
#############################################
# Now execute the function "D1_Extraction_Loop_PostProc.py" using the corresponding batch file!
subprocess.Popen(['D1_Extraction_Loop_PostProcessing.bat'],creationflags=CREATE_NEW_CONSOLE)
# OUTPUT:
# - a dictionary containing all required data for the mechanical odbs (read from MECH_JOINED for finished simulations or MECH_Restarts for unfinished simulations)
# - a dictionary containing all required data for the thermal-electrical odbs
## Note: The result is a json file with the following names: 
#'ELEK_JOINED_Results.json'
#'MECH_JOINED_Results.json'
#############################################

# NOTE Definition of Break Points in Python: "#%%"
# 

#############################################
# FURTHER REMARKS:
# - ...
#############################################



#############################################
#############################################
# Operate on the data
# - ...
#############################################



# FEHLER




