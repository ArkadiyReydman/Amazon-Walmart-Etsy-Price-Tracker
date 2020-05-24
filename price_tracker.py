#Amazon, Walmart, & Etsy Price Tracker
#Author: Arkadiy Reydman
#Year: May 2020

import requests, time, smtplib, os, sys
from bs4 import BeautifulSoup
from tkinter import *


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

#Amazon Main Function
def amazon_main():
    URL = amazon_URL.get()
    sel_price = float(amazon_sel_price.get())
    email = amazon_email.get()
    amazon_password.get()
    time_Checker = amazon_time.get(ACTIVE)
    if time_Checker == '30 seconds':
        time_Checker = 30
    elif time_Checker == '1 minute':
        time_Checker = 60
    elif time_Checker == '10 minutes':
        time_Checker = 600
    elif time_Checker == '30 minutes':
        time_Checker = 1800
    elif time_Checker == '1 hour':
        time_Checker = 3600
    elif time_Checker == '12 hours':
        time_Checker = 43200
    elif time_Checker == '1 day':
        time_Checker = 86400
    else:
        time_Checker = 3600

    #Make Labels and Buttons Dissapear
    amazon_URL_Label.pack_forget()
    amazon_URL.pack_forget()
    amazon_sel_price_label.pack_forget()
    amazon_sel_price.pack_forget()
    amazon_email_label.pack_forget()
    amazon_email.pack_forget()
    amazon_password_label.pack_forget()
    amazon_password.pack_forget()
    amazon_time_label.pack_forget()
    amazon_time.pack_forget()
    amazon_Submit_Button.pack_forget()

    page = requests.get(URL, headers=headers)
    #Parse Page
    soup1 = BeautifulSoup(page.content, 'html.parser')
    #Parse Page twice because of javascript
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    #Finds Name of Product on Page
    title = soup2.find(id="productTitle").get_text().strip()
    #Finds the price of the Product on Page and converts it from string to number
    try:
        price = soup2.find(id="priceblock_ourprice").get_text()
    except:
        #Accounts for amazon products with deals
        price = soup2.find(id="priceblock_dealprice").get_text()
    converted_price = price[1:-3]
    for r in (("-",""), ("$",""), (" ",""),("-","")):
        converted_price = converted_price.replace(*r)
    converted_price = float(converted_price)


    def check_price():
        if converted_price <= sel_price:
            send_mail()
            #Loops in tkinter
            root.after(int(time_Checker*1000), check_price)
        else:
            text = title + ' is not equal to or below ' + str(sel_price)
            nochange_Label = Label(root, text=text)
            nochange_Label.pack()
            #Loops in tkinter
            root.after(int(time_Checker*1000), check_price)

    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(email, 'lahlsqplcvzgytod')

        subject = title + 'price has dropped to ' + price + '!'
        body = '\nCheck out the amazon link: ' + URL

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            email,
            email,
            msg
        )

        trigger_Label = Label(root, text='An email has been sent!', fg='green')
        trigger_Label.pack()


        server.quit()

    #Creates ScrollBar
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill= Y)
    check_price()

