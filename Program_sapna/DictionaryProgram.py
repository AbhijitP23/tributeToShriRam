Country = {
  "India" : {
    "Capital" : "New Delhi",
    "Currency" : "Indian Rupee"
  },
    "Afghanistan":{
        "Capital" : "Kabul",
        "Currency": "Afghani"
    },
    "Albaniya":{
        "Capital": "Tirane",
        "Currency": "Lek"
    },
    "Algeria": {
        "Capital": "Algiers",
        "Currency": "Dinar"
    },
    "Andorra": {
        "Capital": "Andorra la vella",
        "Currency": "Euro"
    },
    "Angola": {
        "Capital": "Luanda",
        "Currency": "New Kwanza"
    },
    "Antigua and Barbuda": {
        "Capital": "Saint John's",
        "Currency": "East caribbean doller"
    },
    "Argentina": {
        "Capital": "Buenos Aires",
        "Currency": "Peso"
    },
    "Armenia": {
        "Capital": "Yerevan",
        "Currency": "Drem"
    },
    "Australia": {
        "Capital": "Canberra",
        "Currency": "Australian doller"
    },
    "Austria": {
        "Capital": "Vienna",
        "Currency": "Euro (formerly schilling)"
    },
    "Republic of the Congo":{
        "Capital":"Brazzaville",
         "Currency": "CFA Franc"
    }
}
print("List of contries and capitals:")
for x, y in Country.items():
    print("Country:", x )
    for m,n in y.items():
        print(m,":",n)

print("\n")
print("country who has doller currency:")
for x, y in Country.items():
    #print("Country:", x )
    for m,n in y.items():
        #print(m,":",n)
        if "doller" in n:
            print(x)


print("\n")
print("Find the word whose has and & of letter:")
for x in Country.keys():
    y=x.lower()
    if "and" in y or "of" in y:
        print(y)

print("\n")
print("Add new key in inner dictionary: ")
for x, y in Country.items():
    for m, n in y.items():
        if(m=="Capital"):
          count = len(n)
    Country[x]["LettersInCapital"] =count

print(Country)




