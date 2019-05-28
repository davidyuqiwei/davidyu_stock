programName=${0##*/}   ### filename without extention type e.g.  test.sh  test
#echo $programName
file_name=${programName%.*} #   'test.sh'


echo $programName
echo $file_name
