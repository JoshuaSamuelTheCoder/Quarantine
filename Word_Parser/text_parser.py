import sys
import os.path


dic = {}
mapping = "mapping"


def grep_mapping(mapping_file):
	if not os.path.exists(mapping_file):
		print("Error: Can't find mapping file, there should be a file called mapping in the folder where the script is located")
		return False

	trigger = False
	with open(mapping_file,'r') as file:

		for line in file:
			trigger_word = ''

			for word in line.split():
				if trigger:
					dic[trigger_word.lower()] = word
					trigger = False
				if type(word) == str:
					trigger = True
					trigger_word = word
	return True

def print_word(input):
	if input.lower() in dic:
		print(input, dic[input.lower()])
	else:
		print(input, "not found in mapping")

if __name__ == "__main__":
	input_file = sys.argv[1]

	if not os.path.exists(input_file):
		print("Error: Can't find input file, check if spelled correctly")

	if grep_mapping(mapping) and os.path.exists(input_file):
		space_word_lst = ["[XXXX:"]
		#add to this list if there is a space between XXXX keyword and id number
		concat_lst = ["xxxx:", "XXXX:", "xxxx=", "XXXX="]
		#add to this list if id number is concatenated with XXXX keyword

		trigger = False
		with open(input_file,'r') as file:

			for line in file:
				trigger_word = ''
				for word in line.split():
					if word[:5] in concat_lst:
						trigger = True
						trigger_word = word
					if trigger:
						if trigger_word in space_word_lst:
							print_word(word[:-1])
						elif trigger_word[:5] in concat_lst:
							print_word(trigger_word[5:15])
						trigger = False
					if word in space_word_lst:
						trigger = True
						trigger_word = word
