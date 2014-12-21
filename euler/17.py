# letters in 1 to 1000

num_to_word_dict = {
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
	100: 'onehundred',
	200: 'twohundred',
	300: 'threehundred',
	400: 'fourhundred',
	500: 'fivehundred',
	600: 'sixhundred',
	700: 'sevenhundred',
	800: 'eighthundred',
	900: 'ninehundred',
	1000: 'onethousand'
}

def num_to_word(num, dictionary):
	if num in dictionary:
		return dictionary[num]
	else:
		if num < 100:
			tens = int(str(num)[0]) * 10
			ones = int(str(num)[1])
			return dictionary[tens] + dictionary[ones]
		else:
			hundreds = int(str(num)[0])
			rem = int(str(num)[1:])
			return '%shundredand%s' % (dictionary[hundreds], num_to_word(rem, num_to_word_dict))

words = []

for i in range(1, 1001):
	words.append(num_to_word(i, num_to_word_dict))

for num in words:
	num.replace(' ', '')

total = 0
for num in words:
	total += len(num)

print words
print total