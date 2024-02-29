from PySide2.QtWidgets import QMessageBox, QTableWidgetItem
import staff_mysql


def sign_in(window1):
	info = window1.textEdit.toPlainText()
	info1 = window1.textEdit1.toPlainText()
	return staff_mysql.sign_in(info, info1)


def open_new_window(self):
	# 显示新窗口
	if self.sign_in():
		self.window2.show()
		self.ui.hide()
		'''self.window2.button6.clicked.connect(self.Register_information)'''
		self.window2.button1.clicked.connect(self.student_attendance1)
		self.window2.button1_3.clicked.connect(self.student_attendance2)
		self.window2.button1_4.clicked.connect(self.student_attendance3)
		self.window2.button1_5.clicked.connect(self.student_attendance4)
		self.window2.button5.clicked.connect(self.print_coach_information)
		self.window2.button5_2.clicked.connect(self.Search_Course)
		self.window2.button5_3.clicked.connect(self.Search_Test)

	else:
		QMessageBox.critical(self.ui, '错误', '用户名或密码错误！')

	'''def Register_information(self):
		info = self.window2.textEdit_2.toPlainText()
		info1 = self.window2.comboBox.addstring'''


def print_coach_information(window1, window2):
	info1 = window1.textEdit.toPlainText()

	info = window2.textExit5.toPlainText()
	staff_mysql.Appointment_Coach(info1, info)
	list1 = staff_mysql.Search_Coach(info)
	window2.table.insertRow(0)
	new_item = QTableWidgetItem(list1[0][0])
	window2.table.setItem(0, 0, new_item)
	new_item = QTableWidgetItem(list1[0][1])
	window2.table.setItem(0, 1, new_item)
	new_item = QTableWidgetItem(list1[0][2])
	window2.table.setItem(0, 2, new_item)
	new_item = QTableWidgetItem(list1[0][3])
	window2.table.setItem(0, 3, new_item)
	new_item = QTableWidgetItem(str(list1[0][4]))
	window2.table.setItem(0, 4, new_item)
	new_item = QTableWidgetItem(list1[0][5])
	window2.table.setItem(0, 5, new_item)
	new_item = QTableWidgetItem(list1[0][6])
	window2.table.setItem(0, 6, new_item)
	new_item = QTableWidgetItem(list1[0][7])
	window2.table.setItem(0, 7, new_item)
	new_item = QTableWidgetItem(list1[0][8])
	window2.table.setItem(0, 8, new_item)


def Search_Course(window2):
	info = window2.textExit5_2.toPlainText()
	list1 = staff_mysql.Search_Course(info)
	window2.table_2.insertRow(0)
	new_item = QTableWidgetItem(list1[0][0])
	window2.table_2.setItem(0, 0, new_item)
	new_item = QTableWidgetItem(list1[0][1])
	window2.table_2.setItem(0, 1, new_item)
	new_item = QTableWidgetItem(str(list1[0][2]))
	window2.table_2.setItem(0, 2, new_item)
	new_item = QTableWidgetItem(str(list1[0][3]))
	window2.table_2.setItem(0, 3, new_item)
	new_item = QTableWidgetItem(str(list1[0][4]))
	window2.table_2.setItem(0, 4, new_item)
	new_item = QTableWidgetItem(str(list1[0][5]))
	window2.table_2.setItem(0, 5, new_item)




def student_attendance1(window1, window2):
	info = window1.textEdit.toPlainText()
	staff_mysql.log_in(info)
	QMessageBox.information(window2, '操作成功', '定位签到成功')


def student_attendance2(window1, window2):
	info = window1.textEdit.toPlainText()
	staff_mysql.log_in(info)
	QMessageBox.information(window2, '操作成功', '手势签到成功')


def student_attendance3(window1, window2):
	info = window1.textEdit.toPlainText()
	staff_mysql.log_in(info)
	QMessageBox.information(window2, '操作成功', '验证码签到成功')


def student_attendance4(window1, window2):
	info = window1.textEdit.toPlainText()
	staff_mysql.log_in(info)
	QMessageBox.information(window2, '操作成功', '拍照签到成功')
