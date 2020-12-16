## calculate the linear regression coef for 
# a single column in a dataframe

# input df: pandas Dataframe
# column_in: the column name that we want to caluate the linear regression
'''
from functions.LinearReg import LinearReg
SH_slope = LinearReg.single_linear_reg(SH_index_df1,'norm_col')[0]
'''
class LinearReg:
    """
    for linear regression
    """
    @classmethod
    def single_linear_reg(self,df,column_in,if_normed=1):
        try:
	        """
	        linear regression for one column
	        x: 0: length(y)
	        y: y 
	        """
	        import pandas as pd
	        from sklearn.linear_model import LinearRegression
	        from sklearn import linear_model
	        import numpy as np
	        X_in1 = pd.DataFrame(df,columns=[column_in])
	        X = pd.DataFrame(X_in1,columns=[column_in]).dropna()
	        # how many rows in the dataframe and make it as x
	        rows=X.shape[0]
	        x = np.array(range(rows)).reshape(-1,1)
	        if if_normed == 1:
	            y = X.values
	            y_normed = (y -y.min(axis=0))/(y.max(axis=0)-y.min(axis=0)+0.001)
	        else:
	            y_normed = X.values
	        # regression
	        regr = linear_model.LinearRegression()
	        regr.fit(x,y_normed)
	        slope = round(regr.coef_.item(),5)
	        inter = round(regr.intercept_.item(),2)
        except:
            slope = -999
            inter = -999
        return slope,inter
if __name__=='__main__':
    import pandas as pd
    from functions.LinearReg import *
    d = {'col1': [1, 2,5], 'col2': [3, 4,2]}
    df = pd.DataFrame(data=d)
    t1 = LinearReg()
    slope, inter = t1.single_linear_reg(df,"col1")
    print("slope "+ str(slope))
    print("intercept "+ str(inter))




