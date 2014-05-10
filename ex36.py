from sys import exit

def fighting_harry_potter():
    print "Okay, good decision."
    print "Now decide on your weapon so you can go kill Harry Potter."
    
    decision = int(raw_input("Choose from weapon 1-10:  "))
    
    if decision <= 5:
        print "You choose a metal based weapon."
        print "You are insane.  Harry is a wizard and you want to kill him with some metal?"
        doomed("Dang!")    
    elif decision >= 6 and decision <= 10:
        print "You are wise to choose magical weapon."
        print "Now you go and cast a spell on him."
        print "Good luck!"
        exit(0)
    else:
        doomed("Oy vey!")
        
def hunting_lord_voldermort():
    print "You thought you can go somewhere happy with a happy dragon huh?"
    print "Well, we are going to hunt for Lord Voldermort"
    print "We must find him"
    alive = True
    
    while True:
        print "Should we use the magical mirror or the funny hat?"
        
        decision = raw_input()
        
        if decision == "magical mirror" and alive:
            print "Lord Voldermort is already dead. Let's go home."
            exit(0)
        elif decision == "magical mirror" and not alive:
            print "Oh no, he saw you."
            doomed("Jesus!")
        elif decision == "funny hat":
            print "Let's forget about Voldermort.  Let's go kill Harry Porter."
            fighting_harry_potter()
        else:
            doomed("Sh*t")
    
    
def doomed(curse_word):
    print curse_word, "You stupid person!  Be vaporized"
    exit(0)
    

def start():
    print """You are entering a dragon dungeon, two dragon awaits you.
Which one do you hop on --  bloody dragon or happy dragon?"""
    decision = raw_input("> ")
    
    if "bloody" in decision:
        fighting_harry_potter()
    elif "happy" in decision:
        hunting_lord_voldermort()
    else:   
        doomed("Urg!")
        
        
    
start()