#!/usr/bin/sh
#cp -r /cygdrive/g/stock/data/financial_report/shenzhen/ /cygdrive/g/stock/data/financial_report/shenzhen_test/
## find name not has 'tr' and remove it
find /cygdrive/g/stock/data/financial_report/shanghai/* ! -name '*tr*' | xargs rm -f


### remove file like 000001_tr.csv end 
find /cygdrive/g/stock/data/financial_report/shanghai/ -regex ".*/[0-9]*_tr.csv" | xargs rm -f

#find /cygdrive/g/stock/data/financial_report/shenzhen_test/* ! -name '*tr*';
