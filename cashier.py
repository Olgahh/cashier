def main():
	# write code here
	total = 0
	items = []
	item_name = input("Item (enter \"done\" when finished): ")
	while item_name != "done":
		price = float(input("Price: "))
		quantity = int(input("Quantity: "))
		items.append({'name' : item_name, 'price': price, 'quantity': quantity})
		total += price*quantity
		item_name = input("Item (enter \"done\" when finished): ")

	print("\n-------------------")
	print("reciept")
	print("-------------------")

	print(items)
	for item in items:
		print("{} {} {:.3f}KD".format(item['quantity'],item['name'],item['price']*item['quantity']))
		# YAAAAAYYYYY


	print("\n-------------------")
	print("Total Price: {}KD".format(total))


if __name__ == '__main__':
	main()
