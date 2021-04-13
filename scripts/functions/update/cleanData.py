class cleanData:
    def __init__(self):
        self.test = ""
    @staticmethod
    def columnToFloat(df,columns):
        import numpy as np
        """
        @param: df: a dataframe
        @param: columns: a list of the colnames that need trans to float
        """
        for col in columns:
            float_list = []
            for xx in df[col].values.tolist():
                try:
                    new_float = np.float(xx.replace(",","").replace("    ","").replace("-",""))
                    #print(new_float)
                    float_list.append(new_float)
                except Exception as e:
                    float_list.append(-999)
                    print(e)
            df[col] = float_list
        return df

