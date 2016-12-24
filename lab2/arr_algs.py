arr1=[3,7,5,9,2]

def minInArray(arrToCalculate):
    if len(arrToCalculate) !=0 :
        min1=arrToCalculate[0]
    else:
        return 'Err'
    for n in arrToCalculate:
        if min1>= n:
            min1=n
    return min1

def AverageInArray(arrToCalculate):
    if len(arrToCalculate) !=0 :
        sumOfElements = 0
    else:
        return 'Err'
    for n in arrToCalculate:
        sumOfElements+=n
    return sumOfElements/len(arrToCalculate)

minArr1 = minInArray(arr1)
print('минимальный элемент в массиве [3,7,5,9,2] :',minArr1)
AverageArr1 = AverageInArray(arr1)
print('средний элемент в массиве [3,7,5,9,2] :',AverageArr1)
print('минимальный элемент пустого массива : ',minInArray([]))
print('средний элемент пустого массива : ',AverageInArray([0]))
