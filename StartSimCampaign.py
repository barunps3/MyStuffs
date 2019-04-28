# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:43:15 2018

@author: skd1si
"""
"""
    Script runs simulations and evaluates them.

    1. Script checks whether an unlock file (unlock.py) has been written by some other script or program.
    Existence of the  unlock file indicates that the previous simulation has already been evaluated and the parameters "Stromverlauf.txt" and "Kraftverlauf.txt" 
    were set by the external script or program.
    
    2. The simulations are started by by the line "subprocess.Popen([CoupledSimProcess],creationflags=CREATE_NEW_CONSOLE)" which executes "StartCouplingMethod.bat"
    in the current simulation folder
    
    3. When the simulation is finished it writes the file SimFinishMark.py which indicates that the resultsfile <SpotWelding2D_Sim_xx.odb> is complete and ready for evaluation
    
    4. Evaluation is started by "subprocess.Popen([EvalScriptName],creationflags=CREATE_NEW_CONSOLE)" which executes "evaluate_results_odb.bat".
    when finished the scripts creates the file "weldDiameter.dat" in the current simulation folder. This file contains only contains the weld diameter in the unit mm.
    
    Remark: evaluate_results_odb.bat starts the python script getWeldDiameterFromODB.py. 
    In addition to the weld diameter it also writes the time series for all nodes in the interface of both sheets. 
    "nodalDisplacementData.dat" contains a nested list of displacement data
    "nodalTemperatureData.dat" contains a nested list of temperature data
    This data can be retrieved using pickle.load("path_to_file"), pickle module is required.
    
    
"""
#Modules
import time
import numpy as np
import copy
import pickle as pickle
import os
import subprocess
import shutil
import json
from subprocess import Popen, CREATE_NEW_CONSOLE



#############################################
# INPUT:
jsonFilePath = 'VirtualScenario.json'
# Some examples: 
#############################################


#############################################
# START SCRIPT:

# Now load the VirtualScenario.json
with open(jsonFilePath) as json_data:
  SimDict = json.load(json_data)
# END with

# Assign the internal variables required in this script:
CoupledSimProcess = SimDict['Name_batFile_execute_SimRun']   # name defined in the baseline folder to run the simulations
SimFoldersTemp = SimDict['PathsSimFolders_rel']
SimFolderList = [SimFoString.split('\\')[-1] for SimFoString in SimFoldersTemp]

#MainFolder set to the directory in which this script was started
MainFolder = os.getcwd()                        

#loop through simulations 
#for SimChar in enumerate(SimFolderList):
def ParallelSim(SimChar):
    SimNumber = SimChar[0]
    SimFolder = SimChar[1]
    #checks existence of unlock.py and starts simulation if it is found in the current simulation folder, otherwise waits 10 seconds until recheck
    if SimNumber == 0:
        # write the unlock file for first simulation to start simcampaign
        outputFileObject = open(SimFolderList[SimNumber]+"/unlock.py", "w")
        
    while os.path.isfile(SimFolder+"/unlock.py") == False:
        time.sleep(10) #Suspends script for 10 seconds
        print("waiting for unlock of: " + SimFolder)
    

    #print(CoupledSimProcess)    
    os.chdir(SimFolder)
    #Starts the simulation by executing StartCouplingMethod.bat in the NameSimFolder
    subprocess.Popen(CoupledSimProcess, creationflags=CREATE_NEW_CONSOLE) #  
    #subprocess.Popen("cmd")    
    os.chdir(MainFolder) 
    
    #checks existence of SimFinishMark.py and starts evaluation if it is found in the current simulation folder, otherwise waits 10 seconds until recheck
    """
    while os.path.isfile(SimFolder+"/SimFinishMark.py") == False:      
        time.sleep(10) #Suspends script for 10 seconds
        print("waiting for simulation to finish: " + SimFolder)
    """
    #writes unlock file for next simulation allowing it to proceed
    outputFileObject = open(SimFolderList[SimNumber+1]+"/unlock.py", "w") 
    outputFileObject.close()    
    #print (MainFolder)



import multiprocessing as mp
if __name__ == '__main__':
    pool = mp.Pool(int(mp.cpu_count()/2))
    simNumFolderTupleList = [val for val in enumerate(SimFolderList)]
    pool.map_async(ParallelSim, simNumFolderTupleList)
    pool.close()
    pool.join()
