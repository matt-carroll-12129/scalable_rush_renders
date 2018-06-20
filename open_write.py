def open_write(file_variable, old_text, new_text_variable):
	with open(file_variable, "r") as f:
		file = f.read()
	file = file.replace(old_text, new_text_variable)
	with open(file_variable, "w") as f:
		f.write(file)
		f.close()

