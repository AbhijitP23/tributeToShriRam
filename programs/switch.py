def get_city_info(city):
    if city == "Ayodhya":
        return ("Ayodhya is where Lord Rama was born and where his 14-year journey in exile began after King Dashratha granted his youngest wife Kekayi her wish and banished Rama to the forest.")
    elif city == "JanakPur":
        return ("Janakpur is the birthplace of goddess Sita as well as the site where she was married to Lord Rama. The legend has it that the King of Janakpur ploughed the land here to get rid of a devastating drought, and it was in the course of the ploughing that he stumbled upon an earthen pot out of which Sita emerged. Thereafter, the place is also known as Sitamarhi.")
    else:
        return "Lord Rama along with his wife Sita and brother Lakshman crossed the river Ganga from here to go beyond their kingdom. The trio spent some time at the Ashram of Sage Bharadwaj here, before travelling ahead."

def main():
    print("Select a city:")
    print("Ayodhya")
    print("JanakPur")
    print("Prayag")

    user_input = input("Enter the city name: ")
    city_info = get_city_info(user_input)

    print("\nCity Information:")
    print(city_info)

    main()

