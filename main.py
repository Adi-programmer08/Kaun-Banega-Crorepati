import random
import time

def lineprint():
    for i in range(145):
        print('*', end="")
        time.sleep(0)

def line2print():
    for i in range(145):
        print('-', end="")
        time.sleep(0)


print("\n\t\t\t\tWelcome to the game : KAUN BANEGA CROREPATI")
lineprint()

pn = input('\n\nEnter your name : ')
lineprint()

print("\n\nLet's start the game.")
time.sleep(1)

questions = ["Who is the prime minister of INDIA ?", "Who is the Indian CEO of Google ?", "When India won its first cricket world cup ?","Who is the Cheif minister of Maharashtra ?", "Which batsman has scored most runs in IPL ? ", "What colour did Lord Shiva’s throat turn into when he drank the deadly poison during Samudra Manthan?", " What is the profession of Kabir in the film Kabir Singh?", "Which state is the largest producer of sugarcane in India?", "Which of these colors when mixed with red will produce the color orange?", "Who of the following personalities is not married to a sports person?", "Which part of the plant absorbs water and nutrients from the soil?", "For which of those groups has MS Dhoni performed two seasons in IPL?", "What is the shape of the cells in a honeycomb made by bees?", "In which state is this mountain peak located?", "Which of these mobile games might require the player to walk around in the real go?", " Which YouTuber star’s real name is Ajey Nagar?", "Which of these is an international football tournament?", "Which ingredient is mixed in milk is a popular home remedy for healing any internal injury?", "Who is this tech entrepreneur and CEO of the electric vehicle company, Tesla?", "The language of Lakshadweep. a Union Territory of India, is _______"]

answers = ["Narendra Modi","Sundar Pichai","In 1983","Eknath Shinde","Virat Kohli", "Blue", "Doctor", "Uttar Pradesh", "Yellow", "Mahesh Bhupathi", "Root", "Rising Pune Supergiants", "Hexagon", "Uttarakhand", "Pokemon Go", "CarryMinati", "FIFA Wrold Cup", "Turmeric", "Elon Musk", "Malayalam"]

wronganswers = [["Eknath Shinde","Yogi Aditya Nath","Rahul Gandhi"],["Bill Gates","Ratan Tata","Nita Ambani"], ["In 2011","In 2013","In 1980"], ["Devendra Phadnavis","Uddhav Thakare","Raj Thakare"], ["Jos Buttler","Mahendra Singh Dhoni","Sachin Tendulkar"], ["Red", "Yellow", "Black"], ["Engineer","Cricketor","Athelete"], ["Maharashtra", "Karnataka", "Madhya Pradesh"], ["Violet", "Green", "Orange"], ["Anushka Sharma", "Sakshi Singh Bagwat","Sharmila Tagore"], ["Stem", "Buds", "Leafs"], ["Chennai Super Kings", "Deccan Chargers", "Gujarat Lions"], ["Octagon", "Square", "Oval"], ["Himachal Pradesh", "Maharshtra", "Tamil Nadu"], ["Gangsters Theft Auto", "PUBG", "Warrior"], ["Mostly Sane", "Flying Beast", "TechnoGuruji"], ["ICC T20 World cup", "NBA Cup International", "IFL"], ["Lemon", "Honey", "Almond"], ["Jack Dorsey", "Drew Houston", "Brain Chesky"], ["Tamil", "Hindi", "Telegu"]]

askedquestions = []
count = 1
amount = 0

while True: 
    while True:
        selectquestion = random.choice(questions)
        if selectquestion in askedquestions:
            pass
        elif selectquestion not in askedquestions:
            askedquestions.append(selectquestion)
            questionindex = questions.index(selectquestion)
            correctanswer = answers[questionindex]
            break

    optionlist = []
    inoptionlist = []
    optioncount = 1
    
    while optioncount < 4:
        optionselect = random.choice(wronganswers[questionindex])
        if optionselect in inoptionlist:
            pass
        elif optionselect not in inoptionlist:
            optionlist.append(optionselect)
            inoptionlist.append(optionselect)
            optioncount = optioncount + 1

    optionlist.append(correctanswer)
    displayed = []
    optiondisplay = []

    a1 = True

    while a1:
        a = random.choice(optionlist)
        if a in displayed:
            pass
        elif a not in displayed:
            displayed.append(a)
            optiondisplay.append(a)
            a1 = not True

    a1 = True

    while a1:
        b = random.choice(optionlist)
        if b in displayed:
            pass
        elif b not in displayed:
            displayed.append(b)
            optiondisplay.append(b)
            a1 = not True

    a1 = True

    while a1:
        c = random.choice(optionlist)
        if c in displayed:
            pass
        elif c not in displayed:
            displayed.append(c)
            optiondisplay.append(c)
            a1 = not True

    a1 = True

    while a1:
        d = random.choice(optionlist)
        if d in displayed:
            pass
        elif d not in displayed:
            displayed.append(d)
            optiondisplay.append(d)
            a1 = not True
    
    matchanswer = ""
    if correctanswer == a:
        matchanswer="a"
    elif correctanswer == b:
        matchanswer= "b"
    elif correctanswer == c:
        matchanswer = "c"
    elif correctanswer == d:
        matchanswer = "d"

    line2print()
    print('\nAmount won = ', amount, '\n')
    line2print()
    time.sleep(1)

    print('\nQuestion number ', count, 'on your screen.')
    print('\nQuestion - ', selectquestion)


    print('\n\tA. ',a)
    time.sleep(1)
    print('\tB. ',b)
    time.sleep(1)
    print('\tC. ',c)
    time.sleep(1)
    print('\tD. ',d)
    time.sleep(1)

    useranswer = input("\nPress the correct option and press Enter  or  Press Q and Enter for Quit the game. -  ").lower()

    if useranswer == matchanswer:
        if count == 1:
            amount = 1000
        elif count == 2:
            amount = 2000
        elif count == 3:
            amount = 3000
        elif count == 4:
            amount = 5000
        elif count == 5:
            amount = 10000
        elif count == 6:
            amount = 20000
        elif count == 7:
            amount = 40000
        elif count == 8:
            amount = 80000
        elif count == 9:
            amount = 160000
        elif count == 10:
            amount = 320000
        elif count == 11:
            amount = 640000
        elif count == 12:
            amount = 1250000
        elif count == 13:
            amount = 2500000
        elif count == 14:
            amount = 5000000
        elif count == 15:
            amount = 10000000
            print('\n\n\n\n\n\n')
            lineprint()
            print('\n\t\t\t\t\tCONGRATULATIONS!')
            print('\t\t\t\t\tYOU WON THE KBC GAME.\n')
            line2print()
            print('\nYou won amount RS. ',amount)
            break

        print('\n\t\t\t\tRight Answer.')
        count = count + 1

    elif useranswer == 'q':
        print('\n')
        lineprint()
        print('\nYOU WON AMOUNT RS. ',amount)
        break

    elif useranswer != matchanswer:
        if amount < 320000 and amount >= 10000:
            print('\nWRONG ANSWER.\n')
            lineprint()
            print('\nYOU WON AMOUNT RS. 10000','\n')
            lineprint()
            break
        else:
            print('\nWRONG ANSWER.\n')
            lineprint()
            print('\nYOU WON AMOUNT RS. ',amount,'\n')
            lineprint()
            break
