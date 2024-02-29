import pymysql as mysql


def sign_in(coach_number, password):
	""" 管理员登录函数 """
	conn = mysql.connect(host="localhost", user="root", password="123456",db="zjz")
	cur = conn.cursor()
	sql = f"select * from `管理员密码表` where `管理员编号` = '{coach_number}' "
	cur.execute(sql)
	list1 = cur.fetchall()
	if password == list1[0][1]:
		return 1
	else:
		return 0


def search_student_information(student_number):
	""" 查找员工信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="zjz")
	cur = conn.cursor()
	sql = f"select * from `员工表` where `员工编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


def search_signin_information(student_number):
	""" 查找签到表信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="zjz")
	cur = conn.cursor()
	sql = f"select * from `签到表` where `员工编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


def search_queue_information(student_number):
	""" 查找队列优先级信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="zjz")
	cur = conn.cursor()
	sql = f"select * from `队列优先级表` where `员工编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


def search_car_information(student_number):
	""" 查找花数据库表信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="zjz")
	cur = conn.cursor()
	sql = f"select * from `花数据库表` where `花编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


def updatesignin(number):
	con = mysql.connect(host="localhost", user="root", password="123456", database="zjz")
	# 创建操作游标

	with con:
		with con.cursor() as cursor:
			sql1 = f"UPDATE `签到表` SET `签到表`.`签到状态` =  '已签到'  WHERE `签到表`.`员工编号` = '{number}'"
			# 执行创建sql语句
			cursor.execute(sql1)
		# 提交数据
		con.commit()


def updatecar(number):
	con = mysql.connect(host="localhost", user="root", password="123456", database="zjz")
	# 创建操作游标

	with con:
		with con.cursor() as cursor:
			sql1 = f"UPDATE `花数据库表` SET `花数据库表`.`花状态` =  '使用'  WHERE `花数据库表`.`花编号` = '{number}'"
			# 执行创建sql语句
			cursor.execute(sql1)
		# 提交数据
		con.commit()


def updatequeue(number):
	con = mysql.connect(host="localhost", user="root", password="123456", database="zjz")
	# 创建操作游标

	with con:
		with con.cursor() as cursor:
			sql1 = f"UPDATE `队列优先级表` SET `队列优先级表`.`优先级` =  '优先级'  WHERE `队列优先级表`.`员工编号` = '{number}'"
			# 执行创建sql语句
			cursor.execute(sql1)
		# 提交数据
		con.commit()


def updatestudent(number):
	con = mysql.connect(host="localhost", user="root", password="123456", database="zjz")
	# 创建操作游标

	with con:
		with con.cursor() as cursor:
			sql1 = f"UPDATE `员工表` SET `员工表`.`员工状态` =  '已通知'  WHERE `员工表`.`员工编号` = '{number}'"
			# 执行创建sql语句
			cursor.execute(sql1)
		# 提交数据
		con.commit()