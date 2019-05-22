## calculate the linear regression coef for 
# a single column in a dataframe

# input df: pandas Dataframe
# column_in: the column name that we want to caluate the linear regression
def single_linear_reg(df,column_in):
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn import linear_model
    import numpy as np
    X_in1=pd.DataFrame(df,columns=[column_in])
    X=pd.DataFrame(X_in1,columns=[column_in]).dropna()
    # how many rows in the dataframe and make it as x
    rows=X.shape[0]
    x=np.array(range(rows)).reshape(-1,1)
    y = X.values
    # regression
    regr = linear_model.LinearRegression()
    regr.fit(x,y)
    fit1=round(regr.coef_.item(),3)
    return fit1
