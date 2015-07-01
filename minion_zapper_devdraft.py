

def main():

	numMinions, spellDamage, attenuation = [int(x) for x in input().split()]

	minions = [int(x) for x in input().split()]
	minions.sort(reverse = True)
	deathcount = 0

	for x in minions:
		if spellDamage <= 0: 
			break
			
		print("minion health is {}".format(x))
		print("current spell damage is {}".format(spellDamage))

		if spellDamage >= x:
			deathcount += 1
			spellDamage -= attenuation
			print("ZZap minion Death")

	print(deathcount)

if __name__ == '__main__':
	main()