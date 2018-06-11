#main.py
try:
	import getpass
	import hashlib
	import svr_conn as conn
#checking dbconnection
	if conn.testconn():
		print("connected sucessfully")
	else:
		print("connected failed")
	print("{:+^100}".format("Welcome to Civorution"))
	while True:
		print("waiting for command...")
		user = ""
		pswd = ""
		comd = input()
#command list: "i"for log in;"u"for log up;"h"for gethelp
		if comd == "i":
			user = input("username:")
			pswd = input("password:")
			pswd = hashlib.md5(pswd.encode('utf-8')).hexdigest()
			rt = conn.login(user,pswd)
			if rt == -1:
				print("woring username")
			elif rt == 0:
				print("woring password")
			elif rt == 1:
				print("welcome back {}".format(user))
			else:
				print("unexpect")
			break
		elif comd == "u":
			print("Creating new accont...")
			user = input("username:")
			pswd = input("password(well not show characters):")
			pswd = hashlib.md5(pswd.encode('utf-8')).hexdigest()
			rt = conn.logup(user,pswd)
			if rt == 0:
				print("username has been ocupied")
			elif rt == 1:
				print("sucess")
			else:
				print("unexpect")
			break
		else:
			print("command list: \"i\"for log in;\"u\"for log up;\"h\"for gethelp")
except:
	print("error")
finally:
	input('Press Enter to exit...')
