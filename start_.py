import requests
import traceback

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import threading

import time
from datetime import datetime, timedelta

import json
import configparser
import teleg
#import datetime

true_orders = {}

drivers = []


config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

def update_json():
	while True:
#		print('in json')
		try:
#			print(config['JSON']['link_json'])
			response = requests.get(config['JSON']['link_json'])
			global true_orders
			true_orders = json.loads(response.text)
		except Exception as e:
			pass
#		print(datetime.now(), true_orders)
#		print('ss')
	#	print(orders)
	# 	for order in orders:
	# #		print(coin, order['coin'])
	# 		if coin in order['coin']:
	# 			true_order = order
	# 			break
	# 	print('time ', str(datetime.now()))
	# 	print(true_order)
		time.sleep(20)


def add_coins(orders, driver, wait_orders):


	i_orders = len(orders['orders'])
	i = 1
	while i < i_orders:
		driver = webdriver.Chrome('chromedriver', options = options)
#		driver = webdriver.Chrome('chromedriver.exe', options = options)
#		driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
		wait_orders = WebDriverWait(driver,30)
		#print(orders['orders'][i]['link'])
	#	wait_auth = WebDriverWait(driver, 180)
		driver.get(orders['orders'][i]['link'])
		wait_orders.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='right']//div[@class='tbody']/div/ul")))
		for cookie in cookies:
	#		print(cookie)
			driver.add_cookie(cookie)

		driver.get(orders['orders'][i]['link'])
		wait_orders.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='right']//div[@class='tbody']/div/ul")))
		global drivers
		drivers.append(driver)


# 		driver.execute_script(("ooo = document.getElementsByTagName('head')[0].innerHTML;"))
# #		driver.execute_script(("document.body.innerHTML += document.getElementsByTagName('head')[0].innerHTML;"))
# 		time.sleep(1)
# 		#driver.execute_script(("document.getElementsByTagName('head')[0].innerHTML('<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>');"))
# 		#driver.execute_script(("'<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>';"))
# 		driver.execute_script(("document.getElementsByTagName('head')[0].remove();"))
# #		time.sleep(1)
# #		driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
# 		time.sleep(1)
# 		driver.execute_script(("document.body.insertAdjacentHTML('beforeend', ooo);"))
# 		driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
# 		driver.execute_script(("document.getElementsByClassName('left')[0].remove();"))
# 		time.sleep(1)
# 		driver.execute_script(("document.getElementsByClassName('ee340b')[0].remove();"))


		i = i + 1
		# print(orders['orders'][i]['link'])
		# driver.execute_script("window.open('about:blank');")
		# i = i + 1
		# time.sleep(1)


	#print(drivers)
	for driver in drivers:
		print(driver.current_url)

#	input()
# 	i = 0
# 	print(len(driver.window_handles))
# 	for item in orders['orders']:
# 		driver.switch_to_window(driver.window_handles[i])
# 		driver.get(item['link'])
# 		wait_orders.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div/div')))
# 		driver.execute_script(("document.getElementsByClassName('left')[0].remove();"))
# 		driver.execute_script(("document.getElementsByClassName('ee340b')[0].remove();"))
# #		ee340b
# 		i = i + 1
# 	return driver

def close_tabs(driver):
	i_close = 1
	while i_close < len(driver.window_handles):
		driver.switch_to_window(driver.window_handles[i_close])
		driver.close()
		i_close = i_close + 1
	return driver

options = Options()
#options.set_capability("pageLoadStrategy", "none")
options.add_argument('--log-level=3')
options.add_argument('--disable-logging')
options.add_argument('--start-maximized')

driver = webdriver.Chrome('chromedriver.exe', options = options)
#driver = webdriver.Firefox(executable_path=r'geckodriver.exe')

wait_orders = WebDriverWait(driver,30)
wait_auth = WebDriverWait(driver, 180)

# print(response.text)

# orders = json.loads(response.text)
resp = threading.Thread(target=update_json, daemon=True)
resp.start()

driver.get(config['JSON']['exchange_entrypoint'])

# print('Продолжить выполнение? (y/n)')
# stop_go = input()
# if 'n' in stop_go:
# 	quit()

#quit()``

#print(driver.title)
#wait_auth.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'userTextWrap')]")))
wait_auth.until(EC.presence_of_element_located((By.XPATH, "//div[@class='wraper minw']")))

while True:
	print('not json')
	if true_orders:
		break
	time.sleep(5)
orders = true_orders

