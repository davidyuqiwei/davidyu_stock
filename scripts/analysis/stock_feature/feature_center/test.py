for loop_i in range(0,3):
    f2 = open('model_out.txt','a')
    model_score = 0.725
    print(model_score)
    f2.write('\nmodel'+str(loop_i)+'\t'+str(model_score))

