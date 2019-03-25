import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


NodeNames = ['Node0', 'Node1', 'Node2', 'Node3']
timeSeries = pd.DataFrame({'Time':np.linspace(0, 2, 5)})
#%%
#Coords of node 0 at different time
NZeroXSeries = pd.Series(np.zeros(5), name='Node0')
NZeroYSeries = pd.Series(np.zeros(5), name='Node0')
#Coords of node 1 at different time
NOneXSeries = pd.Series(np.linspace(1, 1.5, 5), name='Node1')
NOneYSeries = pd.Series(np.linspace(1, 1.5, 5), name='Node1')
#Coords of node 2 at different time
NTwoXSeries = pd.Series(np.linspace(2, 2.5, 5), name='Node2')
NTwoYSeries = pd.Series(np.linspace(2, 2.5, 5), name='Node2')
#Coords of node 3 at different time
NThreeXSeries = pd.Series(np.full(5, 3), name='Node3')
NThreeYSeries = pd.Series(np.full(5, 0), name='Node3')

dictForDF = {'Node0': NZeroXSeries, 'Node2':NOneXSeries, 'Node1':NTwoXSeries, 'Node3':NThreeXSeries}
NodeCoordXTimeDF = pd.DataFrame(dictForDF)
dictForDF = {'Node0': NZeroYSeries, 'Node2':NOneYSeries, 'Node1':NTwoYSeries, 'Node3':NThreeYSeries}
NodeCoordYTimeDF = pd.DataFrame(dictForDF)
#%%
# Sort according to the distance of node at beginning of time
# Get the first row, 
nodeCoordsInitial = NodeCoordXTimeDF.iloc[0]
# Get the indices of the sorted elements in the first row 
sortedNodes = nodeCoordsInitial.argsort()
# Sort the columns of the DataFrame accordingly
sortedColumn = NodeCoordXTimeDF.columns[sortedNodes]
sortedCoordXTimeDF = NodeCoordXTimeDF[sortedColumn]
sortedCoordYTimeDF = NodeCoordYTimeDF[sortedColumn]
#%%
heightDataFrame = pd.DataFrame(index=sortedCoordXTimeDF.index, columns=sortedCoordXTimeDF.columns)
for i in range(sortedCoordXTimeDF.index.size): #sortedCoordXTimeDF.index.size
    # Skip the first row which has the initial coord at time t = 0 sec
    # CAUTION: Don't move this code to any other line
    if i == 0:
        initalCoordAtTimeZero = sortedCoordXTimeDF.iloc[0]
        continue
    
    # Collect the coordinates from time t > 0 sec
    coordX = sortedCoordXTimeDF.iloc[i] # Series
    coordY = sortedCoordYTimeDF.iloc[i] # Series
    # displacement of the nodes with respect to initial coord
    deltaX = coordX - initalCoordAtTimeZero
    # For Nodes with positive Delta X
    XCoordOfNodesWithPosDeltaX = coordX[deltaX > 0] # Series
    YCoordOfNodesWithPosDeltaX = coordY[deltaX > 0] # Series
    # List to hold the indices of the nodes in front or behind the Node currently being tested
    indicesSecondNodesInInterpFunc = []   
    
    # loop via Nodes with positive Delta X
    # Use get_loc to find the indices of nodes behind node of interest 
    for j in range(XCoordOfNodesWithPosDeltaX.index.size):
        # 1. Get the name of the node of interest -- XCoordOfNodesWithPosDeltaX.index[j]
        # 2. Get the index number from sortedColumn Series using the Node Name -- sortedColumn.get_loc(XCoordOfNodesWithPosDeltaX.index[j])
        # 3. Subtract by 1 to get the index number of the nodes behind the node of interest 
        indicesSecondNodesInInterpFunc.append(sortedColumn.get_loc(XCoordOfNodesWithPosDeltaX.index[j]) - 1)
    
    # Use the indices of the nodes behind to get their X, Y coordinates at the current time
    XCoordBehindNodeOfInterest = sortedCoordXTimeDF.iloc[i, indicesSecondNodesInInterpFunc]
    YCoordBehindNodeOfInterest = sortedCoordYTimeDF.iloc[i, indicesSecondNodesInInterpFunc]
    # interpolate those values
    for k in range(XCoordBehindNodeOfInterest.index.size):
        xp = [XCoordBehindNodeOfInterest.iloc[k], XCoordOfNodesWithPosDeltaX.iloc[k]]
        fp = [YCoordBehindNodeOfInterest.iloc[k], YCoordOfNodesWithPosDeltaX.iloc[k]]
    
        interpolatedYCoordPosDelX = np.interp(initalCoordAtTimeZero.loc[XCoordOfNodesWithPosDeltaX.index[k]], xp, fp)
        heightDataFrame.at[i, XCoordOfNodesWithPosDeltaX.index[k]]  = interpolatedYCoordPosDelX
