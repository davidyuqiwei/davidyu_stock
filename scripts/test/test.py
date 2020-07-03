import logging
#logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(filename = "a.log", level = logging.DEBUG)
#logger = logging.getLogger(__name__)
 
#logger.info("Start print log")
#logger.debug("Do something")
#logger.warning("Something maybe fail.")
#logger.info("Finish")


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-start_date",type=str,help="start_date",default="2016-01-01")
parser.add_argument("-end_date",type=str,help="end_date",default="2016-12-31")
args=parser.parse_args()
start_date=args.start_date
end_date=args.end_date
print(start_date)
print(end_date)

