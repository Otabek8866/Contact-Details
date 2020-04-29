import pickle

with open('contacts', 'rb') as my:
 	main_dict = pickle.load(my)

DETAILS = {'Name':14, 'Email':27, 'Mobile-phone':13, 'Address':39}
# atuple = ()
# print(type(atuple))
print(main_dict)
main_list = []
for item in main_dict.values():
	blist = []
	for i in item.values():
		blist.append(i)
	main_list.append(blist)
#main_dict.clear()
h = 1
for row in main_list:
	k = 0
	for key in DETAILS.keys():
		main_dict[h][key] = row[k]
		k+=1
	h+=1
for i in main_dict.values():
	print(i)

# main_list.sort(key=lambda x: (x[0], x[1], x[3]))
# print(len(main_list))
# for i in main_list:
# 	print(i)




# DETAILS = {'Name':14, 'Email':27, 'Mobile-phone':13, 'Address':39}
# with open('coloumn_size', 'wb') as my:
# 	pickle.dump(DETAILS, my)


# a = 'Otabek'
# a = a.lower()
# print('otabek' in a)



# import os
# print('+'*200)s
# a = input()
# print(bool(a))
# if a==2:
# 	os.system('cls')

# import pickle
# with open('contacts', 'rb') as my_file:
# 	adict = pickle.load(my_file)

# print(adict)



# for i in adict.values():
# 	for j in i.values():
# 		a.append(len(j))
# print(a)
# #print('{:<a[0]} hello world {:<a[1]}'.format(1,2))
# astr = '{:<3}{:<'+str(a[0])+'}{:<'+str(a[1])+'}{:<'+str(a[2])+'}{:<'+str(a[3])+'}'
# print(astr)
# print(astr.format(0,1,2,3,4))

# a = [1,23,4,5]
# print('{0} ha sa {1} sackjsan {2}'.format(i for i in a))





# adict = {}
# if adict:
# 	print('empty')
# else:
# 	print('something')



# import pickle

# with open('contacts', 'rb') as my_file:
# 	if my_file: adict = pickle.load(my_file)
# 	print(my_file)
# print(adict)

# atuple = [(1, 'hello'),('2', 'world')]
# adict = dict(atuple)
# print(adict)
# print(list(adict.keys())[-1])