#Amazon Click Function
def amazon_Click():
    amazon_Button.pack_forget()
    walmart_Button.pack_forget()
    etsy_Button.pack_forget()
    try:
        global amazon_URL_Label
        amazon_URL_Label = Label(root, text='Enter an Amazon link:')
        amazon_URL_Label.pack()
        global amazon_URL
        amazon_URL= Entry(root, width=50)
        amazon_URL.pack()
        global amazon_sel_price_label
        amazon_sel_price_label = Label(root, text='Enter a trigger price for the email:')
        amazon_sel_price_label.pack()
        global amazon_sel_price
        amazon_sel_price = (Entry(root, width=5))
        amazon_sel_price.pack()
        global amazon_email_label
        amazon_email_label = Label(root, text='Enter your email:')
        amazon_email_label.pack()
        global amazon_email
        amazon_email = Entry(root, width=30)
        amazon_email.pack()
        global amazon_password_label
        amazon_password_label = Label(root, text='Enter your email password')
        amazon_password_label.pack()
        global amazon_password
        amazon_password = Entry(root, width=30)
        amazon_password.pack()
        global amazon_time_label
        amazon_time_label = Label(root, text='Select the time interval to check the price:')
        amazon_time_label.pack()
        global amazon_time
        amazon_time = Listbox()
        amazon_time.insert(1, '30 seconds')
        amazon_time.insert(2, '1 minute')
        amazon_time.insert(3, '10 minutes')
        amazon_time.insert(4, '30 minutes')
        amazon_time.insert(5, '1 hour')
        amazon_time.insert(6, '12 hours')
        amazon_time.insert(7, '1 day')
        amazon_time.pack()
        #submit button - add command to button later:
        global amazon_Submit_Button
        amazon_Submit_Button = Button(root, text='Submit', width=30, activebackground='white', command=amazon_main)
        amazon_Submit_Button.pack()
    except ValueError:
        valueerror_label = Label(root, text='ValueError was raised')
        valueerror_label.pack()
    except:
        error_label = Label(root, text='Error try again')
        error_label.pack()

#Walmart Main Function
def walmart_main():
    URL = walmart_URL.get()
    sel_price = float(walmart_sel_price.get())
    email = walmart_email.get()
    walmart_password.get()
    time_Checker = walmart_time.get(ACTIVE)
    if time_Checker == '30 seconds':
        time_Checker = 30
    elif time_Checker == '1 minute':
        time_Checker = 60
    elif time_Checker == '10 minutes':
        time_Checker = 600
    elif time_Checker == '30 minutes':
        time_Checker = 1800
    elif time_Checker == '1 hour':
        time_Checker = 3600
    elif time_Checker == '12 hours':
        time_Checker = 43200
    elif time_Checker == '1 day':
        time_Checker = 86400
    else:
        time_Checker = 3600

    #Make Labels and Buttons Dissapear
    walmart_URL_Label.pack_forget()
    walmart_URL.pack_forget()
    walmart_sel_price_label.pack_forget()
    walmart_sel_price.pack_forget()
    walmart_email_label.pack_forget()
    walmart_email.pack_forget()
    walmart_password_label.pack_forget()
    walmart_password.pack_forget()
    walmart_time_label.pack_forget()
    walmart_time.pack_forget()
    walmart_Submit_Button.pack_forget()

    page = requests.get(URL, headers=headers)
    #Parse Page
    soup1 = BeautifulSoup(page.content, 'html.parser')
    #Parse Page twice because of javascript
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    #Finds Name of Product on Page
    title = soup2.find('h1', class_='prod-ProductTitle font-normal').get_text().strip()
    #Finds the price of the Product on Page and converts it from string to number
    price = soup2.find(class_='price-characteristic')['content']
    converted_price = price
    for r in (("-",""), ("$",""), (" ",""),("-","")):
        converted_price = converted_price.replace(*r)
    converted_price = float(price)


    def check_price():
        if converted_price <= sel_price:
            send_mail()
            #Loops in tkinter
            root.after(int(time_Checker*1000), check_price)
        else:
            text = title + ' is not equal to or below ' + str(sel_price)
            nochange_Label = Label(root, text=text)
            nochange_Label.pack()
            #Loops in tkinter
            root.after(int(time_Checker*1000), check_price)

    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(email, 'lahlsqplcvzgytod')

        subject = title + 'price has dropped to ' + price + '!'
        body = '\nCheck out the walmart link: ' + URL

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            email,
            email,
            msg
        )

        trigger_Label = Label(root, text='An email has been sent!', fg='green')
        trigger_Label.pack()


        server.quit()

    #Creates ScrollBar
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill= Y)
    check_price()