driver.get(orders['orders'][0]['link'])
wait_orders.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='right']//div[@class='tbody']/div/ul")))
cookies = driver.get_cookies()
#driver.get(orders['orders'][0]['link'])
#global drivers
drivers.append(driver)

# driver.execute_script(("ooo = document.getElementsByTagName('head')[0].innerHTML;"))
# #		driver.execute_script(("document.body.innerHTML += document.getElementsByTagName('head')[0].innerHTML;"))
# time.sleep(1)
# #driver.execute_script(("document.getElementsByTagName('head')[0].innerHTML('<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>');"))
# #driver.execute_script(("'<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>';"))
# driver.execute_script(("document.getElementsByTagName('head')[0].remove();"))
# #		time.sleep(1)
# #		driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
# time.sleep(1)
# driver.execute_script(("document.body.insertAdjacentHTML('beforeend', ooo);"))
# driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
# driver.execute_script(("document.getElementsByClassName('left')[0].remove();"))
# time.sleep(1)
# driver.execute_script(("document.getElementsByClassName('ee340b')[0].remove();"))


#document.createElement(tagName, [options])
#document.head.innerHTML += '<script src="http://example.com/file.js"></script>';
#driver.execute_script(("document.createElement('blackblock');"))
#driver.execute_script(("document.getElementsByTagName('blackblock')[0].innerHTML = document.getElementsByTagName('head')[0].innerHTML;"))
# driver.execute_script(("document.body.innerHTML += '<h10>' + document.getElementsByTagName('head')[0].innerHTML + '</h10>';"))
# time.sleep(1)
# #driver.execute_script(("document.getElementsByTagName('head')[0].innerHTML('<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>');"))
# #driver.execute_script(("'<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>';"))
# driver.execute_script(("document.getElementsByTagName('head')[0].remove();"))
# time.sleep(1)
# driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
# input()
# i_orders = len(orders['orders'])
# i = 1
# while i < i_orders:
# 	print(orders['orders'][i]['link'])
# 	driver.execute_script("window.open('about:blank');")
# 	i = i + 1
# 	time.sleep(1)


# i = 0
# print(len(driver.window_handles))
# for item in orders['orders']:
# 	driver.switch_to_window(driver.window_handles[i])
# 	driver.get(item['link'])
# 	wait_orders.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='bid-ask-item']")))
# 	i = i + 1

driver = add_coins(orders, driver, wait_orders)

#driver.switch_to_window(driver.window_handles[1])
date_now = datetime.now()
time_delta = timedelta(seconds = 20)
date_end = date_now + time_delta

date_reload = date_now + timedelta(hours = 1)
# for window in range(len(driver.window_handles)):
# 	driver.close()


while True:
#	orders.find_element_by_class_name('bid-ask-item')
	orders = true_orders
	try:
#		print('go')
#		print(len(drivers))
		for driver in drivers:
	#			driver.switch_to_window(driver.window_handles[window])
			for i in range(len(orders['orders'])):
				if orders['orders'][i]['link'] in driver.current_url:
					print("работаем с")
					print(orders['orders'][i]['coin'])
					orders_stakan = driver.find_elements('xpath', "//div[@class='right']//div[@class='tbody']/div/ul")[0].find_elements(By.TAG_NAME, 'li')
					
					#print("получаю цену в стакане")
					order = orders_stakan[len(orders_stakan)-1]

					#print(orders_stakan)

					#print("Получае данные из стакана")
					data = order.find_elements(By.TAG_NAME, 'span')
					#Иногда тут выходит ошибка

					try:
						summ_availeble = float(data[1].text.replace(',', ''))
					except:
						teleg.send_info('пропустили из-за ошибки в строке 260')
						continue
					
					#summ_availeble = float(data[1].text.replace(',', ''))




	#					print(data[0].text, data[2].text)
	#					print(orders['orders'][i]['link'], driver.current_url)
	#					from_coin = wait_orders.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='transaction-money']")))[0].text.split(' ')[2]
					#print("получаю монету из которой продаем")
					#from_coin = driver.find_elements('xpath', '//div[@class="amount"]')[0].text.split(' ')[0]
					#print(from_coin)
	#				from_coin = wait_orders.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]')))[0].text.split(' ')[0]
	#					balance = float(wait_orders.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='transaction-money']")))[0].text.split(' ')[1])
					#print("получаю баланс")
					balance = float(driver.find_elements('xpath', '//div[@class="amount"]')[0].text.split(' ')[2].replace(',',''))
					#print(balance)
					#print(datetime.now(), orders['orders'][i]['coin'], float(data[0].text), float(orders['orders'][i]['targetPrice']), summ_availeble, float(orders['orders'][i]['minCount']))
