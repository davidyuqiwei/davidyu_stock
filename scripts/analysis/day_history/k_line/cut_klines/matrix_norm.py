def matrix_norm():
    group.tolist()
    minVals = group.min(0)  # 为0时：求每列的最小值[0 3 1]   .shape=(3,)
    maxVals = group.max(0)  # 为0时：求每列的最大值[2 7 8]   .shape=(3,)
    ranges = maxVals - minVals
    
    m = group.shape[0]
    normDataSet = np.zeros(np.shape(group))       #  np.shape(group) 返回一个和group一样大小的数组，但元素都为0
    diffnormData =group - np.tile(minVals,(m,1))  #  (oldValue-min)  减去最小值
    normDataSet1 =diffnormData / np.tile(ranges,(m,1))
