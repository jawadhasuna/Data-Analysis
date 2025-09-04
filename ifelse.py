today = input("Enter the day of the week: ").strip().capitalize()

if today == "Monday":
    print("Today is Monday, the day of the moon.")
elif today == "Tuesday":
    print("Today is Tuesday, the day of Tyr, the god of war.")
elif today == "Wednesday":
    print("Today is Wednesday, the day of Odin, the supreme deity.")
elif today == "Thursday":
    print("Today is Thursday, the day of Thor, the god of thunder.")
elif today == "Friday":
    print("Today is Friday, the day of Frigga, the goddess of beauty.")
elif today == "Saturday":
    print("Today is Saturday, the day of Saturn, the god of fun and feasting.")
elif today == "Sunday":
    print("Today is Sunday, the day of the sun.")
else:
    print("Invalid day entered.")
