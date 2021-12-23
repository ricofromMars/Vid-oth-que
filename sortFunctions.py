def dateSorting(movieDict):
    dateList = []

    for item in movieDict.values():

        if not dateList:
            dateList.append(item)
        elif item.release >= dateList[-1].release:
            dateList.append(item)
        elif item.release <= dateList[0].release:
            dateList.insert(0, item)
        else:
            i = 0
            while i < len(dateList)-1:
                if (item.release >= dateList[i].release) and (item.release <= dateList[i+1].release):
                    dateList.insert(i+1, item)
                    break
                i += 1

    return dateList

def nameSorting(movieDict):
    nameList = []

    for item in movieDict.values():

        if not nameList:
            nameList.append(item)
        elif item.name >= nameList[-1].name:
            nameList.append(item)
        elif item.name <= nameList[0].name:
            nameList.insert(0, item)
        else:
            i = 0
            while i < len(nameList)-1:
                if (item.name >= nameList[i].name) and (item.name <= nameList[i+1].name):
                    nameList.insert(i+1, item)
                    break
                i += 1

    return nameList

def typeSorting(movieDict, vidType):
    typeList = []

    for item in movieDict.values():

        if item.type == vidType:
            typeList.append(item)

    return typeList