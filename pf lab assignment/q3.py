# A:
month = { "jan" : 31 , "feb" : 28 , "march" : 31 , "april" : 30 , "may" : 31 , "june" : 30 , "july" : 31 , "aug" : 31 , "sept" : 30 , "oct" : 31 , "nov" : 30 , "dec" : 31}

mon = input("Enter the month name in short form :- ")
print("Number of days in ",mon,"=",month [ mon ])
#  B:
month = { "jan" : 31 , "feb" : 28 , "march" : 31 , "april" : 30 , "may" : 31 , "june" : 30 , "july" : 31 , "aug" : 31 , "sept" : 30 , "oct" : 31 , "nov" : 30 , "dec" : 31}
keys_in_alphabetic_order = list(month . keys() )
keys_in_alphabetic_order.sort()
print( keys_in_alphabetic_order )
# C
month = { "jan" : 31 , "feb" : 28 , "march" : 31 , "april" : 30 , "may" : 31 , "june" : 30 , "july" : 31 , "aug" : 31 , "sept" : 30 , "oct" : 31 , "nov" : 30 , "dec" : 31}

print( "Month which have 31 days are: ")
for i in month :
    if month [ i ] == 31 :
        print( i )
# D:
month = { "jan" : 31 , "feb" : 28 , "march" : 31 , "april" : 30 , "may" : 31 , "june" : 30 , "july" : 31 , "aug" : 31 , "sept" : 30 , "oct" : 31 , "nov" : 30 , "dec" : 31}

print("Month according to number of days are: ")
print("feb")
for i in month :
    if month [ i ] == 30 :
        print(i)
for i in month :
    if month [ i ] == 31 :
        print(i)