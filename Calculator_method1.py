### Program for making a Calculator in python by using tkinter/ GUI (Method 1) ###
### PROGRAM MADE BY HEMENDRA NAIDU ###
from tkinter import * # importing all the functions from tkinter(GUI Library)
def click(event): #defining the click function 
    global scvalue #making scvalue variable global so it can be used anywhere 
    text=event.widget.cget("text")
    print(text)
    if text =="=": #if user has pressed = sign they want to get the final calculation
        if scvalue.get().isdigit(): #checking is the value of scavlue is digit
            value=int(scvalue.get())
        else: #is not eval function will help in evalation of an expression 
            value=eval(scvalue.get())
        scvalue.set(value)
        Screen.update()
    elif text=="C":  #Condtion when user has pressed C which is clear button 
        scvalue.set("") #this line will clear the space 
        Screen.update()
    else:
       scvalue.set(scvalue.get()+ text) 
       Screen.update()
        
root =Tk() # creating tkinter window
root.geometry("600x800") #giving root geometry in length and breadth acc. to program
root.title("Calculator (creator: Hemendra Naidu)") #giving title which will appear on top
scvalue= StringVar() #making a variable named scvalue and making it string variable 
scvalue.set("") #and making an empty string 
Screen= Entry(root,textvariable=scvalue,font="Calibri 40 bold") #making an entry visit(where value will be showed after calculation)
Screen.pack(fill=X,ipadx=8,pady=25,padx=10) #packing the widget, internal padding,giving some padding in x and y direction
##we will make one frame at a time and will pack three buttons in it##


f1=Frame(root,bg="grey") #we have made our frame 1, with background grey
b=Button(f1,text="9",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 1
b.pack(side=LEFT, padx=10,pady=5) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 



b=Button(f1,text="8",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 1
b.pack(side=LEFT, padx=10,pady=5)  #packing the button
b.bind("<Button-1>",click) # binding the button with click event 


b=Button(f1,text="7",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 1
b.pack(side=LEFT, padx=10,pady=5) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 
f1.pack() 

f2=Frame(root,bg="grey")#we have made our frame 2, with background grey
b=Button(f2,text="6",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 2
b.pack(side=LEFT, padx=10,pady=5) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 



b=Button(f2,text="5",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 2
b.pack(side=LEFT, padx=10,pady=5)  #packing the button
b.bind("<Button-1>",click) # binding the button with click event 


b=Button(f2,text="4",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 2
b.pack(side=LEFT, padx=10,pady=5) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 
f2.pack() 

f3=Frame(root,bg="grey") #we have made our frame 3, with background grey
b=Button(f3,text="3",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 3
b.pack(side=LEFT, padx=10,pady=5) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 



b=Button(f3,text="2",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 3
b.pack(side=LEFT, padx=10,pady=5)  #packing the button
b.bind("<Button-1>",click) # binding the button with click event 


b=Button(f3,text="1",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 3
b.pack(side=LEFT, padx=10,pady=5) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 
f3.pack() 


f4=Frame(root,bg="grey") #we have made our frame 4, with background grey
b=Button(f4,text="0",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 4
b.pack(side=LEFT, padx=15,pady=10) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 



b=Button(f4,text="-",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 4
b.pack(side=LEFT, padx=10,pady=5)  #packing the button
b.bind("<Button-1>",click) # binding the button with click event 


b=Button(f4,text="*",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 4
b.pack(side=LEFT, padx=10,pady=5) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 
f4.pack() 

f5=Frame(root,bg="grey") #we have made our frame 5, with background grey
b=Button(f5,text="/",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 4
b.pack(side=LEFT, padx=10,pady=5) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 



b=Button(f5,text="%",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 5
b.pack(side=LEFT, padx=10,pady=5)  #packing the button
b.bind("<Button-1>",click) # binding the button with click event 


b=Button(f5,text="=",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 5
b.pack(side=LEFT, padx=10,pady=5) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 
f5.pack() 

f6=Frame(root,bg="grey") #we have made our frame 6, with background grey
b=Button(f6,text="C",padx=20,pady=10,font="Calibri 30 bold") #making our button and putting it inside frame 5
b.pack(side=LEFT, padx=10,pady=5) #packing the button
b.bind("<Button-1>",click) # binding the button with click event 
f6.pack() 



root.mainloop() # this is the main lopp it will execute Tkinter