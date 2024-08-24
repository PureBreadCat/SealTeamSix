from tkinter import *

root = Tk()
cookiesClicked=2
cookieMonster = PhotoImage(file = "CookieMonster.gif")

def cookieClick():
    global cookiesClicked
    cookiesClicked += 1
    print(cookiesClicked)
    welcomeText = Label(root, text="Cookie Count: "+str(cookiesClicked)).grid(row=1)




    
def main():
    global cookiesClicked

    
    welcomeText = Label(root, text="Cookie Count: "+str(cookiesClicked)).grid(row=1)
    print(type(welcomeText))
    Cookie = Button(root, text = "clicker",width=250,command=cookieClick,image= cookieMonster).grid(row=2)
    
    
    
    root.mainloop()
    
    
    
    



if __name__ == '__main__':
    main()