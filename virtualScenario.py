#USE THIS FILE TO CREATE NEW SPECIFIC PARAMETER CHANGES using the TEMPLATE (eg. : 000_Input_1Sim_Example_Al-Al_TimInput_)
# SAVES THE NEW PARAMETER DICTIONARY 'p_all_SimRun_list' WITH THE LATEST CHANGES IN PARAMATERS, FILE NAME, RUN ID
# NO INPUT FILE, NO FOLDER CREATED HERE !?
 
import os
import copy
#from ParameterVaryModule import ParamaterVary

#Determine the current work directory
cwd_raw=os.getcwd()


## For FORCE VARIATION CHANGE AT LINE 35

####################################
####################################
# DEFINE or ADD NEW ? INPUT PARAMATERS
####################################

# Define the name of the simulation campaign
name_Sim_Campaign = 'MatDamir_realCt_ShortC_CFStiVary' # Careful: The name should not be too long! --> as the total path may not become too long for windows.



###################################
# Start Script



####################################
# A) Load the baseline parameters
# Define the path of the folder where the python scripts are saved for model definition
part_dir_ScenDef = cwd_raw + "\\A_Virtual_Scenario_Definition\\"
# Load the parameter dictionary containing all model definitions required
# Assign the Parameter dictionary containing all definitions: 
# execfile(part_dir_ScenDef + '000_Input_1Sim_St-St_MatDataDamir_ForceDriven_realContDat_contOp.py')
# execfile(part_dir_simRun + '000_Input_1Sim_Example_Al-Al_Tim.py')
# execfile(part_dir_simRun + '000_Input_1Sim_Example_ShortCircut.py')
# execfile(part_dir_simRun + '000_Input_1Sim_Example_ShortCircut_RefSheet.py')


######################### NOT REQUIRED AS ONLY SHORT CIRCUIT IS BEEN STUDIED ####################################
# Copy the baseline dictionary
# note: as it is a nested dictionary deepcopy is required to be able to make changes to p_all_SimRun_baseline without making changes to p_all_SimRun_example
# p_all_SimRun_baseline = copy.deepcopy(p_all_SimRun_example)    # Note: p_all_SimRun_example is defined in the baseline folder '000_Input_1Sim_Example_St-St_Tim.py'
# created a copy to make changes to the dictionary created from the 
####################################


# REQUIRED -- SHORT CIRCUIT CASE
# Also load the short-circuit case!
execfile(part_dir_ScenDef + '000_Input_1Sim_St-St_ShortCircuit_MatDataDamir_ForceDriven_realContDat_contOp.py')
#########################
# Copy the baseline dictionary
# note: as it is a nested dictionary deepcopy is required to be able to make changes to p_all_SimRun_baseline without making changes to p_all_SimRun_example
p_all_SimRun_baseline_SC = copy.deepcopy(p_all_SimRun_example)    # Note: p_all_SimRun_example is defined in the baseline folder '000_Input_1Sim_Example_St-St_Tim.py'
####################################
######################################################
############ p_all_SimRun_List which will contain different simulation datas of the same p_all_SimRun_baseline_SC: 
p_all_SimRun_list = []



