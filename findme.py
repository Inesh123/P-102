import re
import string
def count_me():
	freq = {}
	file_obj = open('count.txt', 'r')
	word_content = file_obj.read().lower() 
	reg_exp = re.findall(r'\b[a-z]{3,15}\b', word_content)
	for word in reg_exp:
		count = freq.get(word, 0) 
		freq[word] = count + 1 
	freq_list = freq.keys()
	for word in freq_list:
		print word, freq[word]
if __name__ == '__main__':
	count_me()
