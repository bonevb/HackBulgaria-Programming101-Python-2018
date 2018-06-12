import sys

def prediction():
	print('Input your data and press Ctrl + D')
	data = sys.stdin.readlines()
	start_money = int(data[0])
	data.remove(data[0])
	pred = [int(money) for money in data[0].split(',')]
	hackcoins = 0

	result = []
	len_pred = len(pred)

	if pred[0] >= pred[1]:
		result.append('hold')
	else:
		result.append('buy')
		hackcoins += start_money/pred[0]
		start_money = 0

	for i in range(1,len_pred-1):
		if pred[i] < pred[i+1] and result[i-1] == 'buy':
			result.append('sell')
			start_money = float(hackcoins * pred[i])
			hackcoins = 0

		if pred[i] < pred[i+1] and result[i-1] == 'sell':
			result.append('buy')
			hackcoins = start_money / pred[i]
			start_money = 0

		if pred[i] < pred[i+1] and result[i-1] == 'hold':
			result.append('buy')
			hackcoins = start_money / pred[i]
			start_money = 0

		elif pred[i] > pred[i+1] and result[i-1] == 'sell':
			result.append('hold')

		elif pred[i] > pred[i+1] and result[i-1] == 'buy':
			result.append('sell')
			start_money = float(hackcoins * pred[i])
			hackcoins = 0

		elif pred[i] > pred[i+1] and result[i-1] == 'hold':
			result.append('hold')

	if pred[-1] > pred[-2] and result[-1] == 'buy':
		result.append('sell')
		start_money = float(hackcoins * pred[-1])

	elif pred[-1] < pred[-2] and result[-1] == 'hold':
		result.append('hold')

	result = ', '.join(result)


	print('{0:.2f}'.format(start_money))
	print(result)


#print(prediction())