class ParameterVary(object):

    currentList1 = [[0.0, 0.0], [0.001, 0.594394736842105], [0.002, 1.081], 
	[0.003, 1.47126315789474], [0.004, 1.70413157894737], [0.005, 1.89415789473684], 
	[0.006, 2.05942105263158], [0.007, 2.19289473684211], [0.00800000000000001, 2.2861052631579], 
	[0.009, 2.34328947368421], [0.01, 2.38165789473684], [0.011, 2.39915789473684], 
	[0.012, 2.40684210526316], [0.013, 2.40676315789474], [0.014, 2.39934210526316], 
	[0.015, 2.38921052631579], [0.016, 2.3821052631579], [0.017, 2.37389473684211], 
	[0.018, 2.36326315789474], [0.019, 2.34994736842105], [0.02, 2.34294736842105], 
	[0.025, 2.31418421052632], [0.03, 2.30707894736842], [0.035, 2.30573684210526], 
	[0.04, 2.30642105263158], [0.045, 2.31113157894737], [0.05, 2.31210526315789], 
	[0.055, 2.31152631578947], [0.06, 2.31092105263158], [0.065, 2.31094736842105], 
	[0.07, 2.30663157894737], [0.075, 2.30286842105263], [0.08, 2.30486842105263], 
	[0.085, 2.30210526315789], [0.09, 2.30260526315789], [0.0950000000000001, 2.29926315789474], 
	[0.1, 2.29926315789474], [0.102, 0.0], [10.0, 0.0]] 
    currentList2 = [[0.0, 0.0], [0.001, 0.606317543859649], [0.002, 1.09980701754386], 
	[0.003, 1.50107807017544], [0.004, 1.78715263157895], [0.005, 2.00175263157895], 
	[0.006, 2.16089298245614], [0.007, 2.26140789473684], [0.00800000000000001, 2.31727543859649], 
	[0.009, 2.34213947368421], [0.01, 2.35495789473684], [0.011, 2.3622052631579], [0.012, 2.36029210526316], 
	[0.013, 2.35778684210526], [0.014, 2.34588684210526], [0.015, 2.34063859649123], [0.016, 2.33163245614035], 
	[0.017, 2.32832456140351], [0.018, 2.32333596491228], [0.019, 2.3203149122807], [0.02, 2.3174298245614], 
	[0.025, 2.31133333333333], [0.03, 2.30843859649123], [0.035, 2.30951052631579], [0.04, 2.31030701754386], 
	[0.045, 2.31181754385965], [0.05, 2.31756140350877], [0.055, 2.31781228070176], [0.06, 2.31340350877193], 
	[0.065, 2.30777543859649], [0.07, 2.30471228070175], [0.075, 2.30483947368421], [0.08, 2.30239473684211], 
	[0.085, 2.30320526315789], [0.09, 2.29967456140351], [0.0950000000000001, 2.30139824561404], [0.1, 2.30139824561404], 
	[0.102, 0.0], [10.0, 0.0]]
    currentList3 = [[0.0, 0.0], [0.001, 0.607707894736842], [0.002, 1.10280614035088], 
	[0.003, 1.49914122807018], [0.004, 1.78470350877193], [0.005, 1.99733859649123], 
	[0.006, 2.15198596491228], [0.007, 2.25568596491228], [0.00800000000000001, 2.31534912280702], 
	[0.009, 2.34154473684211], [0.01, 2.35204298245614], [0.011, 2.35246929824561], 
	[0.012, 2.36011052631579], [0.013, 2.35629210526316], [0.014, 2.34915964912281], 
	[0.015, 2.34128157894737], [0.016, 2.3346201754386], [0.017, 2.32769385964912], 
	[0.018, 2.32118070175439], [0.019, 2.31901052631579], [0.02, 2.31722192982456], 
	[0.025, 2.31090087719298], [0.03, 2.31039035087719], [0.035, 2.30956666666667], 
	[0.04, 2.30907543859649], [0.045, 2.31880438596491], [0.05, 2.31622807017544], 
	[0.055, 2.31766052631579], [0.06, 2.31255789473684], [0.065, 2.3080201754386], 
	[0.07, 2.30580964912281], [0.075, 2.30035789473684], [0.08, 2.30123684210526], 
	[0.085, 2.30326578947368], [0.09, 2.30196929824561], [0.0950000000000001, 2.29870350877193], 
	[0.1, 2.29870350877193], [0.102, 0.0], [10.0, 0.0]]
    currentNames = []
    time_mech_START_fFIX = 0.005 # in s
    time_mech_START = 0.01
    ForceLow = 1385 # in N
    ForceMid = 1890 # in N
    ForceHigh = 2395 # in N
    forceList1 = [[0.0, -0.01], [time_mech_START_fFIX, -0.01], [time_mech_START, -ForceLow], [(0.37 + time_mech_START), -ForceLow], [(0.41 + time_mech_START), -0.01], [(10 + time_mech_START), -0.01]]
    forceList2 = [[0.0, -0.01], [time_mech_START_fFIX, -0.01], [time_mech_START, -ForceMid], [(0.37 + time_mech_START), -ForceMid], [(0.41 + time_mech_START), -0.01], [(10 + time_mech_START), -0.01]]
    forceList3 = [[0.0, -0.01], [time_mech_START_fFIX, -0.01], [time_mech_START, -ForceHigh], [(0.37 + time_mech_START), -ForceHigh], [(0.41 + time_mech_START), -0.01], [(10 + time_mech_START), -0.01]]
    forceCollectionList = []
    forceListLength = None
    lenOfForceCollList = None
    forceAmpDict = {}
    currentAmpDict = {}


    stiffGunTopList = []
    stiffGunTopListLength = None
    stiffGunBotList = []
    stiffGunBotListLength = None
    stiffCombiList = []
    stiffCombiListLength = None

    combination = {}


    def _init_(self):
        pass

    ################## LIST with Gun Top Stiffness ##########################
    def createStiffListGunTop(self):
        stiffStartVal = 7000
        stiffCurrVal = stiffStartVal
        for i in range(3):
            self.stiffGunTopList.append(stiffCurrVal)
            stiffCurrVal = stiffCurrVal + 1000
        self.stiffGunTopListLength = len(self.stiffGunTopList)


    ################## LIST with Gun Bottom Stiffness ######################
    def createStiffListGunBot(self):
        stiffStartVal = 8000
        stiffCurrVal = stiffStartVal
        for i in range(3):
            self.stiffGunBotList.append(stiffCurrVal)
            stiffCurrVal = stiffCurrVal + 1000
        self.stiffGunBotListLength = len(self.stiffGunBotList)


    ############## LIST with combination of Gun Stiffness ##################
    def createStiffList(self):
        self.createStiffListGunTop()
        self.createStiffListGunBot()

        for i in range(self.stiffGunTopListLength):
            for j in range(self.stiffGunBotListLength):
                topStiffVal = self.stiffGunTopList[i]
                botStiffVal = self.stiffGunBotList[j]
                self.stiffCombiList.append([topStiffVal, botStiffVal])
        self.stiffCombiListLength = len(self.stiffCombiList)
        #print(self.stiffCombiList)


    ############## LIST of Gun Top Force Values ############################
    def createForceList(self):
		self.forceCollectionList = [self.forceList1, self.forceList2, self.forceList3]
		self.lenOfForceCollList = len(self.forceCollectionList)
		print(self.forceCollectionList)
        


    ############ Dict of Gun Top Force Amplitudes ###########################
    def createForceAmp(self):
        self.createForceList()
        for i in range(self.lenOfForceCollList):
            DictKeyVal =  str(i)
            self.forceAmpDict[DictKeyVal] = self.forceCollectionList[i]
        print(self.forceAmpDict)
		
    def createCurrentList(self):
		self.currentCollectionList = [self.currentList1, self.currentList2, self.currentList3]
		self.currentNames = ['LowC', 'MidC', 'HigC']
		self.lenOfCurrentCollList = len(self.currentCollectionList)
		
    def createCurrentAmp(self):
		self.createCurrentList()
		for i in range(self.lenOfCurrentCollList):
			ampDictKeyVal = str(i)
			self.currentAmpDict[ampDictKeyVal] = self.currentCollectionList[i]
			
	
	############ Combination of Stiff & Force #############################
    def createCombination(self):

        self.createStiffList()
        self.createForceAmp()
        self.createCurrentAmp()
        
        combiKeyVal = 0

        for i in range(self.lenOfForceCollList):

            for j in range(self.stiffCombiListLength):

                forceAmpDictKeyVal = str(i)
                forceAmplitude = self.forceAmpDict[forceAmpDictKeyVal]
				
                currentAmpDictKeyVal = str(i)
                currentAmplitude = self.currentAmpDict[currentAmpDictKeyVal]
				
                stiffVal = self.stiffCombiList[j]
                self.combination[str(combiKeyVal)] = [forceAmplitude, currentAmplitude, stiffVal]
                combiKeyVal = combiKeyVal + 1


    def getCombination(self):
        self.createCombination()
        return self.combination

		
		
		

		
