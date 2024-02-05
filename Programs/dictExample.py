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
        "Currency": "East caribbean dollar"
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
        "Currency": "Australian dollar"
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

for x,y in Country.items():
    if "of" in x or "and" in x:
        print(x)


for country, details in Country.items():
    currency = details.get("Currency", "Currency not available")

    if "dollar" in currency:
        print(country,":", currency)

for i , k in Country.items():
    for z, y in k.items():
        if z=="Capital":
            lettersCount=len(y)
    k.update({"LettersInCapital": lettersCount})
print(Country)