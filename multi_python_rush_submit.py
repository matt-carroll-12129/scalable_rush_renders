#!/usr/bin/env python

import os
import sys

if (len(sys.argv) <= 1):
	if (os.environ.has_key("RUSH_ISDAEMON")):
		sys.exit(1)

submit = os.popen("rush -submit", "w")

submit.write(	 "title				MYTITLE\n"							
				+"ram				1024\n " 									
				+"frames			MYFRAMES\n"									
				+"logdir			/hd/na10/junk\n"							
				+"command			MYCOMMAND\n"
				+"donemail			mcarroll@amnh.org\n"									
				+"waitforstate			done\n"													
				+"cpus				linuxbox32\n"													
				 #"nevercpus			#NEVERCPUS\n"												 
			) 

err = submit.close()
if err:
	sys.exit(1)			#Submit Failed 
sys.exit(0)				#Submit Succeeded 