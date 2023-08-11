#Activity Write program to ask students their mental healt
#prompt students on a scale of 1 to 10 to rate thier mental healh

Emotion = {
    1 : "Seems your in a great mood so spend the Love to others",
    2: "Seems  your going to enjoy your day with a loved one",
    3: "Seems Your just about to make someone very happy",
    4: "Seems your not in a bad place, and thats good",
    5: "Seems your just average in the center of all your emotions, Namastte",
    6: "Seems your know what not right about you, so please fix it",
    7: "Seems your going through some issues but all with be okay",
    8: "Seems your tired please get some rest",
    9: "Seems your not feeling yor usaully self, go see a friend",
    10: "Seems your having a very bad day, So sing the happy song to make you fell better"
}

emotion = int(input("On a Scale of 1-10, How would you rate your day: \n" ))
try:
    if emotion in Emotion:
        print(Emotion[emotion])
finally:
    print("Thats how you are feeling")