#Walmart Click Function
def walmart_Click():
    walmart_Button.pack_forget()
    amazon_Button.pack_forget()
    etsy_Button.pack_forget()
    try:
        global walmart_URL_Label
        walmart_URL_Label = Label(root, text='Enter a Walmart link:')
        walmart_URL_Label.pack()
        global walmart_URL
        walmart_URL= Entry(root, width=50)
        walmart_URL.pack()
        global walmart_sel_price_label
        walmart_sel_price_label = Label(root, text='Enter a trigger price for the email:')
        walmart_sel_price_label.pack()
        global walmart_sel_price
        walmart_sel_price = (Entry(root, width=5))
        walmart_sel_price.pack()
        global walmart_email_label
        walmart_email_label = Label(root, text='Enter your email:')
        walmart_email_label.pack()
        global walmart_email
        walmart_email = Entry(root, width=30)
        walmart_email.pack()
        global walmart_password_label
        walmart_password_label = Label(root, text='Enter your email password')
        walmart_password_label.pack()
        global walmart_password
        walmart_password = Entry(root, width=30)
        walmart_password.pack()
        global walmart_time_label
        walmart_time_label = Label(root, text='Select the time interval to check the price:')
        walmart_time_label.pack()
        global walmart_time
        walmart_time = Listbox()
        walmart_time.insert(1, '30 seconds')
        walmart_time.insert(2, '1 minute')
        walmart_time.insert(3, '10 minutes')
        walmart_time.insert(4, '30 minutes')
        walmart_time.insert(5, '1 hour')
        walmart_time.insert(6, '12 hours')
        walmart_time.insert(7, '1 day')
        walmart_time.pack()
        #submit button - add command to button later:
        global walmart_Submit_Button
        walmart_Submit_Button = Button(root, text='Submit', width=30, activebackground='white', command=walmart_main)
        walmart_Submit_Button.pack()
    except ValueError:
        valueerror_label = Label(root, text='ValueError was raised')
        valueerror_label.pack()
    except:
        error_label = Label(root, text='Error try again')
        error_label.pack()

#Etsy Main Function
def etsy_main():
    URL = etsy_URL.get()
    sel_price = float(etsy_sel_price.get())
    email = etsy_email.get()
    etsy_password.get()
    time_Checker = etsy_time.get(ACTIVE)
    if time_Checker == '30 seconds':
        time_Checker = 30
    elif time_Checker == '1 minute':
        time_Checker = 60
    elif time_Checker == '10 minutes':
        time_Checker = 600
    elif time_Checker == '30 minutes':
        time_Checker = 1800
    elif time_Checker == '1 hour':
        time_Checker = 3600
    elif time_Checker == '12 hours':
        time_Checker = 43200
    elif time_Checker == '1 day':
        time_Checker = 86400
    else:
        time_Checker = 3600

    #Make Labels and Buttons Dissapear
    etsy_URL_Label.pack_forget()
    etsy_URL.pack_forget()
    etsy_sel_price_label.pack_forget()
    etsy_sel_price.pack_forget()
    etsy_email_label.pack_forget()
    etsy_email.pack_forget()
    etsy_password_label.pack_forget()
    etsy_password.pack_forget()
    etsy_time_label.pack_forget()
    etsy_time.pack_forget()
    etsy_Submit_Button.pack_forget()

    page = requests.get(URL, headers=headers)
    #Parse Page
    soup1 = BeautifulSoup(page.content, 'html.parser')
    #Parse Page twice because of javascript
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    #Finds Name of Product on Page
    title = soup2.find('h1', class_='wt-text-body-03 wt-line-height-tight wt-break-word wt-mb-xs-1').get_text().strip()
    #Finds the price of the Product on Page and converts it from string to number
    price = soup2.find('h3', class_='wt-text-title-03 wt-mr-xs-2').get_text().strip()
    converted_price = price[1:-3]
    for r in (("-",""), ("$",""), (" ",""),("-",""),('+','')):
        converted_price = converted_price.replace(*r)
    converted_price = float(converted_price)


    def check_price():
        if converted_price <= sel_price:
            send_mail()
            #Loops in tkinter
            root.after(int(time_Checker*1000), check_price)
        else:
            text = title + ' is not equal to or below ' + str(sel_price)
            nochange_Label = Label(root, text=text)
            nochange_Label.pack()
            #Loops in tkinter
            root.after(int(time_Checker*1000), check_price)

    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(email, 'lahlsqplcvzgytod')

        subject = title + 'price has dropped to ' + price + '!'
        body = '\nCheck out the etsy link: ' + URL

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            email,
            email,
            msg
        )

        trigger_Label = Label(root, text='An email has been sent!', fg='green')
        trigger_Label.pack()


        server.quit()

    #Creates ScrollBar
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill= Y)
    check_price()

