import tkinter as tk
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php'
r = requests.get(url)
html_code = bs(r.content)

span = html_code.select('span.gld13 span.gld13 a')

company_name = [i.get_text() for i in span]

h = html_code.find_all('td',attrs={'width':75})
high = [i.get_text() for i in h]

l = html_code.find_all('td',attrs={'width':80})
low = [i.get_text() for i in l[0::2]]

prvious_close = [i.get_text() for i in l[1::2]]

lst = html_code.find_all('td',attrs={'width':85})
last_price = [i.get_text() for i in lst]

def stock_window():
	
	root = tk.Tk()
	root.geometry('1000x1000')
	root.title('Stock Top Gainers By Nse')

	l = tk.Label(root,text='Company Name',font=('Bold'),padx=30)
	l1 = tk.Label(root,text='High',font=('Bold'),padx=30)
	l2 = tk.Label(root,text='Low',font=('Bold'),padx=30)
	l3 = tk.Label(root,text='Last Price',font=('Bold'),padx=30)
	l4 = tk.Label(root,text='Previous Close',font=('Bold'),padx=30)

	l.grid(row=0,column=0)
	l1.grid(row=0,column=2)
	l2.grid(row=0,column=4)
	l3.grid(row=0,column=6)
	l4.grid(row=0,column=8)
	for i in company_name:
		clabel = tk.Label(root,text=i,font=('Bold'))
		clabel.grid(row=company_name.index(i)+1,column=0)
		line_label = tk.Label(root,text='|')
		line_label.grid(row=company_name.index(i)+1,column=1)

	for i in high:
		clabel = tk.Label(root,text=i,font=('Bold'))
		clabel.grid(row=high.index(i)+1,column=2)
		line_label = tk.Label(root,text='|')
		line_label.grid(row=high.index(i)+1,column=3)

	for i in low:
		clabel = tk.Label(root,text=i,font=('Bold'))
		clabel.grid(row=low.index(i)+1,column=4)
		line_label = tk.Label(root,text='|')
		line_label.grid(row=low.index(i)+1,column=5)

	for i in last_price:
		clabel = tk.Label(root,text=i,font=('Bold'))
		clabel.grid(row=last_price.index(i)+1,column=6)
		line_label = tk.Label(root,text='|')
		line_label.grid(row=last_price.index(i)+1,column=7)

	for i in prvious_close:
		clabel = tk.Label(root,text=i,font=('Bold'))
		clabel.grid(row=prvious_close.index(i)+1,column=8)
		line_label = tk.Label(root,text='|')
		line_label.grid(row=prvious_close.index(i)+1,column=9)
	root.mainloop()
stock_window()