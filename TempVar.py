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
            # If any value is less than or equal to T_Liq
            if TempPerFrame_DF[NodeIdent].iloc[0] <= T_Liq:
                #  and if :
                if IdentIndex == 0:

                    Coord_belowLiq = 0.0
                    Coord_aboveLiq = 0.0
                    
                    Temperature_belowLiq = TempPerFrame_DF[NodeIdent].iloc[0]
                    Temperature_aboveLiq = TempPerFrame_DF[NodeIdent].iloc[0]
                    TimeActual = TimePerFrame_DF[NodeIdent].iloc[0]

                else:

                    Node_belowLiq = NodeIdent
                    Node_aboveLiq = CoordSorted_NodeList[IdentIndex-1]

                    Coord_belowLiq = CoordPerFrame_DF[Node_belowLiq].iloc[0]
                    Coord_aboveLiq = CoordPerFrame_DF[Node_aboveLiq].iloc[0]

                    Temperature_belowLiq = TempPerFrame_DF[Node_belowLiq].iloc[0]
                    Temperature_aboveLiq = TempPerFrame_DF[Node_aboveLiq].iloc[0]

                    TimeActual = TimePerFrame_DF[NodeIdent].iloc[0]

    #            UpperNodeIdentList.append(copy.copy(Node_belowLiq))
                CoordList_belowLiq.append(copy.copy(Coord_belowLiq))
                CoordList_aboveLiq.append(copy.copy(Coord_aboveLiq))

                TemperatureList_belowLiq.append(copy.copy(Temperature_belowLiq))
                TemperatureList_aboveLiq.append(copy.copy(Temperature_aboveLiq))

                TimeList.append(copy.copy(TimeActual))

                break

        xp = [Temperature_belowLiq, Temperature_aboveLiq]
        fp = [Coord_belowLiq, Coord_aboveLiq]


        Coordinate_Tliq = np.interp(T_Liq, xp, fp)
        Weld_Rad = Coordinate_Tliq

        MoltenMaterial_Rad_List.append(copy.copy(Weld_Rad))


    return(MoltenMaterial_Rad_List, TimeList)
