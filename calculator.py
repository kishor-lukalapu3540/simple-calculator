from tkinter import *

mw = Tk()

mw.title('calculator') #mainwinodw
db = Entry(mw,width=14,font=('Arial',28),justify=RIGHT) # db - display box

#db.grid(row=0,column=0, padx=10, pady=10)
btn_0 = Button(mw, text='0', padx=36, pady=10, font=('Arial',14))
btn_1 = Button(mw, text='1', padx=36, pady=10, font=('Arial',14))
btn_2 = Button(mw, text='2', padx=36, pady=10, font=('Arial',14))
btn_3 = Button(mw, text='3', padx=36, pady=10, font=('Arial',14))
btn_4 = Button(mw, text='4', padx=36, pady=10, font=('Arial',14))
btn_5 = Button(mw, text='5', padx=36, pady=10, font=('Arial',14))
btn_6 = Button(mw, text='6', padx=36, pady=10, font=('Arial',14))
btn_7 = Button(mw, text='7', padx=36, pady=10, font=('Arial',14))
btn_8 = Button(mw, text='8', padx=36, pady=10, font=('Arial',14))
btn_9 = Button(mw, text='9', padx=36, pady=10, font=('Arial',14))

btn_clear = Button(mw, text='clear', padx=70, pady=9, font=('Arial',16))
btn_div = Button(mw, text='/', padx=38, pady=10, font= ('Arial',16))
btn_mul = Button(mw, text='*', padx=38, pady=10, font= ('Arial',16))
btn_sub = Button(mw, text='-', padx=38, pady=10, font= ('Arial',16))
btn_add = Button(mw, text='+', padx=36, pady=10, font= ('Arial',16))
btn_equal = Button(mw, text='=', padx=36, pady=40, font= ('Arial',16))

#showing widgets

btn_equal.grid(row=5, column=2, rowspan=2 , padx=2, pady=2)

btn_div.grid(row=5, column=0, padx=2, pady=2)
btn_mul.grid(row=5, column=1, padx=2, pady=2)
btn_sub.grid(row=6, column=0, padx=2, pady=2)
btn_add.grid(row=6, column=1, padx=2, pady=2)

btn_clear.grid(row=4,column=1, columnspan=2, padx=2, pady=2)

btn_0.grid(row=4, column=0,padx=2,pady=2)

btn_1.grid(row=3, column=0,padx=2,pady=2)
btn_2.grid(row=3, column=1,padx=2,pady=2)
btn_3.grid(row=3, column=2,padx=2,pady=2)

btn_4.grid(row=2, column=0,padx=2,pady=2)
btn_5.grid(row=2, column=1,padx=2,pady=2)
btn_6.grid(row=2, column=2,padx=2,pady=2)

btn_7.grid(row=1, column=0,padx=2,pady=2)
btn_8.grid(row=1, column=1,padx=2,pady=2)
btn_9.grid(row=1, column=2,padx=2,pady=2)

db.grid(row=0, column=0, columnspan= 3, padx=10, pady=10)

mw.mainloop()