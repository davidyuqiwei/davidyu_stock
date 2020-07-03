class C1(object):
    name = "sss"
    def __init__(self,name):
        self.val = 'tt'
        self.name = name
    @classmethod
    def setName(cls,names):
        print('set name')
        print(names)
        cls(names)
        cls.updateName(names)
    @classmethod
    def updateName(cls,names):
        print('update name')
        print(cls.name)
        #cls(names)

aa = C1.setName('aa')



#tmp = aa.clean_colname('aa')
#tmp.shouat
#print(type(tmp))    # 输出 : <class '__main__.C1.C2'>
#tmp.shout()  
