# take out the price of the books
# link the price to their respective book names
# sorting the price
# writing the sorted list into a new file
import csv

filename = "BestSelfHelpBooks.csv"
save_list = {}
price_list = []

# opening the original csv file and,
# 1) link the prices with their respective books into a dict for future use
# 2) remove the "$" sign from the prices and append all of them into a list before sorting them
#    in ascending order
with open(filename) as book_list:
    next(book_list)
    reader = csv.reader(book_list)

    # apparently there is a book with "Free App" as its price, so its price is 0
    for line in reader:
        try:
            price = float(line[1].replace("$", ""))
        except ValueError:
            price = 0

        price_list.append(price)
        save_list[price] = line

    price_list.sort()

# opening a new csv file in writing mode and
# write the sorted version of list into the file
with open("CheapestSelfHelpBook.csv", "w", newline="") as new_file:
    headers = ["Book name", "Prices", "Audio Book Availability"]
    writer = csv.writer(new_file)
    writer.writerow(headers)

    for price in price_list:
        current_cheapest_book = save_list[price]
        writer.writerow(current_cheapest_book)
