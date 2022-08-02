import logging

logging.basicConfig(level=logging.DEBUG)
print("Witaj w kalkulatorze!")
def calculate():
    operation=input("Oto działania jakie możesz wykonać: 1.Dodawanie, 2.Odejmowanie, 3.Mnożenie, 4.Dzielenie:")
    x=float(input("Podaj pierwszą liczbę:"))
    y=float(input("Podaj drugą liczbę:"))
    if operation=="1":
        logging.info("Dodaję %s i %s." %(x,y))
        print("Wynik to:")
        print(x+y)
    elif operation=="2":
        logging.info("Odejmuję %s i %s." %(x,y))
        print("Wynik to:")
        print(x-y)
    elif operation=="3":
        logging.info("Mnożę %s i %s." %(x,y))
        print("Wynik to:")
        print(x*y)
    elif operation=="4":
        logging.info("Dzielę %s i %s." %(x,y))
        print("Wynik to:")
        print(x/y)
    else:
        logging.info("Podałeś/aś złą wartość!")
calculate()




    
    
    

