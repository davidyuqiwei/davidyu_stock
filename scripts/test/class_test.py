class C1(object):
    def __init__(self):
        self.val = 'tt'
        self.name = 'sss'
    def clean_colname(self,names):
        self.name = names
    @staticmethod
    class C2(object):
        def __init__(self, C1):
            self.parent = C1
        def shout(self):
            print("Python世界第%d!%s"%self.C1.name1)

aa=C1()
tmp = aa.clean_colname('aa').C2()
tmp.shout
#print(type(tmp))    # 输出 : <class '__main__.C1.C2'>
#tmp.shout()  