#					print(balance, from_coin)
					flag = False
					while balance < 20.0:
						balance = float(driver.find_elements('xpath', '//div[@class="amount"]')[0].text.split(' ')[2].replace(',',''))
						if flag == False:
							teleg.send_info('Необходимо пополнить баланс. Текущий: ' + str(balance))
							flag = True
						time.sleep(60)
					if flag == True:
						teleg.send_info('Баланс пополнен. Текущий: ' + str(balance))
						for driver in drivers:
							# driver.switch_to_window(tab)
							driver.refresh()
					# 		wait_orders.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='right']//div[@class='tbody']/div/ul")))
					# 		driver.execute_script(("ooo = document.getElementsByTagName('head')[0].innerHTML;"))
					# #		driver.execute_script(("document.body.innerHTML += document.getElementsByTagName('head')[0].innerHTML;"))
					# 		time.sleep(1)
					# 		#driver.execute_script(("document.getElementsByTagName('head')[0].innerHTML('<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>');"))
					# 		#driver.execute_script(("'<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>';"))
					# 		driver.execute_script(("document.getElementsByTagName('head')[0].remove();"))
					# #		time.sleep(1)
					# #		driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
					# 		time.sleep(1)
					# 		driver.execute_script(("document.body.insertAdjacentHTML('beforeend', ooo);"))
					# 		driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
					# 		driver.execute_script(("document.getElementsByClassName('left')[0].remove();"))
					# 		time.sleep(1)
					# 		driver.execute_script(("document.getElementsByClassName('ee340b')[0].remove();"))
						break

					#print("Проверяю цены")


					# 					try:
					# 	summ_availeble = float(data[1].text.replace(',', ''))
					# except:
					# 	teleg.send_info('пропустили из-за ошибки в строке 260')
					# 	continue

					try: 
						tmpPrice = float(data[0].text)
					except:
						teleg.send_info('пропустили из-за ошибки в строке 325 (300)')
						continue

					if tmpPrice <= float(orders['orders'][i]['targetPrice']) and summ_availeble >= float(orders['orders'][i]['minCount']):
	#						driver.find_elements_by_id('getCountPrice')[0].send_keys(data[0].text)
