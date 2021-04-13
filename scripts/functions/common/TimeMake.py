import datetime


class timeFunc():
    '''
    @start_date: 起始日期
    @stat_days: 历史统计日期
    @pred_days: 预测日期
    输入起始日期,历史统计日期,预测日期
    返回: 统计结束日期
    预测起始日期
    预测结束日期
    '''

    def __init__(self, start_date, stat_days, pred_days):
        self.start_date = start_date
        self.stat_days = stat_days
        self.pred_days = pred_days

    def make_date(self):
        stat_end_date = datetime.datetime.strptime(self.start_date, '%Y-%m-%d') + \
                        datetime.timedelta(days=self.stat_days)
        stat_end_date = stat_end_date.strftime("%Y-%m-%d")
        pred_start_date = datetime.datetime.strptime(stat_end_date, '%Y-%m-%d') + \
                          datetime.timedelta(days=1)
        pred_start_date = pred_start_date.strftime("%Y-%m-%d")
        pred_end_date = datetime.datetime.strptime(stat_end_date, '%Y-%m-%d') + \
                        datetime.timedelta(days=self.pred_days)
        pred_end_date = pred_end_date.strftime("%Y-%m-%d")
        return stat_end_date, pred_start_date, pred_end_date

    @staticmethod
    def get_the_datetime():
        now_time = datetime.datetime.now()
        now_date = now_time.strftime('%Y-%m-%d')
        now_date_time = now_time.strftime('%Y-%m-%d-%H%M%S')
        now_month = datetime.datetime(now_time.year, now_time.month,1).strftime('%Y-%m-%d')
        return now_date, now_date_time

    @staticmethod
    def daysAgo(start_date='2099-01-01',days=1):
        print("the start date is: "+start_date)
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        # 先获得时间数组格式的日期
        threeDayAgo = (start_date - datetime.timedelta(days=int(days)))
        date_out = threeDayAgo.strftime("%Y-%m-%d")
        return date_out
    @staticmethod
    def getTheDatetime():
        now_time = datetime.datetime.now()
        now_date = now_time.strftime('%Y-%m-%d')
        now_date_time = now_time.strftime('%Y-%m-%d-%H%M%S')
        now_month = datetime.datetime(now_time.year, now_time.month,1).strftime('%Y-%m-%d')
        return_val = {
                "now_date":now_date,
                "now_date_time":now_date_time,
                "now_month":now_month
                }
        return return_val

    @staticmethod
    def getEveryDay(begin_date='2019-06-01', end_date='2019-12-31'):
        """指定开始时间和结束时间，获取中间的日期"""
        date_list = []
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
        print('共生成了%s天' % str(len(date_list)))
        # print(date_list)
        return date_list

    @staticmethod
    def make_season(month):
        month = int(month)
        if month in [1, 2, 3]:
            season = 1
        elif month in [4, 5, 6]:
            season = 2
        elif month in [7, 8, 9]:
            season = 3
        else:
            season = 4
        return season


if __name__ == "__main__":
    a1 = timeFunc("2019-01-02", 7,3)
    stat_end_date, pred_start_date, pred_end_dat = a1.make_date()
    print(stat_end_date)

