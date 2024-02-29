from PySide2.QtWidgets import QMessageBox, QTableWidgetItem
import distributor_mysql


def sign_in(window1):
	info = window1.textEdit.toPlainText()
	info1 = window1.textEdit1.toPlainText()
	return distributor_mysql.sign_in(info, info1)


def print_student_information(window2):
	info = window2.textEdit.toPlainText()
	list1 = distributor_mysql.search_student_information(info)
	window2.table.insertRow(0)
	new_item = QTableWidgetItem(list1[0][0])
	window2.table.setItem(0, 0, new_item)
	new_item = QTableWidgetItem(list1[0][1])
	window2.table.setItem(0, 1, new_item)
	new_item = QTableWidgetItem(list1[0][2])
	window2.table.setItem(0, 2, new_item)
	new_item = QTableWidgetItem(list1[0][3])
	window2.table.setItem(0, 3, new_item)
'''
	new_item = QTableWidgetItem(list1[0][9])
	window2.table.setItem(0, 4, new_item)
	new_item = QTableWidgetItem(str(list1[0][10]))
	window2.table.setItem(0, 5, new_item)
	new_item = QTableWidgetItem(list1[0][11])
	window2.table.setItem(0, 6, new_item)
	'''


def coach_attendance(window1, window2):
	info = window1.textEdit.toPlainText()
	distributor_mysql.Attendance(info)
	QMessageBox.information(window2, '操作成功', '出勤成功')


def change_car(window1, window2):
	info = window1.textEdit.toPlainText()
	info1 = window2.textEdit2.toPlainText()
	choice = QMessageBox.question(window2, '确认', '确定要调花吗？')
	if choice == QMessageBox.Yes:
		distributor_mysql.change_car(info, info1)
		QMessageBox.information(window2, '操作成功', '调花成功')
	if choice == QMessageBox.No:
		QMessageBox.critical(window2, '错误', '调花失败！')


def print_coach_information(window1, window2):
	info = window1.textEdit.toPlainText()
	list1 = distributor_mysql.print_coach_information(info)
	a = 0
	window2.table1.insertRow(0)
	while a < 4:
		new_item = QTableWidgetItem(list1[0][a])
		window2.table1.setItem(0, a, new_item)
		a += 1