#Etsy Click Function
def etsy_Click():
    etsy_Button.pack_forget()
    amazon_Button.pack_forget()
    walmart_Button.pack_forget()
    try:
        global etsy_URL_Label
        etsy_URL_Label = Label(root, text='Enter an Etsy link:')
        etsy_URL_Label.pack()
        global etsy_URL
        etsy_URL= Entry(root, width=50)
        etsy_URL.pack()
        global etsy_sel_price_label
        etsy_sel_price_label = Label(root, text='Enter a trigger price for the email:')
        etsy_sel_price_label.pack()
        global etsy_sel_price
        etsy_sel_price = (Entry(root, width=5))
        etsy_sel_price.pack()
        global etsy_email_label
        etsy_email_label = Label(root, text='Enter your email:')
        etsy_email_label.pack()
        global etsy_email
        etsy_email = Entry(root, width=30)
        etsy_email.pack()
        global etsy_password_label
        etsy_password_label = Label(root, text='Enter your email password')
        etsy_password_label.pack()
        global etsy_password
        etsy_password = Entry(root, width=30)
        etsy_password.pack()
        global etsy_time_label
        etsy_time_label = Label(root, text='Select the time interval to check the price:')
        etsy_time_label.pack()
        global etsy_time
        etsy_time = Listbox()
        etsy_time.insert(1, '30 seconds')
        etsy_time.insert(2, '1 minute')
        etsy_time.insert(3, '10 minutes')
        etsy_time.insert(4, '30 minutes')
        etsy_time.insert(5, '1 hour')
        etsy_time.insert(6, '12 hours')
        etsy_time.insert(7, '1 day')
        etsy_time.pack()
        #submit button - add command to button later:
        global etsy_Submit_Button
        etsy_Submit_Button = Button(root, text='Submit', width=30, activebackground='white', command=etsy_main)
        etsy_Submit_Button.pack()
    except ValueError:
        valueerror_label = Label(root, text='ValueError was raised')
        valueerror_label.pack()
    except:
        error_label = Label(root, text='Error try again')
        error_label.pack()

#restarts the program:
def restart():
    os.execv(sys.executable, [sys.executable, '"' + sys.argv[0] + '"'] + sys.argv[1:])


#Main window screen
root = Tk(screenName=None,  baseName=None,  className=' Product Price Tracker',  useTk=1)
header = Label(root, text="PRODUCT PRICE TRACKER", font='Helvetica 18 bold', pady=20)
header.pack()
#Amazon Button
amazon_Button = Button(root, text='Amazon', width=30, activebackground='white', bg='yellow', font='Helvetica 12 bold', command=amazon_Click)
amazon_Button.pack()
#Walmart Button
walmart_Button = Button(root, text='Walmart', width=30, activebackground='white', bg='light blue', font='Helvetica 12 bold', command=walmart_Click)
walmart_Button.pack()
#Etsy Button
etsy_Button = Button(root, text='Etsy', width=30, activebackground='white', bg='orange', font='Helvetica 12 bold', command=etsy_Click)
etsy_Button.pack()
#Restart Button:
restart_Button = Button(root,text='Restart', width=10, activebackground='white', bg='red', command=restart)
restart_Button.pack()
root.wm_geometry("800x800")
root.mainloop()
