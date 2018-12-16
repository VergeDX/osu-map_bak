import re
import os

print ('\n-------------------------------------------------')	#	print help message
print ('First,you should open your osu\\songs dir')
print ('hold shift,and right click your mouse')
print ('choice \'open cmd here\',and do \'dir /ad /b > bak\'')
print ('copy your osu\\songs\\bak file here')
print ('-------------------------------------------------\n')

path_bak = './bak'	#	you also can change this path to your bak file
re_csv = re.compile(r'^\d+')	#	compile re
result = []	#	save the result data
path_result = './result'

try:
	with open(path_bak,'r') as file_bak:	#	try to open the bak file

		while 1:

			line = file_bak.readline()  #       read one line,and use compile re
			match = re.match (re_csv,line)   #       re.match,only find at the line head

			if match:
        	        	result.append (match.group(0))   #       if finded,let matched result append result[]

			if not line:
	                	break	#       if not line,exit

except FileNotFoundError as fnfe:	#	if no file
	print ('File not found!')
	print ('This is exception message:',fnfe)
	print ('\n')
	exit (1)

if result:
	try:
		os.mknod ('result')	#	create result file to write result[]
	except FileExistsError:
		print ('result file is existed : (\n')
		exit (1)

with open (path_result,'w') as file_result:
	for i in result:
		file_result.writelines(i)	#	write result file
		file_result.write('\n')	#	change to ',' is CSV
	file_result.close()

print ('Done,check result file : )\n')
exit (0)
