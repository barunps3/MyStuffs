def getTliqCoordEx(set_name_assembly, T_liq, Results_Dict_mech, DOF):


    CoordKey = 'COORD' + str(DOF)

    # Dataframe containing the node set time series is collected
    ResDF_Temp = getArrayfromSetDict(Results_Dict_mech, set_name_assembly, 'NT11', 'N')
    ResDF_Coord = getArrayfromSetDict(Results_Dict_mech, set_name_assembly, CoordKey, 'N')
    
    # Collect the column names (Node names)
    KeyList = list(ResDF_Temp.keys())
    
    MaxValDict = {}
    
    # iterate via each key in KeyList and
    # Take out the maximum value in the time for EACH node and 
    # Add to MaxValDict with key name as the Node names
    for Key in KeyList:
        
        MaxValDict[Key] = ResDF_Temp[Key].max()
    
    # Convert the dictionary with key and max. value into a list of tuple pairs and 
    # sorts the tuple pairs based on max.value in ascending order
    sorted_MaxVals = sorted(MaxValDict.items(), key=operator.itemgetter(1))

    
    try:
        # assign index key to each tuple pair in the sorted list and
        # iterate through each tuple(index, (node name, max. val)) in list
        for Pos, NT_Tuple in enumerate(sorted_MaxVals):
            # if max value is greater than liquid temp then
            if NT_Tuple[1] >= T_liq:
                # collect the index values (Pos) of these Tuple pairs
                Pos_aboveLiq = Pos
                # subtract the index by 1 and collect the subtracted value as Position of 
                # tuple as below liquid temp.
                Pos_belowLiq = Pos - 1
                break
        
        # collect the last assigned node name of the max. val greater than T-liq 
        Node_aboveLiq = sorted_MaxVals[Pos_aboveLiq][0]
        # collect the last assigned node name for Pos_belowLiq
        Node_belowLiq = sorted_MaxVals[Pos_belowLiq][0]
        
        # collect the corresponding temperatures
        NT_aboveLiq = sorted_MaxVals[Pos_aboveLiq][1]
        NT_belowLiq = sorted_MaxVals[Pos_belowLiq][1]

        # Access the columns with the node names and 
        # collect the last row COORD value for the corresponding node name
        Coord_aboveLiq = ResDF_Coord[Node_aboveLiq].iloc[-1]
        Coord_belowLiq = ResDF_Coord[Node_belowLiq].iloc[-1]

        # pair the two temperatures and COORDs
        xp = [NT_belowLiq, NT_aboveLiq]
        fp = [Coord_belowLiq, Coord_aboveLiq]

        # Calculate the interpolated fp value between the two temperatures at liquid temperature
        Coordinate_Tliq = np.interp(T_liq, xp, fp)        
        # Gives the Coordinate
        Weld_Rad_Coord = Coordinate_Tliq

    except:

        Weld_Rad_Coord = 0.0

    # print(Weld_Rad)

    return Weld_Rad_Coord



