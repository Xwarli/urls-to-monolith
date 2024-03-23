import os
import subprocess

# User inputs the url-list
url_list = open(input("url-list = "), "r")

for url in url_list:
	try:
		url = url.replace("\n", "-")
		output_file = url.replace("/","_").replace(".", "-").replace("\n", "-") + ".html"
		command = "monolith " + url + " -I -o " + output_file
		print(command)
		subprocess.run(command, shell=True)
		print("[saved] " + url)
	except:
		print("[error]" + url)

url_list.close
