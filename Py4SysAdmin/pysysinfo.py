#!/usr/bin/env python
#A system information Gathering Script
import subprocess

#Command 1
uname = "uname"
uname_arg = "-a"
print "Gathering system infromation with %s command:\n" % uname
subprocess.call([uname, uname_arg])

#Command 2
diskspace = "df"
diskspace_arg = "-h"
print "Gathering diskspace infromation with %s command:\n" % diskspace
subprocess.call([diskspace, diskspace_arg])
