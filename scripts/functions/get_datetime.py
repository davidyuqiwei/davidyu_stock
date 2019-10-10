import datetime


def get_the_datetime():
    now_time = datetime.datetime.now()
    now_date = now_time.strftime('%Y_%m_%d')
    now_date_time = now_time.strftime('%Y_%m_%d_%H%M%S')
    return now_date,now_date_time

#now_date,now_date_time = 

