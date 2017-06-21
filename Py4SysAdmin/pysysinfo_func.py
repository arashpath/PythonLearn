#!/usr/bin/env python
#A system information Gathering Script
import subprocess

#Command 1
def uname_func():
	uname = "uname"
	uname_arg = "-a"
	print "Gathering system infromation with %s command:\n" % uname
	subprocess.call([uname, uname_arg])

#Command 2
def disk_func():
	diskspace = "df"
	diskspace_arg = "-h"
	print "Gathering diskspace infromation with %s command:\n" % diskspace
	subprocess.call([diskspace, diskspace_arg])
def main():
	uname_func()
	disk_func()
#idiom
if __name__ == "__main__":
	main()
