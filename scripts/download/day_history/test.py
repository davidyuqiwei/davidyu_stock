import os
a1=os.popen(" hive -f check_data.sql ")
a2=a1.read()

v1=a2.split("\n")[1]
print(v1)
