# This file takes a bundesliga dataset which has a row for every match of every team for every year
# and converts it to a 1 row per year for each team with home and away win/loss/draw totals

# For data analysis
import pandas as pd
# For randomly generated colours in graph
import random
# For graphs
import matplotlib.pyplot as plt

# initialise a list of years covered by the data.
# this is for the x-axis
years=[]
for i in range(2005,2023):
    years.append(i)

# Bundesliga summary data
df = pd.read_csv('bl_summary.csv')

# Read all teams from the home team column and convert
# to a set to remove duplicates - this creates a list of
# all the teams in the dataset
teamsList = list(set(df["Team"]))
# This will be a list of lists [["Bayern",0,4,3,8 ...].["Bremen",3,2,7..]..]
allTeamsData=[]
teamSummary=[]
print(teamsList)

# Now create a separate df for each team in the bundesliga
for x in teamsList:
    # Isolate data for current team
    allTeamdf=df.loc[df["Team"]==x]
    # read their total wins data
    results=list(allTeamdf["Total Wins"])
    print(x,results)
    if results[-1]==0:
        print(x,"not in current season")
    else:
        # Add the team name and the list of results to my allTeamsData
        allTeamsData.append([x,results])


print(allTeamsData)

plt.figure(figsize=(15,10))
#fig = plt.figure()
#plot = fig.add_subplot(111) # needed for hover etc

#Initialise new list for teams in current season
thisSeasonTeams=[]
# Alternative to random generate code below
#graphColours=["red","lightgreen","yellow","orange","brown","lightcoral","darkolivegreen","cyan","magenta","green","sienna","maroon","skyblue","navy","purple","indigo","grey","limegreen","aquamarine"]
colNum=965793
colIndex=0
for graphingTeam in allTeamsData:
    
    # Generate random colours
    # This code not needed - alternative to list of colours above
    colNum+=random.randint(1048576,15728640)
    colNum%=16777215
    hexCol=hex(colNum)
    if len(hexCol) == 7:
        teamColour=str("#0"+str(hexCol[2:]))
    elif len(hexCol) == 6:
        teamColour=str("#00"+str(hexCol[2:]))
    elif len(hexCol) == 5:
        teamColour=str("#000"+str(hexCol[2:]))
    else:
        teamColour=str("#"+str(hexCol[2:]))
    
    plt.plot(years, graphingTeam[1], color=teamColour,gid=graphingTeam[0])
    # If using graphColours list instead of random above
    #plt.plot(years, graphingTeam[1], color=graphColours[colIndex],gid=graphingTeam[0])

    colIndex+=1
    thisSeasonTeams.append(graphingTeam[0])

    print("graphing",graphingTeam[0],graphingTeam[1])



plt.title("Overview of all teams")
plt.ylabel("number of wins")
plt.xlabel("years")
plt.legend(thisSeasonTeams)

#plt.xlim(1,24)
# must be the lowest value to highest value in all 3 lists
# minus 1 from the min value and add 1 to the max value for pure optics!
#plt.ylim(min(min(day_one_temp),min(day_two_temp),min(day_three_temp))-1,max(max(day_one_temp),max(day_two_temp),max(day_three_temp))+1)

plt.xticks(years)

plt.show()

