import datetime


def get_the_datetime():
    now_time = datetime.datetime.now()
    now_date = now_time.strftime('%Y_%m_%d')
    now_date_time = now_time.strftime('%Y_%m_%d_%H%M%S')
    return now_date,now_date_time

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



