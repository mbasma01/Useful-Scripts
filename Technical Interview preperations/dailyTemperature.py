temps = [30,38,30,36,35,40,28]
def dailyTemp(temps):
    res = [0]*len(temps)

    for i in range(len(temps) - 1):
        for j in range(i+1, len(temps)):

            if temps[j] > temps[i]:
                res[i] += 1
                print(i, temps[i], j, temps[j])
                break
            elif j == len(temps) - 1:
                res[i] = 0
                break
            else:
                res[i] += 1
    return res
print(dailyTemp(temps))

