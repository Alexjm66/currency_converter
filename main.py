import requests
from tkinter import *

response=requests.get("https://v6.exchangerate-api.com/v6/766d3191664b8a0cf66adbe8/latest/USD")
responsej = response.json()

rates=responsej["conversion_rates"]
print(rates)

root=Tk()
root.title("")
root.geometry("500x500")

def convert():
    num = float(amount_entry.get())
    print(responsej['conversion_rates'][t1.get(ACTIVE)])
    ans = num*responsej['conversion_rates'][t1.get(ACTIVE)]
    converted_lbl['text'] = ans

def exit():
    root.destroy()

head_lbl=Label(root, text="Currency Converter", font=("Arial", 30, "bold"), bg="blue",fg="red", width=500)
head_lbl.pack()

amount_lbl=Label(root, text="Amount: ",font=("Arial", 15, "bold"))
amount_lbl.place(x = 10, y = 65)

from_currency=Label(root,text="From: ",font=("Arial", 15, "bold"))
from_currency.place(x = 10, y = 120)

from_currency=Label(root, text="US Dollar",font=("Arial", 15, "bold"))
from_currency.place(x = 120, y = 120
                    )
to_currency=Label(root, text="To: ",font=("Arial", 15, "bold"))
to_currency.place(x = 10, y = 160)

t1 = Listbox(root, width=10)
for i in rates.keys():
    t1.insert(END, str(i))
t1.place(x = 120,y=160)

amount_entry=Entry(root)
amount_entry.place(x = 120, y = 65)

convert_btn=Button(root, text="Convert",font=("Arial", 15, "bold"),command=convert)
convert_btn.place(x = 10,y = 360)

converted_amnt=Label(root, text="Converted Amount",font=("Arial", 20, "bold"))
converted_amnt.place(x = 10, y = 420)

converted_lbl=Label(root,text="",font=("Arial", 20, "bold"))
converted_lbl.place(x=300,y=420)

exit_btn=Button(root,text="Exit",font=("Arial", 15, "bold"),command=exit)
exit_btn.place(x=10, y = 455)
root.mainloop()




