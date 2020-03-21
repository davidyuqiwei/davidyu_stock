#!/usr/bin/sh
## use root to git
## check if have large files , if has , stop
folder_size=`du -s | awk '{ print $1  }'`
foler_size_M=`du -sh`
echo $folder_size_M
if [ $folder_size -gt 55704 ]
then 
  echo 'Error: there has large files'
  exit 0
fi
git config --global user.email "davidyuqiwei@outlook.com"
git config --global user.name "davidyuqiwei"
git config --global push.default simple
git add --all
git commit -m "david"
git push
