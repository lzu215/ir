import numpy as np

search_results = [1, 1, 1, 1, 1,
                  1, 0, 0, 1, 1,
                  1, 1, 0, 1, 1,
                  0, 1, 0, 1, 1]  # 输入20个0，1数据（随便输，不需要真的去查找了）

Precision = 0
DCG = search_results[0]
Average_precision = 0
IDCG = 1
NDCG = 0
relative = 0
time = 1

for i in range(20):
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
print("Average Precision = MAP = %.4f" % Average_precision)
print("----------------------------------------------")
if relative:
    for i in range(1, relative):
        IDCG += 1/(np.log2(i+1))
    print("DCG = %.4f" % DCG)
    print("IDCG = %.4f" % IDCG)
    print("NDCG(20) = DCG/IDCG = %.4f" % (DCG/IDCG))
