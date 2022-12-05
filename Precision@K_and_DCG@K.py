import numpy as np

search_results = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]

Precision = 0
DCG = search_results[0]
Average_precision = 0
iDCG = 1
relative = 0
time = 1

for i in range(10):
    result = search_results[i]
    if result:
        relative += 1
        Precision = str(relative)+'/'+str(time)
        Average_precision += relative/time
    else:
        Precision = str(relative)+'/'+str(time)
    if i >= 1 and result:
        DCG += 1/(np.log2(time))
    print("Precision@{} = {}, DCG@{} = {:.4f}".format(time, Precision, time, DCG))
    time += 1
print("----------------------------------------------")
Average_precision = Average_precision / relative
print("Average Precision = %.4f" % Average_precision)
print("----------------------------------------------")
if relative:
    for i in range(1, relative):
        iDCG += 1/(np.log2(i+1))
    print("DCG = %.4f" % DCG)
    print("iDCG = %.4f" % iDCG)
    print("nDCG(10) = DCG/iDCG = %.4f" % (DCG/iDCG))
