import random

def getRandomElements(k, inputList, probList):
    # Если k равен размеру входного листа, то возвращаем сам входной лист 
    if (k == len(inputList)):
        return inputList
    # Если k больше размера входного листа,
    # то k уменьшаем до размеру входного листа
    elif (k > len(inputList)):
        k = len(inputList)
    elif (k < 0 or isinstance(inputList, list) == False 
                or isinstance(probList, list) == False):
        print("Wrong arguments")
        exit(1)
    
    # Инициализируем modifiedList, где перезапишем все элменеты inputList
    # с учетом вероятности их появления
    # Например, inputList = [1, 2, 3] probList = [.1, .2, .3]
    # то modifiedList = [1, 2, 2, 3, 3, 3]
    modifiedList = list()
    i = 0
    while (i < len(inputList)):
        probability = probList[i] * 10
        tmp = 0
        
        while (tmp < probability):
            modifiedList.append(inputList[i])
            tmp += 1
        i += 1

    # Инициализируем дополнительный булево лист, 
    # размер которого равен размеру modifiedList, где мы будем помечать
    # был ли этот индекс найден ранее или нет
    helperList = [False] * len(modifiedList)
    returnList = [0] * k

    i = 0
    while (i < k):
        # Находим случайный индекс от 0 до len(modifiedList) - 1
        tmp = random.randint(0, len(modifiedList) - 1)
        
        # Если этот индекс не был ранее найден
        # то его отмечаем как уже найденный 
        # и сразу элемент под этим индексом добавляем в наш returnList
        if (helperList[tmp] == False):
            helperList[tmp] = True
            returnList[i] = modifiedList[tmp]
            i += 1
    return returnList

def printList(randomList):
    i = 0
    print("random list -> [", end="")
    while (i < len(randomList)):
        if (i == len(randomList) - 1):
            print(randomList[i], end="")
        else:
            print(randomList[i], end=", ")
        i += 1
    print("]")

if __name__ == '__main__':
    inputList = [1, 3, 4, 3, 3, 9]
    probList = [.1, .3, .4, .3, .3, 1]
    k = 3
    randomList = getRandomElements(k, inputList, probList)
    printList(randomList)
