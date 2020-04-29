import pickle
import os

def read_file():
	try:
		with open('contacts', 'rb') as my_file:
			a = pickle.load(my_file)
		with open('Coloumn_size', 'rb') as my_file_2:
			b = pickle.load(my_file_2)
		return (a,b)
	except EOFError:
		my_file.close()
		my_file_2.close()
		return ({},{})

def write_file(main_list):
	global DETAILS
	with open('contacts', 'w+b') as my_file:
		pickle.dump(main_list, my_file)
	with open('Coloumn_size', 'w+b') as my_file_2:
		pickle.dump(DETAILS, my_file_2)

def sort_dict():
	global MAIN_DICT
	global DETAILS
	main_list = []
	for item in MAIN_DICT.values():
		blist = []
		for i in item.values():
			blist.append(i)
		main_list.append(blist)
	main_list.sort(key=lambda x: (x[0], x[1], x[3]))
	MAIN_DICT.clear()
	adict = {}
	h = 1
	for row in main_list:
		bdict = {}
		k = 0
		for key in DETAILS.keys():
			bdict[key] = row[k]
			k+=1
		adict[h] = bdict 
		h+=1
	MAIN_DICT = dict(adict)

def show():
	global MAIN_DICT
	global DETAILS
	if not len(MAIN_DICT.keys()):
		print('Currently, you do not have any conatct details')
	else:
		b = list(DETAILS.keys())
		a = list(DETAILS.values())
		astr = '{:>3} | {:<'+str(a[0])+'}  | {:<'+str(a[1])+'}  | {:<'+str(a[2])+'}  | {:<'+str(a[3])+'}'+'\n'+('-'*120)
		print()
		print(astr.format(' ',b[0], b[1], b[2], b[3]))
		for i, value1 in MAIN_DICT.items():
			alist = list(value1.values())
			print(astr.format(i,alist[0],alist[1],alist[2],alist[3]))
		print()

def add():
	global DETAILS
	global MAIN_DICT
	if len(MAIN_DICT):
		a = list(MAIN_DICT.keys())[-1]
	else:
		a=0
	new_conatct = []
	for i in DETAILS.keys():
		print(i,end=': ')
		new_detail = input()
		if not new_detail: new_detail = 'n/a'
		if DETAILS[i] < len(new_detail):
			DETAILS[i] = len(new_detail)
		new_conatct.append(tuple([i,new_detail]))
	MAIN_DICT[a+1] = dict(new_conatct)
	
	with open('Coloumn_size', 'w+b') as my_file_2:
		pickle.dump(DETAILS, my_file_2)
	sort_dict()
	print("Successfully added!\n")

def delete():
	global MAIN_DICT
	clear()
	show()
	print('!!!Deleting a contact!!!\nTo exit, press Enter')
	delete_contact = int(input('Enter the row number: '))
	if delete_contact:
		del MAIN_DICT[delete_contact]
		print('The contact was deleted successfully')
	else:
		print('You canceled the deleting operation')
	sort_dict()

def search():
	global DETAILS
	k = 1
	search_dict = {}
	for i in DETAILS.keys():
		search_dict[k] = i
		k += 1
	print('How would you like to seach a contact detail?')
	for i, j in search_dict.items():
		print(int(i),': ', j)
	h = int(input('Please enter the number: '))
	print(search_dict[h],": ",end='')
	search_item = search_dict[h] 
	search_value = input()
	search_value = search_value.lower()
	result = []
	for i, j in MAIN_DICT.items():
		string = j[search_item].lower()
		if search_value in string:
			result.append(i)
	b = list(DETAILS.keys())
	a = list(DETAILS.values())
	astr = '{:>3} | {:<'+str(a[0])+'}  | {:<'+str(a[1])+'}  | {:<'+str(a[2])+'}  | {:<'+str(a[3])+'}'+'\n'+('-'*120)
	print()
	print(astr.format(' ',b[0], b[1], b[2], b[3]))
	for i, value1 in MAIN_DICT.items():
		if i in result:
			alist = list(value1.values())
			print(astr.format(i,alist[0],alist[1],alist[2],alist[3]))
	print()

def modify():
	global DETAILS
	global MAIN_DICT
	k = 1
	modify_dict = {}
	for i in DETAILS.keys():
		modify_dict[k] = i
		k += 1
	print('which detail would you like to change?')
	for i, j in modify_dict.items():
		print(i,': ', j)
	h = int(input('Please enter the number: '))
	contact_item = modify_dict[h]
	show()
	contact = int(input('Please enter the row number: '))
	print('Current value: ', MAIN_DICT[contact][contact_item])
	new_detail = input('New value: ')
	if not len(new_detail): new_detail = 'n/a'
	else: MAIN_DICT[contact][contact_item] = new_detail
	if DETAILS[contact_item]<len(new_detail):
		DETAILS[contact_item] = len(new_detail)
	clear()
	print('Contact changed successfully')
	sort_dict()

def save():
	global MAIN_DICT
	global DETAILS
	write_file(MAIN_DICT)
	MAIN_DICT, DETAILS = read_file()
	clear()
	print('Your contact details have been saved successfully')

def clear():
	os.system('cls')


string_choice = '== Show:1 == Add:2 == Delete:3 == Search:4 == Modify:5 == Quit:6 == Save:7 =='
quit = True
MAIN_DICT, DETAILS = read_file()
CHOICES_DICT  = {1:show, 2:add, 3:delete, 4:search, 5:modify, 7:save}

while quit:
	print('\n','\t'*6,'<<<<<C O N T A C T - D E T A I L S - C L I>>>>>')
	print('='*120, '\n',string_choice,'\n','='*120)
	CHOICE = int(input('Select: '))
	if CHOICE == 6:
		quit = False
	elif len(MAIN_DICT.keys()) or CHOICE==2:
		CHOICES_DICT[CHOICE]()
	else:
		print('Currently, you do not have any conact details. Try to add a new contact...')

write_file(MAIN_DICT)


