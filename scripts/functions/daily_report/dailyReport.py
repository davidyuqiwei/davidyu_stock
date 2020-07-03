from davidyu_cfg import *
class dailyReport:
    def __init__(self,now_date):
        self.test = 'test'
        self.now_date = now_date
    def save_to_daily_report(self):
        report_dir = data_dict.get("daily_report")
        save_dir = os.path.join(report_dir,self.now_date)
        make_dir(save_dir)
        return save_dir

