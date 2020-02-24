nohup MakeLogFileShell.sh run_download_fin_report.sh > /dev/null 2>&1
nohup MakeLogFileShell.sh run_download_fin_report.sh  >/dev/null 2>&1  & echo $! > pidfile.txt
