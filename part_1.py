import random

def getRandomElements(k, inputList):
    # Если k равен размеру входного листа, то возвращаем сам входной лист 
    if (k == len(inputList)):
        return inputList
    # Если k больше размера входного листа,
    # то k уменьшаем до размеру входного листа
    elif (k > len(inputList)):
        k = len(inputList)
    elif (k < 0 or isinstance(inputList, list) == False):
        print("Wrong arguments")
        exit(1)
    
    # Инициализируем дополнительный булево лист, 
    # размер которого равен размеру inputList, где мы будем помечать
    # был ли этот индекс найден ранее или нет
    helperList = [False] * len(inputList)
    returnList = [0] * k

    i = 0
    while (i < k):
        # Находим случайный индекс от 0 до len(inputList) - 1
        tmp = random.randint(0, len(inputList) - 1)
        
        # Если этот индекс не был ранее найден
        # то его отмечаем как уже найденный 
        # и сразу элемент под этим индексом добавляем в наш returnList
        if (helperList[tmp] == False):
            helperList[tmp] = True
            returnList[i] = inputList[tmp]
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
    k = 3
    randomList = getRandomElements(k, inputList)
    printList(randomList)
