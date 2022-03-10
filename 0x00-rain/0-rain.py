def rain(walls):
    rainTotal = 0
    basinTotal = 0
    tempHigh = 0
    start = 0
    runningShortWallsTotal = 0
    
    for i in range(1, len(walls)):
        if walls[i] >= walls[start]:
            runningShortWallsTotal += walls[tempHigh]
            basinTotal = (min(walls[start], walls[i]) * ((i - start) - 1)) - runningShortWallsTotal
            rainTotal += basinTotal
            start = i
            tempHigh = 0
        elif i == len(walls) - 1 and walls[tempHigh] != 0:
            basinTotal = (min(walls[start], walls[tempHigh]) * ((tempHigh - start) - 1)) - runningShortWallsTotal
            rainTotal += basinTotal
        elif tempHigh == 0:
            tempHigh = i
        elif walls[i] >= walls[tempHigh]:
            runningShortWallsTotal += walls[tempHigh]
            tempHigh = i
    return rainTotal