#						order.click()
						#print("Есть что купить")
						#teleg.send_info("Есть что купить")
						if config['BUY']['separator'] == '.':
							driver.find_elements('xpath', '//input[@type="number"]')[0].send_keys(data[0].text)
						else:
							driver.find_elements('xpath', '//input[@type="number"]')[0].send_keys(data[0].text.replace('.',','))
		#				driver.find_elements_by_id('getCountCoin')[0].send_keys(data[2].text)
						amount = summ_availeble*float(data[0].text)
						# print(amount, balance)
						# if amount > balance:
						# 	teleg.send_info('Недостаточно ' + str(amount - balance) + ' ' + from_coin + ' для покупки монеты ' + str(orders['orders'][i]['coin']) + ' на сумму ' + data[1].text + ' по курсу ' + data[0].text)
						buy = balance/float(data[0].text)
	#						driver.find_elements_by_id('getCountCoin')[0].send_keys(str(orders['orders'][i]['minCount']))
						if config['BUY']['full_buy'] == 'no':
							if buy > summ_availeble:
								buy = summ_availeble
						if config['BUY']['separator'] == '.':
							driver.find_elements('xpath', '//input[@type="number"]')[1].send_keys(str(buy))
						else:
							driver.find_elements('xpath', '//input[@type="number"]')[1].send_keys(str(buy).replace('.',','))
						time.sleep(0.5)
						amount_bit = float(driver.find_elements(By.CLASS_NAME, 'orderform-price')[0].text.split('Value')[1].split(' ')[0])
						if amount_bit <= float(config['BUY']['notification_min_balance']):
							driver.find_elements('xpath', '//input[@type="number"]')[0].send_keys(Keys.CONTROL + 'a')
							driver.find_elements('xpath', '//input[@type="number"]')[0].send_keys(Keys.DELETE)
							driver.find_elements('xpath', '//input[@type="number"]')[1].send_keys(Keys.CONTROL + 'a')
							driver.find_elements('xpath', '//input[@type="number"]')[1].send_keys(Keys.DELETE)
							continue
						if amount > balance:
							teleg.send_info('Недостаточно ' + str(amount - balance) + ' ' + from_coin + ' для покупки монеты ' + str(orders['orders'][i]['coin']) + ' на сумму ' + str(summ_availeble) + ' по курсу ' + data[0].text)
						driver.find_elements(By.CLASS_NAME, 'orderform-btn')[0].click()
						time.sleep(1)
						error = driver.find_elements('xpath', '//div[@class="modal"]')
						print(len(error))
						if len(error) > 0:
							driver.find_element_by_class_name('modal-btn-ok').click()
						teleg.send_info('Куплено ' + str(orders['orders'][i]['coin']) + ' на сумму ' + str(buy)  + ' по курсу ' + data[0].text)
						time.sleep(0.5)
						#отчищаем поля
						driver.find_elements('xpath', '//input[@type="number"]')[0].send_keys(Keys.CONTROL + 'a')
						driver.find_elements('xpath', '//input[@type="number"]')[0].send_keys(Keys.DELETE)
						driver.find_elements('xpath', '//input[@type="number"]')[1].send_keys(Keys.CONTROL + 'a')
						driver.find_elements('xpath', '//input[@type="number"]')[1].send_keys(Keys.DELETE)
						if config['BUY']['pause_after_buy'] == 'yes':
							print('Continue? (y/n)')
							stop_go = input()
							date_end = datetime.now()
							if 'n' in stop_go:
								quit()
						for driver in drivers:
							driver.refresh()
							wait_orders.until(EC.presence_of_all_elements_located((By.XPATH,  "//div[@class='right']//div[@class='tbody']/div/ul")))

					# 		driver.execute_script(("ooo = document.getElementsByTagName('head')[0].innerHTML;"))
					# #		driver.execute_script(("document.body.innerHTML += document.getElementsByTagName('head')[0].innerHTML;"))
					# 		time.sleep(1)
					# 		#driver.execute_script(("document.getElementsByTagName('head')[0].innerHTML('<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>');"))
					# 		#driver.execute_script(("'<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>';"))
					# 		driver.execute_script(("document.getElementsByTagName('head')[0].remove();"))
					# #		time.sleep(1)
					# #		driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
					# 		time.sleep(1)
					# 		driver.exec ute_script(("document.body.insertAdjacentHTML('beforeend', ooo);"))
					# 		driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
					# 		driver.execute_script(("document.getElementsByClassName('left')[0].remove();"))
					# 		time.sleep(1)
					# 		driver.execute_script(("document.getElementsByClassName('ee340b')[0].remove();"))
					break
		time.sleep(float(config['BUY']['check_pause']))
	except Exception as e:
		teleg.send_info('Возникла ошибка: ' + str(e) + '\nПауза ' + str(config['BUY']['error_pause']) + ' секунд')
		print(datetime.now(), 'Возникла ошибка: ' + str(e) + '\nПауза ' + str(config['BUY']['error_pause']) + ' секунд')
		print(traceback.format_exc())

		#input("Press Enter to continue...")
		for driver in drivers:
			# driver.switch_to_window(tab)
			driver.refresh()


			# wait_orders.until(EC.presence_of_all_elements_located((By.XPATH,  "//div[@class='right']//div[@class='tbody']/div/ul")))
	# 		driver.execute_script(("ooo = document.getElementsByTagName('head')[0].innerHTML;"))
	# #		driver.execute_script(("document.body.innerHTML += document.getElementsByTagName('head')[0].innerHTML;"))
	# 		time.sleep(1)
	# 		#driver.execute_script(("document.getElementsByTagName('head')[0].innerHTML('<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>');"))
	# 		#driver.execute_script(("'<blackblock>'+document.getElementsByTagName('head')[0].innerHTML+'</blackblock>';"))
	# 		driver.execute_script(("document.getElementsByTagName('head')[0].remove();"))
	# #		time.sleep(1)
	# #		driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
	# 		time.sleep(1)
	# 		driver.execute_script(("document.body.insertAdjacentHTML('beforeend', ooo);"))
	# 		driver.execute_script(("document.getElementsByTagName('title')[0].remove();"))
	# 		driver.execute_script(("document.getElementsByClassName('left')[0].remove();"))
	# 		time.sleep(1)
	# 		driver.execute_script(("document.getElementsByClassName('ee340b')[0].remove();"))


#			wait_orders.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='bid-ask-item']")))
# 		print('Continue? (y/n)')
# 		stop_go = input()
# #		date_end = datetime.now()
# 		if 'n' in stop_go:
# 			quit()
		time.sleep(float(config['BUY']['error_pause']))
		teleg.send_info('Продолжаем выполнение скрипта')
		pass

