

class CaesarDecoder:
	""" Decode string by shifting each ascii code back by the
	number of input by user """
	lower = (97, 123)
	capital = (65, 91)
		
	def string_to_ascii(string):
		"""convert string to ascii and append to origin_asciis"""
		return [ord(s) for s in string]


	def get_shifted_number_for_char(ascii, number):
		shifted_ascii = ascii - number

		# Run through validations
		if shifted_ascii < CaesarDecoder.capital[0]:
			shifted_ascii =  CaesarDecoder.capital[1] - (ascii - CaesarDecoder.capital[0])

		elif shifted_ascii < CaesarDecoder.lower[0] and shifted_ascii > CaesarDecoder.capital[1]:
			shifted_ascii =  CaesarDecoder.lower[1] - (ascii - CaesarDecoder.lower[0])

		return shifted_ascii


	def shift_numbers(origin_asciis, number):
		shifted_numbers = []

		for ascii in origin_asciis:
			if chr(ascii).isalpha():
				# Get the shifted ascii number
				new_ord_num = CaesarDecoder.get_shifted_number_for_char(ascii, number)
			else:
				new_ord_num = ascii

			shifted_numbers.append(new_ord_num)

		return shifted_numbers


	def convert_ordinals_to_characters(ordinals):
		return ("".join([chr(i) for i in ordinals]))


	def encode(input_string, number):
		"""Encode the input_string based on the provided number"""

		# Get the ordinals for each character
		ordinal_list = CaesarDecoder.string_to_ascii(input_string)

		# shift the ordinals as per the caesar algorithm
		shifted = CaesarDecoder.shift_numbers(ordinal_list, number)

		# Convert ordinal list back to string
		return CaesarDecoder.convert_ordinals_to_characters(shifted)



assert CaesarDecoder.string_to_ascii("CDE") == [67, 68, 69]
assert CaesarDecoder.string_to_ascii("cde") == [99, 100, 101]

assert CaesarDecoder.shift_numbers([67, 68, 69], 2) == [65, 66, 67]
assert CaesarDecoder.shift_numbers([99, 100, 101], 2) == [97, 98, 99]


assert CaesarDecoder.encode('cde', 2) == 'abc', 'cde - 2 should be abc'


# assert convert_list_to_string('CDE', 2) == 'ABC', 'CDE - 2 should be ABC'
# assert convert_list_to_string('XYZ', 1) == 'WXY', 'XYZ - 1 should be WXY'
# assert convert_list_to_string('ABC', 1) == 'ZAB', 'ABC - 1 should be ZAB'
# assert convert_list_to_string('bgu cpf pq', 2) == 'yes and no', 'bgu cpf pq should be yes and no'
# assert convert_list_to_string('c vq C', 2) == 'a to Z', 'c vq C -2 should be a to Z'




