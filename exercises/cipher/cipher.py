




def decode_caesar(string, number):
	""" create Caesar cipher """


	asciis = []
	asciisnum = []

	for s in string:

		ord_num = ord(s)

		# lowercase letters that exceed lower bound wrap to beginning
		if ord_num >= 97 and (ord_num - number) < 97:
			until = ord_num - 97
			after = 122 - until
			new_ord_num = after

		# uppercase letters that exceed lower bound wrap to beginning
		elif ord_num >=65 and (ord_num - number) < 65:
			until = ord_num - 65
			after = 90 -  until
			new_ord_num = after

		# filter out non-alpha characters
		elif  65 < ord_num > 122:
			new_ord_num = ord_num

		else:
			new_ord_num = ord_num - number


		asciis.append(chr(new_ord_num))
		asciisnum.append(new_ord_num)


	print (asciis)
	print (asciisnum)
	return ("".join(asciis))



assert decode_caesar('cde', 2) == 'abc', 'cde - 2 should be abc'
assert decode_caesar('CDE', 2) == 'ABC', 'CDE - 2 should be ABC'
assert decode_caesar('XYZ', 1) == 'WXY', 'XYZ - 1 should be WXY'
assert decode_caesar('ABC', 1) == 'ZAB', 'ABC - 1 should be ZAB'
assert decode_caesar('bgu cpf pq', 2) == 'yes and no', 'bgu cpf pq should be yes and no'
assert decode_caesar('c vq C', 2) == 'a to Z', 'c vq C -2 should be a to Z'








"""
def make_caesar(string, number):
	

	asciis = []
	asciisnum = []

	for s in string:
		print (s)
		ord_num = ord(s)

		if ord_num <=122 and (ord_num + number) > 122:
			until = 122 - ord_num
			after = 97 + number - until
			new_ord_num =  after

		elif ord_num <=90 and (ord_num + number) > 90:
			until = 90 - ord_num
			after = 65 + number - until
			new_ord_num =  after

		elif  65 < ord_num > 122:
			new_ord_num = ord_num

		else:
			new_ord_num = ord_num + number


		asciis.append(chr(new_ord_num))
		asciisnum.append(new_ord_num)


	print (asciis)
	print (asciisnum)




make_caesar('a to Z', 2)
"""


