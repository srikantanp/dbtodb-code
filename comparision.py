def comparision(tab1,tab2):
	if sorted(tab1)==sorted(tab2):
		print "Tables are Equal"
		return "equal"
	else:
		print "tables are not equal"
		return "mismatch"