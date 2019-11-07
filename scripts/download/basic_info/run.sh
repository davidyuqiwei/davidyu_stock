#!/usr/bin/sh
sh MakeLogFilePython.sh stock_index.py
programName="run_scala.sh"
target_table="stock.base_test"
target_csv="all.csv"
sh $programName $target_table $target_csv

