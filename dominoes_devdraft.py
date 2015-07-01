def main():

	lenghtOfNumberLine = int(input())

	if lenghtOfNumberLine >= 0 and lenghtOfNumberLine <= 100:
		gameTable = [int(x) for x in input().split()]

		printList(cascade(gameTable))

		gameTable.reverse()

		value = cascade(gameTable)

		value.reverse()

		printList(value)

	else:
		print("error")	

def cascade(dominoes):

	newlist = []
	for i, value in enumerate(dominoes):

		length = value
		subset = dominoes[i + 1 :len(dominoes)]

		for domino in subset:
			if length <= 0: 
				break
			elif domino >= length:
				value += domino - length + 1
				length = domino
			else:
				length -= 1

		newlist.append(value)

	return newlist

def printList(list):

	for i, value in enumerate(list):
		print(value, end="")
		if i == len(list) - 1:
			pass
		else:
			print(" ", end="")
	print("")


if __name__ == '__main__':
	main()