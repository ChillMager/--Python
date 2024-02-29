from PySide2.QtWidgets import QMessageBox, QTableWidgetItem
import administer_mysql


def sign_in(window1):
	info = window1.textEdit.toPlainText()
	info1 = window1.textEdit1.toPlainText()
	return administer_mysql.sign_in(info, info1)


def print_student_information3(window2):
	info = window2.wb1.toPlainText()
	list1 = administer_mysql.search_student_information(info)
	window2.tableWidget.insertRow(0)
	new_item = QTableWidgetItem(list1[0][0])
	window2.tableWidget.setItem(0, 0, new_item)
	new_item = QTableWidgetItem(list1[0][1])
	window2.tableWidget.setItem(0, 1, new_item)
	new_item = QTableWidgetItem(list1[0][5])
	window2.tableWidget.setItem(0, 2, new_item)
	new_item = QTableWidgetItem(list1[0][6])
	window2.tableWidget.setItem(0, 3, new_item)
	new_item = QTableWidgetItem(list1[0][9])
	window2.tableWidget.setItem(0, 4, new_item)
	new_item = QTableWidgetItem(str(list1[0][10]))
	window2.tableWidget.setItem(0, 5, new_item)
	new_item = QTableWidgetItem(list1[0][11])
	window2.tableWidget.setItem(0, 6, new_item)


def print_signin_information3(window2):
	info = window2.wb2.toPlainText()
	list1 = administer_mysql.search_signin_information(info)
	window2.tableWidget_2.insertRow(0)
	new_item = QTableWidgetItem(list1[0][0])
	window2.tableWidget_2.setItem(0, 0, new_item)
	new_item = QTableWidgetItem(str(list1[0][1]))
	window2.tableWidget_2.setItem(0, 1, new_item)
	new_item = QTableWidgetItem(str(list1[0][2]))
	window2.tableWidget_2.setItem(0, 2, new_item)


def print_queue_information3(window2):
	info = window2.wb3.toPlainText()
	list1 = administer_mysql.search_queue_information(info)
	window2.tableWidget_3.insertRow(0)

	new_item = QTableWidgetItem(str(list1[0][0]))
	window2.tableWidget_3.setItem(0, 0, new_item)
	new_item = QTableWidgetItem(str(list1[0][1]))
	window2.tableWidget_3.setItem(0, 1, new_item)
	new_item = QTableWidgetItem(str(list1[0][10]))
	window2.tableWidget_3.setItem(0, 2, new_item)


def print_car_information3(window2):
	info = window2.wb4.toPlainText()
	list1 = administer_mysql.search_car_information(info)
	window2.tableWidget_4.insertRow(0)
	new_item = QTableWidgetItem(str(list1[0][0]))
	window2.tableWidget_4.setItem(0, 0, new_item)
	new_item = QTableWidgetItem(str(list1[0][1]))
	window2.tableWidget_4.setItem(0, 1, new_item)
	new_item = QTableWidgetItem(str(list1[0][2]))
	window2.tableWidget_4.setItem(0, 2, new_item)
	new_item = QTableWidgetItem(str(list1[0][3]))
	window2.tableWidget_4.setItem(0, 3, new_item)


def aaa(window2):
	info = window2.plainTextEdit.toPlainText()
	administer_mysql.updatestudent(info)
	QMessageBox.information(window2, '操作成功', '已发送通知')


def bbb(window2):
	info = window2.plainTextEdit_3.toPlainText()
	administer_mysql.updatesignin(info)
	QMessageBox.information(window2, '操作成功', '已设置为签到')


def ccc(window2):
	info = window2.plainTextEdit_5.toPlainText()
	administer_mysql.updatequeue(info)
	QMessageBox.information(window2, '操作成功', '已设置为队列优先级')


def ddd(window2):
	info = window2.plainTextEdit_7.toPlainText()
	administer_mysql.updatecar(info)
	QMessageBox.information(window2, '操作成功', '更改车辆状态成功')