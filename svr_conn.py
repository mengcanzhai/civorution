#svr_conn
#connect to database
#u=civconn p=civ123456
print("checking for connection...")
try:
	import pymysql as ps
	def test():
		print("svr_conn has been imported...")
		
	def conn():
		connection = ps.connect(host = 'localhost',user = 'civconn',password = 'civ123456',database = 'civorution')
		return connection
		
	def testconn():
		try:
			connection = conn()
			if connection.open:
				return True
			else:
				return False
		finally:
			connection.close()
			
	def checkuser(u):
		try:
			connection = conn()
			sql = "SELECT * FROM user WHERE user=%s"
			rt = connection.cursor().execute(sql,u)
			return rt
		finally:
			connection.close()
			
	def logup(u,p):
		if checkuser(u):
			return 0
		else:
			try:
				connection = conn()
				sql = "INSERT INTO user VALUES (%s,%s)"
				rt = connection.cursor().execute(sql,(u,p))
				connection.commit()
				return rt
			finally:
				connection.close()
				
	def login(u,p):
		if not checkuser(u):
			return -1
		else:
			try:
				connection = conn()
				sql = "SELECT * FROM user WHERE user=%s AND pswd=%s"
				rt = connection.cursor().execute(sql,(u,p))
				return rt
			finally:
				connection.close()
				
except:
	print("conn_error")