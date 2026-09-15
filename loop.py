while True:
    name = input("What is your name? (or type 'exit' to quit): ")
    
    if name == "exit":
        break
        
    time = input("Is it morning, afternoon, or evening? ").lower()
    
if time == "morning":
    print("Prayerful morning to " + name + " ! ")
elif time == "afternoon":
    print("Prayerful afternoon to " + name + " ! ")
elif time == "night":
    print("Prayerful night to " + name + " ! ")
else:
    print("Hello " + name + " ! ")
    
    
    