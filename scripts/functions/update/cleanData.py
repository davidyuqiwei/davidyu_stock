class cleanData:
    def __init__(self):
        self.test = ""
    @staticmethod
    def columnToFloat(df,columns):
        """
        @param: df: a dataframe
        @param: columns: a list of the colnames that need trans to float
        """
        for col in columns:
            try:
                df[col] = df[col].apply(lambda x:x.replace(",","").replace("    ","")).astype(float)
            except:
                pass
        return df

