def MovingAverage(arr, num):
    ret = []
    N = len(arr)
    partialSum = 0
    for i in range(1, num - 1):
        partialSum += arr[i]
    for i in range(num, N):
        partialSum += arr[i]
        ret.append(partialSum / num)
        partialSum -= arr[i - num + 1]
    return ret