from sys import argv
script, first, second = argv
name = raw_input("What's your Name? ")
print "Dear %s Why the hell are you running %r" % (name, script),
print "with unnessary %r and %r arguments" % (first, second)
