class StringProcess:
    @staticmethod
    def transformLatin2GB2312(x):
        """
        transform latin1 to gb2312
        :param x:
        :return:
        """
        x1 = x.encode('latin1', "ignore").decode('gb2312', "ignore")
        return x1

