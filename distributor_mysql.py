import pymysql as mysql


def sign_in(coach_number, password):
	""" 登录函数 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="zjz")
	cur = conn.cursor()
	sql = f"select * from `经销商密码表` where `经销商编号` = '{coach_number}' "
	cur.execute(sql)
	list1 = cur.fetchall()
	if password == list1[0][1]:
		return 1
	else:
		return 0


def Attendance(coach_number):
	""" 出勤函数 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="zjz")
	cur = conn.cursor()
	sql = f"UPDATE `经销商表` set `状态` = '在岗' where `经销商编号` = '{coach_number}' "
	cur.execute(sql)
	conn.commit()


def search_student_information(student_number):
	""" 查找学生信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="zjz")
	cur = conn.cursor()
	sql = f"select * from `花数据库表` where `花编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


def print_coach_information(coach_number):
	""" 显示教练信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="zjz")
	cur = conn.cursor()
	sql = f"select `经销商编号`,`花编号`,`经销商姓名`,`家庭地址` from `经销商表` where `经销商编号` = '{coach_number}' "
	cur.execute(sql)
	return cur.fetchall()


def change_car(coach_number, car_number):
	""" 调车 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="zjz")
	cur = conn.cursor()
	sql1 = f"select `经销商姓名`,`经销商编号`from `经销商表` where `花编号` = '{car_number}'"
	cur.execute(sql1)
	last_all = cur.fetchall()[0]
	sql2 = f"select `经销商姓名`,`花编号` from `经销商表` where `经销商编号` = '{coach_number}'"
	cur.execute(sql2)
	now_all = cur.fetchall()[0]
	sql3 = f"update `经销商表` set `花编号` = '{car_number}' where `经销商编号` = '{coach_number}'"
	cur.execute(sql3)
	sql4 = f"update `经销商表` set `花编号` = '{now_all[1]}' where `经销商编号` = '{last_all[1]}'"
	cur.execute(sql4)
	sql5 = f"update `花数据库表` set `经销商姓名` = '{now_all[0]}' where `花编号` = '{car_number}'"
	cur.execute(sql5)
	sql6 = f"update `花数据库表` set `经销商姓名` = '{last_all[0]}' where `花编号` = '{now_all[1]}'"
	cur.execute(sql6)
	conn.commit()

