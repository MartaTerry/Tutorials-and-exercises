guests = ["Peter", "Mary", "Ann"]

for guest in guests:
	print("Shall we dine, ",guest, "?")
	
print("Oh, ", guests[2], "will not be able to come!")

del guests[2]
guests.append("Sam")
print(guests)

for guest in guests:
	print("Shall we dine, ",guest, "?")
