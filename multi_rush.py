import os
import re
import sys
import shutil 
import datetime  
import subprocess
 
time = datetime.datetime.now()
now = (time.strftime("%Y%m%d")) 							# For tagging new_rushscript_dir with date
job_num = 0 										# For tagging the user prompts with a job #. 
command_files = [] 									# The final product 
submit_files = []									# The final product 
render_files = []									# The final product


# Make a new directory to house our bundle of scripts we're about to create. The new folder will be named with the date on the end. 
# Ask user how many jobs there are to render. This value is thrown into a for loop to create the appropriate number of files. 
user_rushscript_dir = "/Users/matt/Documents/python/scalable_rush_renders"

while True:
	try:
		nsd = input("New directory for these scripts will be created here {}. Name the directory without using the date and surround in quotations. ".format(user_rushscript_dir))
		job_count = input("How many jobs will you be rendering? No quotations. ") 
		break
	except (NameError, SyntaxError) as e:
		print("ERROR: Follow instructions for use of quotations.")

new_rushscript_dir = os.path.join(user_rushscript_dir + "/" + nsd + "_" + now)
os.umask(000)
if not os.path.isdir(new_rushscript_dir):
	os.mkdir(new_rushscript_dir, 0777)

for i in range(int(job_count)):
	job_num += 1
	# Create new command file for each job.
	shutil.copy("multi_HOPE_ClimateWall", new_rushscript_dir)
	old_command_file = os.path.join(new_rushscript_dir + "/multi_HOPE_ClimateWall")
	new_command_file = os.path.join(new_rushscript_dir + "/HOPE_ClimateWall_" + str(i+1))
	os.rename(old_command_file, new_command_file)
	command_files.append(new_command_file)

	# Create new submit file for each job.
	shutil.copy("multi_python_rush_submit.py", new_rushscript_dir)
	old_submit_file = os.path.join(new_rushscript_dir + "/multi_python_rush_submit.py")
	new_submit_file = os.path.join(new_rushscript_dir + "/multi_python_rush_submit_" + str(i+1) + ".py")
	os.rename(old_submit_file, new_submit_file)
	submit_files.append(new_submit_file)

	# Create new render file for each job. 
	shutil.copy("multi_HOPE_ClimateWall_render", new_rushscript_dir)
	old_render_file = os.path.join(new_rushscript_dir + "/multi_HOPE_ClimateWall_render")
	new_render_file = os.path.join(new_rushscript_dir + "/multi_HOPE_ClimateWall_render_" + str(i+1))
	os.rename(old_render_file, new_render_file)
	render_files.append(new_render_file)


	# Get user input for variables to be used in new files. 	
	while True:	
		try:
			name = input("[JOB #{}] What is the frame name root? ($idir/$name.$i.$iext). Put inside quotations ".format(job_num))
			title = input("[JOB #{}] What would you like to name your render? Put inside quotations ".format(job_num))
			frames = input("[JOB #{}] What is the frame range? Format = X-XXX. Put in quotations ".format(job_num))
			command = new_render_file
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

	# Customize individual render file. 
	with open(new_render_file, "r") as f:
		file = f.read()
	file = file.replace("new_command_file", new_command_file)
	with open(new_render_file, "w") as f:
		f.write(file)
		f.close()

# List files created 
for command_file in command_files: 
	print("COMMAND FILES CREATED:: " + command_file)

for submit_file in submit_files:
	print("SUBMIT FILES CREATED:: " + submit_file)

for render_file in render_files:
	print("RENDER FILES CREATED:: " + render_file)

#Execute commands // submit renders 

# Execute submissions
for x in submit_files:
        submission_file = '"' + x + '"'
        subprocess.check_output([x])



		





	
		