a = ParameterVary()
combiDict = a.getCombination()
noOfCombi = len(combiDict)

for i in range(noOfCombi):
    
	p_all_SimRun_temp = copy.deepcopy(p_all_SimRun_baseline_SC)
	
	combiList = combiDict[str(i)]
	
	forceAmp = combiList[0]
	p_all_SimRun_temp['processPar']['ForceAmplitude_move_closing'] = forceAmp
	
	currentAmp = combiList[1]
	p_all_SimRun_temp['processPar']['CurrentAmplitude'] = currentAmp
		
	gunCombiStiffVal = combiList[2]
	gunTopStiffVal = gunCombiStiffVal[0]
	gunBotStiffVal = gunCombiStiffVal[1]
	p_all_SimRun_temp['weldMachine']['gun_top']['spring_stiffness'] = gunTopStiffVal
	p_all_SimRun_temp['weldMachine']['gun_bot']['spring_stiffness'] = gunBotStiffVal



	# ADD p_all_SimRun_List with ALL THE SIMULATION VARIATION #####################################
	forceLastElement = forceAmp[2]
	forceVal = forceLastElement[1]
	
	p_all_SimRun_temp['SimulationMetaData']['name_sim_campaign'] = name_Sim_Campaign 
	# Modify the ID of the simulation run
	# Sim_ID = len(p_all_SimRun_list) + 1
	p_all_SimRun_temp['SimulationMetaData']['simRun_ID'] =  i
	# creates a folder named 'RSW_2Dax_StSt_ShortCirc_Barun' + '_' + str(Sim_ID)
	p_all_SimRun_temp['FEMethod']['JobName_root'] = 'Sim_ID' + str(i) + '_' + 'F' + str(forceVal) + '_' + 'StifGT'+ str(gunTopStiffVal) + 'StifGB' + str(gunBotStiffVal)
	#p_all_SimRun_temp['FEMethod']['JobName_root'] = 'RSW_2Dax_StSt_ShortCirc' + '_' + str(i)
	p_all_SimRun_list.append(p_all_SimRun_temp)
		
		

#####################################################################################################################	
