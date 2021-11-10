from tkinter import *

expression = ''

#Function Memasukkan Angka Dan Simbol
def press(num): 

    global expression 
  
    expression = expression + str(num)
    equation.set(expression) 

#Function Sama Dengan 
def equalpress(): 

    try: 
        global expression 

        total = str(eval(expression)) 
        equation.set(total) 

        expression = '' 

    except: 
        equation.set('Masukkan Angka') 
        expression = '' 

#Function Hapus 
def clear():
    
    global expression 
    expression = '' 
    equation.set('0')

root = Tk()

root.geometry('355x435')
  
root.configure(bg='gray')
  
root.title('Calculator - Michael') 

root.resizable(False,False)
  
button_frame = Frame(root,bg='gray')
button_frame.pack()

equation = StringVar()
equation.set('0')

#Angka dilayar   
expression_field = Entry(button_frame,textvariable=equation,justify='right', font = ('helvetica',20))

#Variable Angka    
button1 = Button(button_frame,font= ('futura',11,'bold'),text=' 1 ',bd=1,relief='ridge',
                 fg='white', bg='gray',command=lambda: press(1), height=3, width=8) 
 
button2 = Button(button_frame,font= ('futura',11,'bold'),text=' 2 ',bd=1,relief='ridge',
                 fg='white', bg='gray',command=lambda: press(2), height=3, width=8) 
  
button3 = Button(button_frame,font= ('futura',11,'bold'),text=' 3 ',bd=1,relief='ridge',
                 fg='white', bg='gray',command=lambda: press(3), height=3, width=8)  
  
button4 = Button(button_frame,font= ('futura',11,'bold'),text=' 4 ',bd=1,relief='ridge',
                 fg='white', bg='gray',command=lambda: press(4), height=3, width=8) 

button5 = Button(button_frame,font= ('futura',11,'bold'),text=' 5 ',bd=1,relief='ridge',
                 fg='white', bg='gray',command=lambda: press(5), height=3, width=8) 
  
button6 = Button(button_frame,font= ('futura',11,'bold'),text=' 6 ',bd=1,relief='ridge',
                 fg='white', bg='gray',command=lambda: press(6), height=3, width=8) 
  
button7 = Button(button_frame,font= ('futura',11,'bold'),text=' 7 ',bd=1,relief='ridge',
                 fg='white', bg='gray',command=lambda: press(7), height=3, width=8) 
  
button8 = Button(button_frame,font= ('futura',11,'bold'),text=' 8 ',bd=1,relief='ridge',
                 fg='white', bg='gray',command=lambda: press(8), height=3, width=8) 
  
button9 = Button(button_frame,font= ('futura',11,'bold'),text=' 9 ',bd=1,relief='ridge',
                 fg='white', bg='gray',command=lambda: press(9), height=3, width=8) 
  
button0 = Button(button_frame,font= ('futura',11,'bold'),text=' 0 ',bd=1,relief='ridge',
                 fg='white', bg='gray',command=lambda: press(0), height=3, width=8) 

plus = Button(button_frame,font= ('futura',11,'bold'),text=' + ',bd=1,relief='ridge',
              fg='white', bg='dimgray',command=lambda: press("+"), height=3, width=8)

minus = Button(button_frame,font= ('futura',11,'bold'),text=' - ',bd=1,relief='ridge',
               fg='white', bg='dimgray',command=lambda: press("-"), height=3, width=8)

multiply = Button(button_frame,font= ('futura',11,'bold'),text=' * ',bd=1,relief='ridge',
                  fg='white', bg='dimgray',command=lambda: press("*"), height=3, width=8)

divide = Button(button_frame,font= ('futura',11,'bold'),text=' / ',bd=1,relief='ridge',
                fg='white', bg='dimgray',command=lambda: press("/"), height=3, width=8) 

decimal= Button(button_frame,font= ('futura',11,'bold'),text='.',bd=1,relief='ridge',
                fg='white', bg='dimgray',command=lambda: press('.'), height=3, width=8) 

clear = Button(button_frame,font= ('futura',11,'bold'),text='C',bd=1,relief='ridge',
               fg='white', bg='dimgray',command=clear, height=3, width=8)  

equal = Button(button_frame,font= ('futura',11,'bold'),text=' = ',bd=1,relief='ridge',
               fg='white', bg='dimgray',command=equalpress,height=3) 

#Layar
expression_field.grid(row=0,column=0,ipadx=8,columnspan = 4,ipady=10,pady=15)

#Button
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
plus.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
minus.grid(row=2, column=3)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
multiply.grid(row=3, column=3)

button0.grid(row=4, column=0)
decimal.grid(row=4, column=1)
clear.grid(row=4, column=2)
divide.grid(row=4, column=3)

equal.grid(row=5, column=0,columnspan = 4,sticky='nsew')

root.mainloop() 