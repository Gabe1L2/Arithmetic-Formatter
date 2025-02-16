def getTime(timeString):
    colonIndex = timeString.find(":")
    spaceIndex = timeString.find(" ")
    hour = int(timeString[:colonIndex])
    suffix = timeString[spaceIndex+1:]

    # If there's no space (like in the duration time)
    if spaceIndex == -1:
        minute = int(timeString[colonIndex+1:])
    else:
        minute = int(timeString[colonIndex+1:spaceIndex])

    # convert to 24 hour time
    if hour >= 1 and hour <= 11 and suffix == 'PM':
        hour += 12
    if hour == 12 and suffix == 'AM':
        hour = 0

    return [hour, minute]

def numAddition(start, duration, max):
    totalNum = start + duration
    # if the number goes past 60 minutes or 24 hours
    if totalNum >= max:
        newCarry = totalNum // max
        newNum = totalNum % max
    else: 
        newCarry = 0
        newNum = totalNum

    return [newCarry, newNum] # returns how many extra to carry and the final number of hours/minutes

def add_time(start, duration, startDate = "None"):
    # both lists [hour, minute]
    startTime = getTime(start)
    durationTime = getTime(duration)

#    print(startTime)
#    print(durationTime)

    # Returns [Extra hours, minutes]
    finalMinutes = numAddition(startTime[1], durationTime[1], 60)
    # Returns [Extra days, hours]
    finalHours = numAddition(startTime[0], durationTime[0] + finalMinutes[0], 24)

    # get AM or PM
    if finalHours[1] <= 11:
        suffix = "AM"
    else:
        suffix = "PM"

    # Change back to 12-hour time
    if finalHours[1] == 0:
        hour = 12
    elif finalHours[1] <= 12:
        hour = finalHours[1]
    else:
        hour = finalHours[1] - 12

    # format minute
    if finalMinutes[1] < 10:
        minute = f"0{finalMinutes[1]}"
    else:
        minute = finalMinutes[1]
        
    # checks if any days passed
    daysLater = ""
    if finalHours[0] == 1:
        daysLater = " (next day)"
    elif finalHours[0] > 1:
        daysLater = f" ({finalHours[0]} days later)"

    # Check if there's days of the week
    dayOfWeek = ""
    if startDate != "None":
        startDate = startDate.lower()
        weekList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        lowercaseList = []
        for day in weekList:
            lowercaseList.append(day.lower())
        # check against standardized lowercase list
        startIndex = lowercaseList.index(startDate)
        newIndex = startIndex + finalHours[0]
        if newIndex > 6:
            finalIndex = newIndex % 7
        else:
            finalIndex = newIndex
        dayOfWeek = f", {weekList[finalIndex]}"

    return(f"{hour}:{minute} {suffix}{dayOfWeek}{daysLater}")

print(add_time('2:59 AM', '24:00', 'saturDay'))