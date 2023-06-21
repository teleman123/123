def NetProfit（）：
	income = input(‘请输入总收入：’)
	salary = input(‘请输入会计小王的薪资：’)
	catering_expense =  input(‘请输入餐饮费：’)
	traffic_expense = input(‘请输入交通费’)
	if income.isdigit() and salary.isdigit() and catering_expense.isdigit() and traffic_expense.isdigit() :
		profit = int(income)-int(salary)-int(catering_expense)-int(traffic_expense)
		if profit < 0 :
			print('利润为负')   #暂无计算公式
		else:
			net_profit = str(profit * 0.8)
			print('净利润为：' + net_profit)

	else:
		print('输入错误')
	
	print('函数结束')
