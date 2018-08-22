# Part II: Nested loops

# 2. ​The following data shows the number of signatures collected each day of the week -
# by each of five team members working with you on a ballot initiative campaign.
# Your team uses the number “-1” ​to indicate that someone did not work on that day, so
# be careful not to add this number to any totals you may generate.

weeklyReport = [["Monday", [30, 45, -1, 18, 20]],
                ["Tuesday", [12, 40, -1, 19, 34]],
                ["Wednesday", [22, 25, 31, 36, -1]],
                ["Thursday", [-1, 28, 39, 22, -1]],
                ["Friday", [-1, 25, 24, 0, 2]],
                ["Saturday", [38, -1, 73, -1, 50]],
                ["Sunday", [64, -1, 44, -1, 61]]]


# Write a program called weeklyReport.py ​that uses nested loops to find out and report
# (using any language or formatting that makes sense to you):


# ● The total number​ of signatures collected for the week
weeklyTotal = 0
for dailyReport in weeklyReport:
    dailyIndividuals = dailyReport[1]
    dailyTotal = 0
    for individual in dailyIndividuals:
        if individual != -1:
            dailyTotal = dailyTotal + individual
    weeklyTotal = weeklyTotal + dailyTotal
print()
print("Total number of signatures collected this week: " + str(weeklyTotal))


# ● The name of the day ​on which your team collected the most ​signatures
bestDaily = 0
for dailyReport in weeklyReport:
    dailyIndividuals = dailyReport[1]
    day = dailyReport[0]
    dailyTotal = 0
    for individual in dailyIndividuals:
        if individual != -1:
            dailyTotal = dailyTotal + individual
    if dailyTotal > bestDaily:
        bestDaily = dailyTotal
        bestDay = day
print("Our best day was " + str(bestDay) + ", where we collected " + str(bestDaily) + " signatures.")


# ● The name of the day ​on which your team collected the least ​signatures
worstDaily = 0
for dailyReport in weeklyReport:
    dailyIndividuals = dailyReport[1]
    day = dailyReport[0]
    dailyTotal = 0
    for individual in dailyIndividuals:
        if individual != -1:
            dailyTotal = dailyTotal + individual
    if worstDaily == 0:
        worstDaily = dailyTotal
        worstDay = day
    elif worstDaily >0 and dailyTotal < worstDaily:
        worstDaily = dailyTotal
        worstDay = day
print("Our worst day was " + str(worstDay) + ", where we collected " + str(worstDaily) + " signatures.")
