## calculate the linear regression coef for 
# a single column in a dataframe

# input df: pandas Dataframe
# column_in: the column name that we want to caluate the linear regression
class LinearReg:
    """
    for linear regression
    """
    def single_linear_reg(self,df,column_in):
        import pandas as pd
        from sklearn.linear_model import LinearRegression
        from sklearn import linear_model
        import numpy as np
        X_in1 = pd.DataFrame(df,columns=[column_in])
        X = pd.DataFrame(X_in1,columns=[column_in]).dropna()
        # how many rows in the dataframe and make it as x
        rows=X.shape[0]
        x=np.array(range(rows)).reshape(-1,1)
        y = X.values
        # regression
        regr = linear_model.LinearRegression()
        regr.fit(x,y)
        slope = round(regr.coef_.item(),3)
        inter = round(regr.intercept_.item(),2)
        return slope,inter
if __name__=='__main__':
    import pandas as pd
    d = {'col1': [1, 2,5], 'col2': [3, 4,2]}
    df = pd.DataFrame(data=d)
    t1 = LinearReg()
    slope, inter = t1.single_linear_reg(df,"col1")
    print("slope "+ str(slope))
    print("intercept "+ str(inter))




