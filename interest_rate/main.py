interest = float(input("Δώσε το επιτόκιο του τραπεζικού λογαριασμού: "))
interest = interest / 100

fund = float(input("Δώσε το ποσό κατάθεσης: "))

fund +=fund * interest

print("Το τελικό ποσό στο τέλος του χρόνου θα είναι: ", fund)