def getTliqCoordTS(set_name_assembly, T_Liq, Results_Dict_mech, DOF):


    CoordKey = 'COORD' + str(DOF)


    ResDF_Temp = getArrayfromSetDict(Results_Dict_mech, set_name_assembly, 'NT11', 'N')
    ResDF_Coord = getArrayfromSetDict(Results_Dict_mech, set_name_assembly, CoordKey, 'N')
    ResDF_Time = getArrayfromSetDict(Results_Dict_mech, set_name_assembly, 'TIME', 'N')

    # Collect all the node names 
    KeyList = list(ResDF_Temp.keys())

    MaxValDict = {}
    InitialCoordsDict = {}
    
    # iterate via each node names and
    # collect the initial COORD values
    # collect maximum temperature value in the whole time series for each node names 
    for Key in KeyList:
        InitialCoordsDict[Key] = ResDF_Coord[Key].iloc[0]
        MaxValDict[Key] = ResDF_Temp[Key].max()

    # Convert the dictionary with Key and Initial COORD into a list of tuple pairs and 
    # sorts the tuple pairs based on Initial COORD values in ascending order
    sorted_Coords = sorted(InitialCoordsDict.items(), key=operator.itemgetter(1))

    # Create a list of sorted node name [node1, node2, node3]
    CoordSorted_NodeList = [Entry[0] for Entry in sorted_Coords]
    
    # Get the number of rows of Temperature DataFrame
    ShapeTpl = ResDF_Temp.shape
    lenDF = ShapeTpl[0]

    CoordList_belowLiq = []
    CoordList_aboveLiq = []
    
    TemperatureList_belowLiq = []
    TemperatureList_aboveLiq = []

    MoltenMaterial_Rad_List = []
    TimeList = []

    
    for Index in range(lenDF):
        # Assign 'Index' row as DataFrame 
        TempPerFrame_DF = ResDF_Temp.loc[[Index]]
        CoordPerFrame_DF = ResDF_Coord.loc[[Index]]
        TimePerFrame_DF = ResDF_Time.loc[[Index]]
        
        # loop over [(0, node1), (1, node2), ..] 
        for IdentIndex, NodeIdent in enumerate(CoordSorted_NodeList):
            # If temperature value at the give node name and Index is less than or equal to T_Liq
            if TempPerFrame_DF[NodeIdent].iloc[0] <= T_Liq:
                #  and if :
                if IdentIndex == 0:
                    # assign the Coord variables as = 0.0
                    Coord_belowLiq = 0.0
                    Coord_aboveLiq = 0.0
                    # collect the temperatures for given node name
                    Temperature_belowLiq = TempPerFrame_DF[NodeIdent].iloc[0]
                    Temperature_aboveLiq = TempPerFrame_DF[NodeIdent].iloc[0]
                    TimeActual = TimePerFrame_DF[NodeIdent].iloc[0]

                else:
                    # assign the node name 
                    Node_belowLiq = NodeIdent
                    # collect the node name at index value 'IdentIndex-1' from list CoordSorted_NodeList
                    Node_aboveLiq = CoordSorted_NodeList[IdentIndex-1]
                    # collect the COORDs for both node names
                    Coord_belowLiq = CoordPerFrame_DF[Node_belowLiq].iloc[0]
                    Coord_aboveLiq = CoordPerFrame_DF[Node_aboveLiq].iloc[0]
                    # collect the respective temperatures for both node names 
                    Temperature_belowLiq = TempPerFrame_DF[Node_belowLiq].iloc[0]
                    Temperature_aboveLiq = TempPerFrame_DF[Node_aboveLiq].iloc[0]
                    # assign the current time value for node name - NodeIdent 
                    TimeActual = TimePerFrame_DF[NodeIdent].iloc[0]
                    
                # Append the Coord_belowLiq to the list CoordList_belowLiq
                # UpperNodeIdentList.append(copy.copy(Node_belowLiq))
                CoordList_belowLiq.append(copy.copy(Coord_belowLiq))
                # Append the CoordList_aboveLiq to the list Coord_aboveLiq
                CoordList_aboveLiq.append(copy.copy(Coord_aboveLiq))
                # Append the temperatures to their respective temperature lists
                TemperatureList_belowLiq.append(copy.copy(Temperature_belowLiq))
                TemperatureList_aboveLiq.append(copy.copy(Temperature_aboveLiq))
                # Append the time to Time List
                TimeList.append(copy.copy(TimeActual))
                # break the for loop completely
                break
        
        xp = [Temperature_belowLiq, Temperature_aboveLiq]
        fp = [Coord_belowLiq, Coord_aboveLiq]


        Coordinate_Tliq = np.interp(T_Liq, xp, fp)
        Weld_Rad = Coordinate_Tliq

        MoltenMaterial_Rad_List.append(copy.copy(Weld_Rad))


    return(MoltenMaterial_Rad_List, TimeList)
