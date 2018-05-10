import os
import re
import sys
import shutil 
import datetime  
import subprocess
 
time = datetime.datetime.now()
now = (time.strftime("%Y%m%d"))
job_num = 0
command_files = []

# Make a new directory to house our bundle of scripts we're about to create. The new folder will be named with the date on the end. 
user_rushscript_dir = "/Users/matt/Documents/python/scalable_rush_renders"
while True:
	try:
		nsd = input("New directory for these scripts will be created here {}. Name the directory without using the date and surround in quotations ".format(user_rushscript_dir))
		break
	except (NameError, SyntaxError) as e:
		print("ERROR: Use quotations. Try again.")
new_rushscript_dir = os.path.join(user_rushscript_dir + "/" + nsd + "_" + now)
os.umask(000)
if not os.path.isdir(new_rushscript_dir):
	os.mkdir(new_rushscript_dir, 0777)

# Take user input to find out how many jobs we'll be rendering.
user_input = input("How many jobs will you be rendering? ") 


for i in range(user_input):
	job_num += 1
	# Create new command file for each job to be rendered.
	shutil.copy("multi_HOPE_ClimateWall", new_rushscript_dir)
	old_command_file = os.path.join(new_rushscript_dir + "/multi_HOPE_ClimateWall")
	new_command_file = os.path.join(new_rushscript_dir + "/HOPE_ClimateWall_" + str(i+1))
	os.rename(old_command_file, new_command_file)
	command_files.append(new_command_file)

	# Create new submit file for each job to be rendered.
	shutil.copy("multi_python_rush_submit.py", new_rushscript_dir)
	old_submit_file = os.path.join(new_rushscript_dir + "/multi_python_rush_submit.py")
	new_submit_file = os.path.join(new_rushscript_dir + "/multi_python_rush_submit_" + str(i+1) + ".py")
	os.rename(old_submit_file, new_submit_file)

	# Get user input for variables to be used in new files. 	
	while True:	
		try:
			name = input("[JOB #{}] What is the frame name root? ($idir/$name.$i.$iext). Put inside quotations ".format(job_num))
			title = input("[JOB #{}] What would you like to name your render? Put inside quotations ".format(job_num))
			frames = input("[JOB #{}] What is the frame range? Format = X-XXX. Put in quotations ".format(job_num))
			command = new_command_file
			break 
		except (NameError, SyntaxError) as e:
			print("ERROR: Use quotations. Start again.")
	# Customize individual command file. The directory tree should be MYFRAME/src_frames/MRFRAME.12345.png. Name would then be MYFRAME.
	with open(new_command_file, "r") as f:
		file = f.read()
	file = file.replace("ADD_NAME", name)
	with open(new_command_file, "w") as f:
		f.write(file) 
		f.close()

	# Customize individual submit file. 
	with open(new_submit_file, "r") as f:
		file = f.read()
	file = file.replace("MYTITLE", title)
	with open(new_submit_file, "w") as f:
		f.write(file)
		f.close()
	with open(new_submit_file, "r") as f:
		file = f.read()
	file = file.replace("MYFRAMES", frames)
	with open(new_submit_file, "w") as f:
		f.write(file)
		f.close()
	with open(new_submit_file, "r") as f:
		file = f.read()
	file = file.replace("MYCOMMAND", command)
	with open(new_submit_file, "w") as f:
		f.write(file)
		f.close()

# Execute Commands 
for command_file in command_files: 
	print(command_file)


		





	
		




