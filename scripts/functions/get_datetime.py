import datetime


def get_the_datetime():
    now_time = datetime.datetime.now()
    now_date = now_time.strftime('%Y-%m-%d')
    now_date_time = now_time.strftime('%Y-%m-%d-%H%M%S')
    return now_date,now_date_time

def getEveryDay(begin_date='2019-06-01',end_date='2019-12-31'):
    """指定开始时间和结束时间，获取中间的日期"""
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    print('共生成了%s天' % str(len(date_list)))
    #print(date_list)
    return date_list

if __name__ == "__main__":
    getEveryDay("2019-01-02","2019-01-10")

#now_date,now_date_time = 

'''
   def strftime(self, fmt):
               "Format using strftime()."
                       return _wrap_strftime(self, fmt, self.timetuple())



    @classmethod
    def now(cls, tz=None):
        "Construct a datetime from time.time() and optional time zone info."
        t = _time.time()
        return cls.fromtimestamp(t, tz)


 def date(self):
         "Return the date part."
                 return date(self._year, self._month, self._day)

datetime.datetime.now().date()

'''



