from PySide2.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
import distributor_ui_function
import administer_ui_function
import staff_ui_function


class Stats:
	def __init__(self):
		self.main_ui = QUiLoader().load('ui/登录方式.ui')
		self.sign_in_ui = QUiLoader().load('ui/登录.ui')
		self.student_ui = QUiLoader().load('ui/员工.ui')
		self.coach_ui = QUiLoader().load('ui/经销商.ui')
		self.administer_ui = QUiLoader().load('ui/管理员.ui')
		self.main_ui.button.clicked.connect(self.open_sign_in_ui)
		self.main_ui.button1.clicked.connect(self.open_sign_in_ui1)
		self.main_ui.button2.clicked.connect(self.open_sign_in_ui2)

	def open_sign_in_ui1(self):
		self.sign_in_ui.show()
		self.main_ui.close()
		self.sign_in_ui.button.clicked.connect(self.open_coach_window)

	def open_coach_window(self):#教练换
		# 显示新窗口
		if distributor_ui_function.sign_in(self.sign_in_ui):
			self.coach_ui.show()
			self.sign_in_ui.close()
			self.coach_ui.button.clicked.connect(self.print_student_information)
			self.coach_ui.button1.clicked.connect(self.coach_attendance)
			self.coach_ui.button2.clicked.connect(self.change_car)
			self.coach_ui.button3.clicked.connect(self.print_coach_information)
		else:
			QMessageBox.critical(self.sign_in_ui, '错误', '用户名或密码错误！')

	def print_student_information(self):
		distributor_ui_function.print_student_information(self.coach_ui)

	def coach_attendance(self):
		distributor_ui_function.coach_attendance(self.sign_in_ui, self.coach_ui)

	def change_car(self):
		distributor_ui_function.change_car(self.sign_in_ui, self.coach_ui)

	def print_coach_information(self):
		distributor_ui_function.print_coach_information(self.sign_in_ui, self.coach_ui)

	def open_sign_in_ui2(self):
		self.sign_in_ui.show()
		self.main_ui.close()
		self.sign_in_ui.button.clicked.connect(self.open_administer_window)

	def open_administer_window(self):
		# 显示新窗口
		if administer_ui_function.sign_in(self.sign_in_ui):
			self.administer_ui.show()
			self.sign_in_ui.hide()
			self.administer_ui.pushButton.clicked.connect(self.print_student_information3)
			self.administer_ui.pushButton_2.clicked.connect(self.aaa)
			self.administer_ui.pushButton_3.clicked.connect(self.print_signin_information3)
			self.administer_ui.pushButton_4.clicked.connect(self.bbb)
			self.administer_ui.pushButton_5.clicked.connect(self.print_queue_information3)
			self.administer_ui.pushButton_6.clicked.connect(self.ccc)
			self.administer_ui.pushButton_7.clicked.connect(self.print_car_information3)
			self.administer_ui.pushButton_8.clicked.connect(self.ddd)
		else:
			QMessageBox.critical(self.sign_in_ui, '错误', '用户名或密码错误！')

	def print_student_information3(self):
		administer_ui_function.print_student_information3(self.administer_ui)

	def print_signin_information3(self):
		administer_ui_function.print_signin_information3(self.administer_ui)

	def print_queue_information3(self):
		administer_ui_function.print_queue_information3(self.administer_ui)

	def print_car_information3(self):
		administer_ui_function.print_car_information3(self.administer_ui)

	def aaa(self):
		administer_ui_function.aaa(self.administer_ui)

	def bbb(self):
		administer_ui_function.bbb(self.administer_ui)

	def ccc(self):
		administer_ui_function.ccc(self.administer_ui)

	def ddd(self):
		administer_ui_function.ddd(self.administer_ui)

	def open_sign_in_ui(self):
		self.sign_in_ui.show()
		self.main_ui.close()
		self.sign_in_ui.button.clicked.connect(self.open_student_window)

	def open_student_window(self):
		# 显示新窗口
		if staff_ui_function.sign_in(self.sign_in_ui):
			self.student_ui.show()
			self.sign_in_ui.hide()
			'''self.window2.button6.clicked.connect(self.Register_information)'''
			self.student_ui.button1.clicked.connect(self.student_attendance1)
			self.student_ui.button1_3.clicked.connect(self.student_attendance2)
			self.student_ui.button1_4.clicked.connect(self.student_attendance3)
			self.student_ui.button1_5.clicked.connect(self.student_attendance4)
			self.student_ui.button5.clicked.connect(self.print_coach_information1)
			self.student_ui.button5_2.clicked.connect(self.Search_Course)


		else:
			QMessageBox.critical(self.sign_in_ui, '错误', '用户名或密码错误！')

		'''def Register_information(self):
			info = self.window2.textEdit_2.toPlainText()
			info1 = self.window2.comboBox.addstring'''

	def student_attendance1(self):
		staff_ui_function.student_attendance1(self.sign_in_ui, self.student_ui)

	def student_attendance2(self):
		staff_ui_function.student_attendance2(self.sign_in_ui, self.student_ui)

	def student_attendance3(self):
		staff_ui_function.student_attendance3(self.sign_in_ui, self.student_ui)

	def student_attendance4(self):
		staff_ui_function.student_attendance4(self.sign_in_ui, self.student_ui)

	def print_coach_information1(self):
		staff_ui_function.print_coach_information(self.sign_in_ui, self.student_ui)

	def Search_Course(self):
		staff_ui_function.Search_Course(self.student_ui)




app = QApplication([])
stats = Stats()
stats.main_ui.show()
app.exec_()
