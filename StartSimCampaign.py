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
SimFoldersTemp = SimDict['PathsSimFolders_rel']

SimFolderList = [SimFoString.split('\\')[-1] for SimFoString in SimFoldersTemp]

# EvalScriptName = "evaluate_results_odb.bat"     #evaluate_results_odb.bat starts getWeldDiameterFromODB.py for extraction of weld diameter
# NameSimFolderTemplate = "SpotWelding2D_Sim_"    #SpotWelding2D_Sim_ is enumerated to SpotWelding2D_Sim_1, SpotWelding2D_Sim_2, etc. is the folder where simulations are executed in
NameSimFolder = ""                              #Enumerated folder
AmplitudesFolder = ""                              

TotalNumberSims = 0 
NumSim = 0                           #as python starts enumeration with 0 a total of TotalNumberSims + 1 simulations will be performed
SimulationList = [] 

UnlockFile = "unlock.py"                        #existence of this file will be checked and execution of next simulation prevented if file does not exist
OptimizationContMark = "OptCont.py"
OptimizationFinishMark = "OptFin.py"






MainFolder = os.getcwd()                        #MainFolder set to the directory in which this script was started


#SimStatusDict = {}

#for Order, SimFolder in enumerate(SimFolderList):
#    
#    SimStatusDict[SimFolder] = {}
#    
#
#    SimStatusDict[SimFolder]['Status'] = 'created'
#    SimStatusDict[SimFolder]['Order'] = Order




#SimFolderList = list(SimStatusDict.keys())
#SimStatusList = [SimStatusDict[SimFolder]['Status'] for SimFolder in SimFolderList]
#SimOrderList = [SimStatusDict[SimFolder]['Order'] for SimFolder in SimFolderList]


#loop through simulations 
for SimNumber, SimFolder in enumerate(SimFolderList):
    
#    NameSimFolder = NameSimFolderTemplate + str(NumSim) #current simulation folder, enumerates the simulation folder to SpotWelding2D_Sim_1, SpotWelding2D_Sim_2 etc.
#    NameSimFolderDBG = NameSimFolderTemplate + str(NumSim+1) #next simulation folder, used for debugging purposes
#    shutil.copytree(NameSimFolderTemplate, NameSimFolder)
    
#    os.chdir(AmplitudesFolder)     #changes working directory to NameSimFolder. Required because otherwise subprocess.Popen() would start "StartCouplingMethod.bat" in the MainFolder
    
    #checks existence of unlock.py and starts simulation if it is found in the current simulation folder, otherwise waits 10 seconds until recheck
    if SimNumber == 0:
        
        outputFileObject = open(SimFolderList[SimNumber]+"/unlock.py", "w")
        
    while os.path.isfile(SimFolder+"/unlock.py") == False:
        time.sleep(10) #Suspends script for 10 seconds
        print("waiting for unlock of: " + SimFolder)
    

    print (CoupledSimProcess)
    
#    shutil.move("Amplitudes/Stromverlauf.txt", SimFolder+"/main")
#    shutil.move("Amplitudes/Kraftverlauf.txt", SimFolder+"/main")
#    os.remove("Amplitudes/unlock.py")
    
    # shutil.copy(CoupledSimProcess, SimFolder)    

    try: 
        os.remove("Amplitudes/EvalFinished.py")
    except:
        pass
    
    os.chdir(SimFolder)
    
    subprocess.Popen([CoupledSimProcess],creationflags=CREATE_NEW_CONSOLE)  #Starts the simulation by executing StartCouplingMethod.bat in the NameSimFolder 
    
    os.chdir(MainFolder) 
    


    
    #checks existence of SimFinishMark.py and starts evaluation if it is found in the current simulation folder, otherwise waits 10 seconds until recheck
    while os.path.isfile(SimFolder+"/SimFinishMark.py") == False:      
        time.sleep(10) #Suspends script for 10 seconds
        print("waiting for simulation to finish: " + SimFolder)
    
    
#    shutil.move(NameSimFolder+"/SimFinishMark.py", "Amplitudes")          
    
#    os.chdir(SimFolder)    
#    subprocess.Popen([EvalScriptName],creationflags=CREATE_NEW_CONSOLE)     #Starts the evaluation by executing evaluate_results_odb.bat in the NameSimFolder 
#    
#    os.chdir(MainFolder)    #changes current working directory to MainFolder
#    os.chdir(NameSimFolderDBG) #changes current working directory to next simulation folder
    
    
#    while os.path.isfile(SimFolder+"/EvalFinished.py") == False:
#        print ("waiting for evaluation of: " +SimFolder)
#        time.sleep(10)
#    shutil.move(SimFolder+"/EvalFinished.py", "Amplitudes")

#    with open(SimFolder+"/weldDiameter.dat", "r") as weldDiamFile:
#        weldDiam = float(weldDiamFile.readline())

#    with open("Amplitudes/weldDiamList.dat", "a") as DiamListFile:
#        DiamListFile.write(str(weldDiam)+"\n") 
    outputFileObject = open(SimFolderList[SimNumber+1]+"/unlock.py", "w") #writes unlock file for next simulation allowing it to proceed
    outputFileObject.close()
    
    
    print (MainFolder)
    
#    if os.path.isfile("Amplitudes/OptCont.py") == True:   
#        NumSim += 1
#        TotalNumberSims +=1
#    else:
#        while os.path.isfile("OptFin.py") == False:
#            print("Simulation Finished")
#            time.sleep(10)
    