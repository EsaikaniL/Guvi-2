amt=int(input("Enter Amount:"))
inter=int(input("Enter interest:"))
period=int(input("Enter Time(Month):"))
totamt=amt*(inter/100)*period
print("Total amount is:",round(totamt))
