# **********************************************************************************************************************
# *********************************************THE PETRİKOR PROJECT*****************************************************
# ************************************************BY ONUR CAGLAR********************************************************
# **********************************************************************************************************************
# **********************************************************************************************************************
import math
import random
import time
from cv2 import cv2
import tkinter
from tkinter import *
import re
from tkinter import messagebox
import sys
import webbrowser
import datetime
import smtplib
import urllib3
from email.mime.text import MIMEText
from PIL import ImageTk
# **********************************************************************************************************************
# **********************************************************************************************************************
# *************************************************WELCOME WELCOME******************************************************
# **********************************************************************************************************************
# **********************************************************************************************************************
with open("Archives\end.txt", "r+", encoding="utf-8") as endfile:
    satir = endfile.readlines()
    print(satir)
    satirhatirla = satir[0]
    Rememberdatum1 = satirhatirla.split(":")
    firstlg = Rememberdatum1[0]
    Rememberdatum1 = satirhatirla.split(":")
    Rememberdatum = Rememberdatum1[1]
    Rememberdatum = Rememberdatum.split("}")
    telRemember = Rememberdatum[0]
    passRemember = Rememberdatum[1]
    if firstlg=="False":
        language=False
        Wtext1="Başlatılıyor...Lütfen Bekleyin!"
        Wtext2 = "Versiyon: BETA"
    else:
        language=True
        Wtext1 = "Starting Up...Please Wait!"
        Wtext2 = "Version: BETA"

# """
video= cv2.VideoCapture ("C:\\Users\\asus\\Documents\\Python\\Petrikor\\image\\welcome.mp4")

if not video.isOpened():
    messagebox.showerror("hata", "Video bulunamadı... :(")
while True:
    yakalanan, kare = video.read()
    font= cv2.FONT_HERSHEY_PLAIN
    if language==True:
        Wtext1 = "Please Wait!"
        Wtext2 = "Version:BETA"
        cv2.putText(kare, Wtext1, (225, 245), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(kare, Wtext2, (215, 340), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
    else:
        Wtext1 = "Lutfen Bekleyin!"
        Wtext2 = "Versiyon:BETA"
        cv2.putText(kare, Wtext1, (225, 245), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(kare, Wtext2, (215, 340), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
    if not yakalanan:
        print("video finish...")
        break
    cv2.namedWindow('Petrikor',cv2.WINDOW_FULLSCREEN)
    cv2.moveWindow("Petrikor", 100,100)
    cv2.resizeWindow("Petrikor",640,360)
    cv2.setWindowProperty('Petrikor', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Petrikor',kare)
    if cv2.waitKey(15) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
# **********************************************************************************************************************
# **********************************************************************************************************************
# ********************************************NETWORK CONNECTION CHECK**************************************************
# **********************************************************************************************************************
# **********************************************************************************************************************
def check_internet_conn():
    try:
        http = urllib3.PoolManager(timeout=3.0)
        r = http.request('GET', 'google.com', preload_content=False)
        code = r.status
        r.release_conn()
    except urllib3.exceptions.MaxRetryError as err:
        return False
    if code == 200:
        return True

    else:
        return False
check_network=check_internet_conn()
if check_network==False:
    if language==False:
        messagebox.showerror("hata","Ağ bağlatısı bulunamadı...")
    else:
        messagebox.showerror("Eror", "Your device's network connection was not found...")
    sys.exit()
# **********************************************************************************************************************
# **********************************************************************************************************************
# *************************************************LOGIN SCREEN*********************************************************
# **********************************************************************************************************************
# **********************************************************************************************************************
def remember_me_func():
    global checkkk
    checkkk = 1
    with open("Archives\end.txt", "w", encoding="utf-8") as sonfile:
        sonfile.write("False"+":"+"05*********" + "}" + "********")
def log_out_func():
    if language==True:
        res = messagebox.askquestion("Exit", "do you really want to log out ??")
        if res == 'yes':
            sys.exit()
    else:
        res = messagebox.askquestion("Çıkış", "Gerçekten çıkış yapmak istiyor musunuz???")
        if res == 'yes':
            sys.exit()
def email_time_counter_func(register_window):
    second = StringVar()
    second.set("150")
    secondEntry = Entry(register_window, font=("times", 18, "bold"), textvariable=second, bg="#514c6d")
    secondEntry.place(x=200, y=210, width=100, height=30)
    # secondEntry.config(state="readonly")
    temp = int(second.get())
    while temp > -1:
        second.set("{0}".format(temp))
        register_window.update()
        register_window.update()
        time.sleep(1)
        if temp == 0:
            if language==False:
                messagebox.showinfo("Süre Doldu",
                                "Ne yazıkki kod numrasını girmek için verilen zaman doldu...\nKayıt tamamlandı. Fakat mail doğrulanamadı...")
            else:
                messagebox.showinfo("Time Over","Unfortunately, the time to enter the code number has expired...\nRegistration is complete. But the mail could not be verified...")
            register_window.quit()
            register_window.destroy()
            mail_check= False
            # Buradan sonra SQL dosyasına kayıt edilecek.....
            # Buradan sonra SQL dosyasına kayıt edilecek.....
            # Buradan sonra SQL dosyasına kayıt edilecek.....
            # Buradan sonra SQL dosyasına kayıt edilecek.....
            break
        temp -= 1
def welcome_email_func(names, Umail):
    if language==False:
        body = f"Sayın {names}, Petrikor'a kayıt işlemini başarıyla tamamladınız. Petrikor Projesi'ne hoşgeldiniz birçok özellik ve kullanıcı dostu arayüz tasarımı ile Petrikor uygulaması kullanımıza hazır ve nazırdır. :) Saygılarımızla, Petrikor Projesi Ekibi"
        subject = "PETRİKOR Projesi'ne HOŞGELDİN"
    else:
        body = f"Dear {names}, You have successfully completed the registration to Petrichor. Welcome to the Petrichor Project, with many features and user-friendly interface design, the Petrichor application is ready and available for you. :) Best regards, Petrichor Project Team"
        subject = "Welcome to The PETRICHOR PROJECT"
    # print(body)
    account = "mailgir@gmail.com"
    mailll = smtplib.SMTP("smtp.gmail.com", 587)
    mailll.ehlo()
    mailll.starttls()
    mailll.login("mailgir@gmail.com", "Passwordgir")

    server = MIMEText(body, 'html', 'utf-8')
    server['From'] = account
    server['Subject'] = subject
    server['To'] = ''.join(Umail)
    server = server.as_string()
    mailll.sendmail("mailgir@gmail.com", Umail, server)
def email_send_func(rastgele, Umail, names):
    if language==False:
        body = f"Sayın {names} uygulamaya kayıt işlemini tamamlamak için {Umail} eposta adresinize gönderilen bu mailde sizin için hazırlanan kod: {rastgele} dir.NOT: Bu mailin sizle alakası olmadığını düşünüyorsanız önemsemeyiniz..."
        subject = "Petrikor Projesi Eposta Doğrulama"
    else:
        body = f"Dear {names} e-mail address to complete the registration process is {Umail}. The code prepared for you in this e-mail sent to your  {random}  NOTE: If you think this e-mail has nothing to do with you, ignore it..."
        subject = "The Petrichor Project Email Verification"
    # print(body)
    account = "mailgir@gmail.com"
    mailll = smtplib.SMTP("smtp.gmail.com", 587)
    mailll.ehlo()
    mailll.starttls()
    mailll.login("mailgir@gmail.com", "Passwordgir")

    server = MIMEText(body, 'html', 'utf-8')
    server['From'] = account
    server['Subject'] = subject
    server['To'] = ''.join(Umail)
    server = server.as_string()
    mailll.sendmail("mailgir@gmail.com", Umail, server)
def Register_func():
    def come_back_func():
        if language==False:
            res=messagebox.askquestion("Geri dön","Geri dönmek istediğine emin misin?\nTüm ilerlemen kaybolacak!!!")
            if res == 'yes':
                register_window.quit()
                register_window.destroy()
        else:
            res = messagebox.askquestion("Come back", "Are you sure you want to come back?\nAll your progress will be lost!!!")
            if res == 'yes':
                register_window.quit()
                register_window.destroy()
    def register_contact_information_unit_func(Usave):
        global Umail
        def register_contact_information_check_func():
            global usave
            global Umail
            Uphone=entry_phone.get()
            Umail=entry_mail.get()
            Upassword=entry_password.get()
            Unick=entry_nick.get()
            try:
                Uphone=int(Uphone)
                Umail= str(Umail)
                Unick=str(Unick)
                Upassword=str(Upassword)
            except Exception as ex:
                print("hatalı tuşlama yapıldı.")
                if language==False:
                    messagebox.showerror("Hata","Hatalı tuşlama yapıldı...")
                else:
                    messagebox.showerror("Eror","Eror, You entry wrong a value.")
            if len(str(Uphone)) != 10 or str(Uphone)=="05*********":
                if language != False:
                    messagebox.showerror("Eror", "Incorrect dialing in phone number...")
                else:
                    messagebox.showerror("Hata","Telefon numarasında hatalı tuşlama yapıldı...")
                entry_phone.config(fg="red")
            else:
                if Umail == " " or Umail == "" or len(Umail) < 5:
                    if language != False:
                        messagebox.showerror("Eror", "Email address is too short, please enter a real email... :(")
                    else:
                        messagebox.showerror("hata", "Email adresi çok kısa lütfen gerçek bir mail girin... :(")
                    entry_mail.config(fg="red")
                elif not re.search("@", Umail):
                    if language != False:
                        messagebox.showerror("Eror", "An incorrect or incomplete Email was entered... :(")
                    else:
                        messagebox.showerror("hata", "Yanlış veya eksik bir Email girildi... :(")
                    entry_phone.config(fg="red")
                elif re.search("gamil", Umail) or re.search("outlok", Umail) or re.search("homail", Umail):
                    if language != False:
                        messagebox.showerror("Eror", "An incorrect or incomplete Email was entered... :(")
                    else:
                        messagebox.showerror("hata", "Yanlış veya eksik bir Email girildi... :(")
                    entry_mail.config(fg="red")
                elif not re.search("[.]", Umail):
                    if language != False:
                        messagebox.showerror("Eror", "An incorrect or incomplete Email was entered... :(")
                    else:
                        messagebox.showerror("hata", "Yanlış veya eksik bir Email girildi... :(")
                    entry_mail.config(fg="red")
                elif not re.search("com", Umail):
                    if language != False:
                        messagebox.showerror("Eror", "An incorrect or incomplete Email was entered... :(")
                    else:
                        messagebox.showerror("hata", "Yanlış veya eksik bir Email girildi... :(")
                    entry_mail.config(fg="red")
                elif Unick == "" or len(Unick) < 4:
                    if language != False:
                        messagebox.showerror("Eror",
                                             "Nickname is too short, create a nick of at least 4 digits... :(")
                    else:
                        messagebox.showerror("hata", "Takma ad çok kısa en az 4 haneli bir takma isim bulun... :(")
                    entry_nick.config(fg="red")
                elif Upassword == "" or len(Upassword) < 8 or str(Upassword)=="********":
                    if language != False:
                        messagebox.showerror("Eror", "Password is too short, create a password of at least 8 digits... :(")
                    else:
                        messagebox.showerror("hata", "Parola çok kısa en az 8 haneli bir parola oluşturun... :(")
                    entry_password.config(fg="red")
                elif Unick == "" or len(Unick) > 15:
                    if language != False:
                        messagebox.showerror("Eror",
                                             "Nickname is too long, create a nick of at least 14 digits... :(")
                    else:
                        messagebox.showerror("hata", "Takma ad çok uzun en fazla 14 haneli bir takma isim oluşturabilirsin... :(")
                    entry_nick.config(fg="red")
                elif len(Upassword) > 15:
                    if language != False:
                        messagebox.showerror("Eror", "Password is too long, create a password of at least 14 digits... :(")
                    else:
                        messagebox.showerror("hata", "Parola çok uzun en fazla 14 haneli bir parola oluşturabilirisin... :(")
                    entry_password.config(fg="red")
                # elif SQL SORGU YAPILACAK:
                #     "SQL SORGU YAPILACAK"
                #     "SQL SORGU YAPILACAK"
                #     "SQL SORGU YAPILACAK"
                #     "SQL SORGU YAPILACAK"
                #     "SQL SORGU YAPILACAK"
                #     "SQL SORGU YAPILACAK"
                #     "SQL SORGU YAPILACAK"
                #     "SQL SORGU YAPILACAK"
                else:
                    usave=Usave+" "+str(Uphone)+" "+str(Umail)+" "+str(Unick)+" "+str(Upassword)
                    register_email_verification_unit_func()
        frame_register.configure(bg="#27234c")
        frame_contact=Frame(frame_register,bd=5,bg="#514c6d")
        frame_contact.place(x=10,y=10,width=390, height=240)
        information1 = Label(frame_contact, text="2)İletişim Bilgileri Bölümü", bg="orange", fg="White", font="Times 14 bold")
        information1.place(x=8, y=8, width=375, height=25)
        lbl_phone = Label(frame_contact, text="Telefon No", bg="#514c6d", fg="white", font="times 15 bold")
        lbl_phone.place(x=10, y=50, width=100, height=30)
        lbl_mail = Label(frame_contact, text="Mail Adresi", bg="#514c6d", fg="white", font="times 15 bold")
        lbl_mail.place(x=10, y=100, width=100, height=30)
        lbl_nick = Label(frame_contact, text="Takma Ad", bg="#514c6d", fg="white", font="times 15 bold")
        lbl_nick.place(x=10, y=150, width=100, height=30)
        lbl_password = Label(frame_contact, text="Parola", bg="#514c6d", fg="white", font="times 15 bold")
        lbl_password.place(x=10, y=200, width=100, height=30)
        phone_txt = StringVar(frame_contact)
        phone_txt.set("05*********")
        password_txt = StringVar(frame_contact)
        password_txt.set("********")
        entry_phone = Entry(frame_contact, bg="#27234c", fg="white", font="times 15 bold",textvariable=phone_txt)
        entry_phone.place(x=120, y=50, width=260, height=30)
        entry_mail = Entry(frame_contact, bg="#27234c", fg="white", font="times 13 bold")
        entry_mail.place(x=120, y=100, width=260, height=30)
        entry_nick = Entry(frame_contact, bg="#27234c", fg="white", font="times 14 bold")
        entry_nick.place(x=120, y=150, width=260, height=30)
        entry_password = Entry(frame_contact, bg="#27234c", fg="white", font="times 14 bold",textvariable=password_txt)
        entry_password.place(x=120, y=200, width=260, height=30)
        btn_continue = Button(register_window, text="Email Doğrulamasına Geç", command=register_contact_information_check_func,cursor="hand2", bg="green", fg="white", font="Times 18 bold")
        btn_continue.place(x=30, y=337, width=390, height=50)
        if language == True:
            btn_continue.configure(text="EMAİL VERIFICATION STAGE")
            lbl_phone.configure(text="Phone No")
            lbl_mail.configure(text="Mail adress")
            lbl_nick.configure(text="Nickname")
            lbl_password.configure(text="Password")
    def register_personal_information_unit_func():
        def register_personal_information_check_func():
            global names
            Uname = entry_name.get()
            Usurname = entry_surname.get()
            Udistrict = entry_district.get()
            Ugender = varGender.get()
            Uyear = clicked_year.get()
            Ucity = clicked_city.get()
            Uaddress = entry_address.get()
            Uname = Uname.strip()
            Uname=Uname.upper()
            Usurname = Usurname.strip()
            Usurname=Usurname.upper()
            Udistrict = Udistrict.strip()
            Udistrict = Udistrict.upper()
            print(str(Uname) + str(Usurname) + str(Ugender) + str(Uyear) + str(Ucity) + str(Udistrict) + str(Uaddress))
            try:
                str(Uname)
                str(Usurname)
                Uyear = clicked_year.get()
                str(Ucity)
                str(Udistrict)
                str(Uaddress)
            except Exception as ex:
                if language==False:
                    messagebox.showerror("Hata","Hata Yanlış bir değer girildi.")
                else:
                    messagebox.showerror("Eror", "Eror, You entry wrong a value.")
            if len(Uname) < 3:
                print("İsim eksik yazıldı.... :(")
                entry_name.config(fg="red")
                if language==True:
                    messagebox.showerror("Eror","Name is misspelled")
                else:
                    messagebox.showerror("hata", "İsim eksik yazıldı.... :(")
            elif len(Uname) < 2:
                print("Soyisim eksik yazıldı.... :(")
                entry_surname.config(fg="red")
                if language==True:
                    messagebox.showerror("Eror","Surame is misspelled")
                else:
                    messagebox.showerror("hata", "Soyisim eksik yazıldı.... :(")
            elif re.search("[.,£#${}|*+?!<>'^%&()=_/]", Usurname):
                print("Saçma sapan soyisim yazıyorsun doğru yaz soyadını.... :(")
                entry_surname.config(fg="red")
                if language==True:
                    messagebox.showerror("Eror","You are writing a ridiculous surname, write your name and surname correctly")
                else:
                    messagebox.showerror("hata", "Saçma sapan isim yazıyorsun doğru yaz adını soyadını.... :(")
            elif re.search("[.,£#${}|*+?<>!'^%&()=_/]", Uname):
                print("Saçma sapan isim yazıyosun doğru yaz şu adını.... :(")
                entry_name.config(fg="red")
                if language==True:
                    messagebox.showerror("Eror","You are writing a ridiculous name, write your name and surname correctly")
                else:
                    messagebox.showerror("hata", "Saçma sapan isim yazıyosun doğru yaz adını soydını.... :(")
            elif re.search("[0-9]", Uname):
                print("Saçma sapan sayı yazıyosun doğru yaz şu adını.... :(")
                entry_name.config(fg="red")
                if language==True:
                    messagebox.showerror("Eror","You are writing a ridiculous number, write your name and surname correctly")
                else:
                    messagebox.showerror("hata", "Saçma sapan sayı yazıyosun doğru yaz adını.... :(")
            elif re.search("[0-9]", Usurname):
                entry_surname.config(fg="red")
                print("Saçma sapan sayı yazıyosun doğru yaz şu soydını.... :(")
                if language==True:
                    messagebox.showerror("Eror","You are writing a ridiculous number, write your name and surname correctly")
                else:
                    messagebox.showerror("hata", "Saçma sapan sayı yazıyosun doğru şu soydını.... :(")
            elif Uyear == "":
                if language==True:
                    messagebox.showerror("Eror","No birth year selection has been made :(")
                else:
                    messagebox.showerror("hata", "Herhangi bir doğum yılı seçimi yapılmadı :(")
                drop_year.config(fg="red")
            elif Uyear == "Yıllar" or Uyear=="Years":
                if language==True:
                    messagebox.showerror("Eror","No birth year selection has been made :(")
                else:
                    messagebox.showerror("hata", "Herhangi bir doğum yılı seçimi yapılmadı :(")
                drop_year.config(fg="red")
            elif Ucity == "":
                if language==True:
                    messagebox.showerror("Eror","No city selection has been made :(")
                else:
                    messagebox.showerror("hata", "Herhangi bir şehir seçimi yapılmadı :(")
                drop_city.config(fg="red")
            elif Ucity == "İller" or Uyear=="Cities":
                drop_city.config(fg="red")
                if language==True:
                    messagebox.showerror("Eror","No city selection has been made :(")
                else:
                    messagebox.showerror("hata", "Herhangi bir şehir seçimi yapılmadı :(")
            elif re.search("[.,£#${}|*+?<>!'^%&()=_/]", Udistrict):
                print("Saçma sapan ilçe adı yazıyosun doğru yaz şu adını.... :(")
                entry_district.config(fg="red")
                if language==True:
                    messagebox.showerror("Eror","You are writing a nonsense District name, write your district correctly.... :(")
                else:
                    messagebox.showerror("hata", "Saçma sapan İlçe adı yazıyosun doğru yaz ilçeni.... :(")
            elif re.search("[0-9]", Udistrict):
                print("Saçma sapan sayı yazıyosun doğru yaz şu ilçeni.... :(")
                entry_district.config(fg="red")
                if language==True:
                    messagebox.showerror("Eror","You are writing a nonsense District name, write your district correctly.... :(")
                else:
                    messagebox.showerror("hata", "Saçma sapan İlçe adı yazıyosun doğru yaz ilçeni.... :(")
            elif len(Udistrict) < 2:
                print("İlçe eksik yazıldı.... :(")
                entry_surname.config(fg="red")
                if language==True:
                    messagebox.showerror("Eror","District name is incomplete. :(")
                else:
                    messagebox.showerror("hata", "İlçe adı eksik yazıldı.... :(")
            else:
                names=Uname+" "+Usurname
                Usave=Uname+" "+Usurname+" "+str(Ugender)+" "+Uyear+" "+Ucity+" "+Udistrict+" "+Uaddress
                register_contact_information_unit_func(Usave)

        frame_register.configure(bg="#27234c")
        frame_personal= Frame(frame_register,bd=5,bg="#514c6d")
        frame_personal.place(x=4,y=5,width=397, height=85)
        frame_adress = Frame(frame_register, bd=5, bg="#514c6d")
        frame_adress.place(x=4, y=90, width=397, height=160)
        lbl_name= Label(frame_personal,text="İsim",bg="#514c6d", fg="white", font="times 14 bold")
        lbl_name.place(x=2,y=10,width=50, height=20)
        lbl_surname = Label(frame_personal, text="Soyisim", bg="#514c6d", fg="white", font="times 14 bold")
        lbl_surname.place(x=5, y=50, width=62, height=20)
        lbl_year = Label(frame_personal, text="DoğumYılı", bg="#514c6d", fg="white", font="times 13 bold")
        lbl_year.place(x=200, y=10, width=75, height=20)
        lbl_city = Label(frame_adress, text="Şehir:", bg="#514c6d", fg="white", font="times 14 bold")
        lbl_city.place(x=1, y=15, width=80, height=20)
        lbl_district = Label(frame_adress, text="İlçe:", bg="#514c6d", fg="white", font="times 14 bold")
        lbl_district.place(x=190, y=15, width=60, height=20)
        lbl_address = Label(frame_adress, text="Tam Adres:", bg="#514c6d", fg="white", font="times 14 bold")
        lbl_address.place(x=120, y=55, width=110, height=20)
        entry_name = Entry(frame_personal, bg="#27234c", fg="white", font="times 13 bold")
        entry_name.place(x=70, y=10, width=110, height=20)
        entry_surname = Entry(frame_personal, bg="#27234c", fg="white", font="times 13 bold")
        entry_surname.place(x=70, y=50, width=110, height=20)
        entry_district = Entry(frame_adress, bg="#27234c", fg="white", font="times 13 bold")
        entry_district.place(x=260, y=15, width=120, height=20)
        entry_address = Entry(frame_adress, bg="#27234c", fg="white", font="times 12 bold")
        entry_address.place(x=10, y=78, width=363, height=70)
        btn_continue = Button(register_window, text="İLK AŞAMAYI BİTİR", command=register_personal_information_check_func,cursor="hand2", bg="green", fg="white", font="Times 18 bold")
        btn_continue.place(x=30, y=337, width=390, height=50)
        varGender = IntVar()
        man = Radiobutton(frame_personal, text="Erkek", variable=varGender, value=1, bg="#514c6d", fg="white",font="Times 12 bold", cursor="heart", selectcolor="orange")
        man.place(x=200, y=50, width=70, height=20)
        woman = Radiobutton(frame_personal, text="Kadin", variable=varGender, value=2, bg="#514c6d", fg="white",font="Times 12 bold", cursor="heart", selectcolor="orange")
        woman.place(x=300, y=50, width=70, height=20)
        clicked_year = StringVar(frame_personal)
        clicked_year.set("Yıllar")
        drop_year = OptionMenu(frame_personal, clicked_year, "1939-1935", "1944-1940", "1949-1945", "1954-1950", "1959-1955","1964-1960", "1969-1965", "1974-1970", "1979-1975", "1984-1980", "1989-1985", "1994-1990","1999-1995", "2004-2000", "2009-2005", "2015-2010", "2020-2016")
        drop_year.config(bg="#27234c",fg="white")
        drop_year.place(x=280, y=8, width=100, height=25)
        clicked_city = StringVar(frame_adress)
        clicked_city.set("İller")
        drop_city = OptionMenu(frame_adress, clicked_city, "Adana","Adıyaman","Afyon","Ağrı","Amasya","Ankara","Antalya","Artvin","Aydın","Balıkesir","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Edirne","Elazığ","Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari","Hatay","Isparta","Mersin","İstanbul","İzmir","Kars","Kastamonu","Kayseri","Kırklareli","Kırşehir","Kocaeli","Konya","Kütahya","Malatya","Manisa","K.maraş","Mardin","Muğla","Muş","Nevşehir","Niğde","Ordu","Rize","Sakarya","Samsun","Siirt","Sinop","Sivas","Tekirdağ","Tokat","Trabzon","Tunceli","Şanlıurfa","Uşak","Van","Yozgat","Zonguldak","Aksaray","Bayburt","Karaman","Kırıkkale","Batman","Şırnak","Bartın","Ardahan","Iğdır","Yalova","Karabük","Kilis","Osmaniye","Düzce")
        drop_city.config(bg="#27234c",fg="white")
        drop_city.place(x=70, y=15, width=110, height=22)

        if language == True:
            btn_continue.configure(text="COMPLETE TO FIRST STAGE")
            lbl_name.configure(text="Name")
            lbl_surname.configure(text="Surname")
            lbl_year.configure(text="BirthYear")
            lbl_city.configure(text="City")
            lbl_district.configure(text="District")
            lbl_address.configure(text="Adress")
            man.configure(text="Male")
            woman.configure(text="Female")
            clicked_year.set("Years")
            clicked_city.set("Cities")
    def register_email_verification_unit_func():
        rastgele = random.randint(1000, 9999)
        email_send_func(rastgele, Umail, names)
        def register_email_verification_check_func():
            email_box1 = email_box.get()
            try:
                email_box1 = int(email_box1)
                eror = False
            except Exception as ex:
                if language == False:
                    messagebox.showerror("Hata", "Yanlış tuşlama yapıldı...")
                else:
                    messagebox.showerror("Eror", "Incorrect typing...")
                eror = True
            if eror != True:
                email_boxxxx = str(email_box1)
                if len(email_boxxxx) != 4:
                    if language == False:
                        messagebox.showerror("Hata", "Eksik veya Fazla bir sayı girildi....")
                    else:
                        messagebox.showerror("Eror", "A missing or extra number was entered.")
                elif int(email_box1) == rastgele:
                    if language == False:
                        messagebox.showinfo("Bilgi", "Kayıt işlemini başarıyla tamamladınız... :)\n\tTEBRİKLER")
                    else:
                        messagebox.showerror("Info",
                                             "You have successfully completed the registration process...\n\tCONGRATULATIONS")
                    register_window.quit()
                    register_window.destroy()
                    welcome_email_func(names, Umail)
                    mail_check = True
                    #    Buradan sonrasında SQL bağlantısı kurulacak......
                    #    Buradan sonrasında SQL bağlantısı kurulacak......
                    #    Buradan sonrasında SQL bağlantısı kurulacak......
                    #    Buradan sonrasında SQL bağlantısı kurulacak......

                else:
                    if language == False:
                        messagebox.showerror("Hata",
                                             "ÜZGÜNÜZ!!! Kod numarası yanlış girildi.\nKayıt yapıldı ama doğrulama yapılamadı\nGiriş Ekranına geçiliyor!!!")
                    else:
                        messagebox.showerror("Info",
                                             "WE ARE SAD!!! The code number was entered incorrectly.\nRegistered but failed to verify\nGoing to the Login Screen!!!")
                    register_window.quit()
                    register_window.destroy()
                    mail_check = False
                    #    Buradan sonrasında SQL bağlantısı kurulacak......
                    #    Buradan sonrasında SQL bağlantısı kurulacak......
                    #    Buradan sonrasında SQL bağlantısı kurulacak......
                    #    Buradan sonrasında SQL bağlantısı kurulacak......

        print(usave)
        frame_register.configure(bg="#27234c")
        frame_email = Frame(frame_register, bd=5, bg="#514c6d")
        frame_email.place(x=10, y=10, width=390, height=240)
        information1 = Label(frame_email, text="3)Email doğrulama Bölümü", bg="orange", fg="White", font="Times 14 bold")
        information1.place(x=8, y=8, width=375, height=25)
        email_name = Umail + " adlı"
        information2 = Label(frame_email,
                             text=f"{email_name}\nEpostanıza gelen 4 haneli rakamı aşağıdaki\nkutu içine girerek doğrulama ve kayıt\nişlemini başarıyla tamamlayın...",
                             bg="#514c6d", fg="White", font="Times 13 bold")
        information2.place(x=10, y=40, width=375, height=80)
        email_box = Entry(frame_email, bg="#27234c", fg="White", font="Times 22 bold")
        email_box.place(x=165, y=175, width=100, height=35)
        btn_continue = Button(register_window, command=register_email_verification_check_func,
                              text="Kayıt işlemini tamamla", cursor="hand2", bg="green", fg="white",
                              font="Times 18 bold")
        btn_continue.place(x=30, y=337, width=390, height=50)
        email_time_counter_func(register_window)

        if language == True:
            btn_continue.configure(text="Complete registration process")
            information1.configure(text="3)Email check Stage")
            information2.configure(
                text=f"{email_name}\nEnter the 4-digit number sent to your\ne-mail in the box below and complete\nthe verification and registration process successfully.")

    register_window = tkinter.Toplevel()
    register_window.title("Register")
    register_window.overrideredirect(True)
    register_window.geometry("450x450+80+80")
    register_window.resizable(width="FALSE", height="FALSE")
    register_window.iconbitmap('image\icon.ico')
    C = Canvas(register_window,bd=10, height=450, width=450,bg="#514c6d" )
    title = Label(register_window, text="Petrikor Uygulamasına KAYIT OL", bg="orange", fg="white", font="times 21 bold")
    title.place(x=10, y=10,width=430)
    frame_register= Frame(register_window,bd=3,bg="#27234c")
    frame_register.place(x=20,y=60,width=410, height=260)
    frame_register_first = Frame(frame_register, bd=3, bg="#514c6d")
    frame_register_first.place(x=4,y=5,width=397, height=250)
    finformation1=Label(frame_register_first,text="Kayıt İşlemine başlamadan önce:",bg="#514c6d",fg="orange",font="Times 15 bold")
    finformation1.place(x=10,y=10,width=390, height=25)
    finformation2 = Label(frame_register_first, text="Kayıt işlemine başla butonuna basarak işleme\nbaşlayabilirsiniz. Kayıt aşamasında geriye\ndönüş mümkün olmayacaktır.\nKayıt İşlemi 5 aşamadan oluşacaktır...\n\n1)Kişisel Bilgileri \n2)İletişim Bilgileri\n3)Eposta Doğrulama\n4)Telefon Doğrulama\n5)Hüküm ve Şartlar", bg="#514c6d",fg="white",font="Times 13 bold")
    finformation2.place(x=10,y=45,width=390, height=185)
    btn_continue= Button(register_window,text="KAYIT OL!!!",command=register_personal_information_unit_func,cursor="hand2", bg="green", fg="white",font="Times 18 bold")
    btn_continue.place(x=30, y=337, width=390, height=50)
    btn_return = Button(register_window, command=come_back_func, cursor="hand2", bg="orange", fg="white", text="GERİ DÖN",font="Times 20 bold")
    btn_return.place(x=30, y=395, width=185, height=50)
    btn_exit = Button(register_window, command=log_out_func, cursor="hand2", bg="red", fg="white", text="ÇIKIŞ YAP",font="Times 20 bold")
    btn_exit.place(x=235, y=395, width=185, height=50)
    C.place(width=450, height=450)

    if language==True:
        finformation1.configure(text="Before starting the Registration Process:")
        finformation2.configure(text="You can start the process by pressing the start\nrecording button. It will not be possible to go back\nduring the registration phase.\nRegistration will consist of 5 stages...\n\n1)Personal Information\n2)Contact Information\n3)Email Verification\n4)Phone Vertification\nTerms and Conditions")
        btn_exit.configure(text="EXIT")
        btn_return.configure(text="COME BACK")
        btn_continue.configure(text="LETS START TO REGISTER")
        title.configure(text="The Petrichor to REGISTER")
    register_window.mainloop()
def Login_func():
    password1 = password.get()
    phone1 = phone.get()
    phone1 = phone1.strip()
    check_phone="05530800537"
    check_password="qwe123"
    if password1==check_password and check_phone==phone1:
        print ("Login completed...")
        if chekkk!=1:
            with open("Archives\end.txt", "w", encoding="utf-8") as endfile1:
                endfile1.write(str(language) + ":" + str(phone1) + "}" + str(password1))
        login_window.quit()
        login_window.destroy()
    else:
        messagebox.showerror("hata","Hatalı bir giriş yaptınız...\nBöyle bir hesap bulunmuyor!")
def select_language():
    global language
    with open("Archives\end.txt", "r+", encoding="utf-8") as endfile1:
        satir_oku = endfile1.readlines()
        satir_read=satir_oku[0]
        lg_words = satir_read.split(":")
        lg_word = lg_words[1]
        lg_text1 = lg_word.split("}")
        phone_text = lg_text1[0]
        password_text = lg_text1[1]
    if lg_text=="choose English":
                title.configure(text="PETRICHOR Project")
                phonet.configure(text="Telephone =>")
                passwordt.configure(text="Password =>")
                btn_reset.configure(text="Remember to reset")
                btn_login.configure(text="LOGIN")
                btn_register.configure(text="REGISTER")
                btn_exit.configure(text="EXIT")
                btn_language.configure(text="Türkçe'ye geç")
                login_window.update()
                language=True
                with open("Archives\end.txt", "w", encoding="utf-8") as endfile1:
                    endfile1.write(str(language) + ":" + str(phone_text) + "}" + str(password_text))
    else:
                title.configure(text="PETRİKOR PROJESİ")
                phonet.configure(text="Telefon ==>")
                passwordt.configure(text="Parola ==>")
                btn_reset.configure(text="Hatırlamayı sıfırla")
                btn_login.configure(text="GİRİŞ YAP")
                btn_register.configure(text="KAYIT OL")
                btn_exit.configure(text="ÇIKIŞ YAP")
                btn_language.configure(text="choose English")
                login_window.update()
                language=False
                with open("Archives\end.txt", "w", encoding="utf-8") as endfile1:
                    endfile1.write(str(language) + ":" + str(phone_text) + "}" + str(password_text))
        # time.sleep(1.2)
        # login_window.after(2000,select_language(clicked))
chekkk=0
ws = Tk()
ws.overrideredirect(True)
ws.geometry("0x0")
login_window =tkinter.Toplevel()
login_window.title("Login")
login_window.overrideredirect(True)
login_window.geometry("400x400+100+100")
login_window.resizable(width= "FALSE", height="FALSE")
login_window.iconbitmap('image\icon.ico')
img = ImageTk.PhotoImage(file="image/background.png")
C=Canvas(login_window,bd = 3 , height = 400, width = 400)
background_image = Label(login_window, image = img)
background_image.place(x=0,y=0)
title= Label(login_window,text="PETRİKOR PROJESİ",bg="#514c6d",fg="white",font="times 28 bold")
title.place(x=10,y=10)
if True:
    x1 = StringVar(login_window)
    x1.set(telRemember)
    x2 = StringVar(login_window)
    x2.set(passRemember)
else:
    x1 = StringVar(login_window)
    x1.set("05*********")
    x2 = StringVar(login_window)
    x2.set("********")
phonet= Label(login_window, text="Telefon=>",bg="#514c6d",fg="white",font= "Times 15 bold")
phonet.place(x=30,y=100,width=110,height=40)
passwordt= Label(login_window, text="Parola=>", bg="#514c6d",fg="white",font= "Times 15 bold")
passwordt.place(x=30,y=155,width=110,height=40)
phone= Entry(login_window,bg="#514c6d",fg="orange",font="times 15 bold",textvariable=x1)
phone.place(x=150,y=100,width=220,height=40)
password= Entry(login_window,bg="#514c6d",show="*",fg="orange",font="times 15 bold",textvariable=x2)
password.place(x=150,y=155,width=220,height=40)
btn_reset= Button(login_window,command=remember_me_func,text="Hatırlamayı sıfırla",cursor="hand2",bg="#514c6d",fg="white",font= "Times 15 bold")
btn_reset.place(x=150, y=203, width=220,height=40)
btn_login=Button(login_window,command=Login_func,cursor="hand2",bg="dark green",fg="white",text="GİRİŞ YAP",font= "Times 20 bold")
btn_login.place(x=30,y=277,width= 340,height=50)
btn_register=Button(login_window,command=Register_func,cursor="hand2",bg="orange",fg="white",text="KAYIT OL",font= "Times 20 bold")
btn_register.place(x=30,y=335,width= 160,height=50)
btn_exit=Button(login_window,command=log_out_func,cursor="hand2",bg="red",fg="white",text="ÇIKIŞ YAP",font= "Times 20 bold")
btn_exit.place(x=210,y=335,width=160,height=50)
if language==False:
    lg_text="choose English"
else:
    lg_text="Türkçe'ye geç"
btn_language= Button(login_window,text=str(lg_text),command=select_language,bg="grey",fg="white",font= "Times 12 bold")
btn_language.place(x=30, y=203, width=110,height=40)
if language==True:
    title.configure(text="PETRICHOR Project")
    phonet.configure(text="Telephone =>")
    passwordt.configure(text="Password =>")
    btn_reset.configure(text="Remember to reset")
    btn_login.configure(text="LOGIN")
    btn_register.configure(text="REGISTER")
    btn_exit.configure(text="EXIT")
    login_window.update()
    language = True
C.place(width= 400,height=400)
login_window.mainloop()
# **********************************************************************************************************************
# **********************************************************************************************************************
# *************************************************Start Video**********************************************************
# **********************************************************************************************************************
# **********************************************************************************************************************
waylist=["C:\\Users\\asus\\Documents\\Python\\Petrikor\\image\\tree_background.mp4","C:\\Users\\asus\\Documents\\Python\\Petrikor\\image\\leaf_background.mp4","C:\\Users\\asus\\Documents\\Python\\Petrikor\\image\\spring_background.mp4","C:\\Users\\asus\\Documents\\Python\\Petrikor\\image\\water_background.mp4"]
rand_value=random.randint(0,3)
video= cv2.VideoCapture (waylist[rand_value])
if not video.isOpened():
    messagebox.showerror("hata", "Video bulunamadı... :(")
while True:
    yakalanan, kare = video.read()
    cv2.line(kare,(520,870),(1500,870),(255,255,255),3)
    font= cv2.FONT_HERSHEY_DUPLEX
    if language==True:
        intro_text="Press 'q' to switch"
        cv2.putText(kare, intro_text, (520, 830), font, 3, (255, 255, 255), 3, cv2.LINE_4)
    else:
        intro_text="Gecmek icin 'q'ya bas"
        cv2.putText(kare,intro_text,(520,830),font,3,(255,255,255),3,cv2.LINE_4)
        cv2.line(kare, (520, 870), (1630, 870), (255, 255, 255), 3)
    if not yakalanan:
        print("video finish...")
        break
    cv2.namedWindow('baslik', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('baslik', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('baslik',kare)
    if cv2.waitKey(15) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
# """
# **********************************************************************************************************************
# **********************************************************************************************************************
# **************************************************Main Menu***********************************************************
# **********************************************************************************************************************
# **********************************************************************************************************************
def log_out_func():
    if language==True:
        res = messagebox.askquestion("Exit", "do you really want to log out ??")
        if res == 'yes':
            sys.exit()
    else:
        res = messagebox.askquestion("Çıkış", "Gerçekten çıkış yapmak istiyor musunuz???")
        if res == 'yes':
            sys.exit()
def help_me_func():
    webbrowser.open_new(r"mailto:onurcaglar60@hotmail.com")
def F_Q_A_func():
    webbrowser.open_new(r"Archives\fqa.pdf")
def date_func():
        gun="bos"
        ay ="bos"
        ttarih = datetime.datetime.now()
        if str(ttarih.strftime("%B"))=="January":
            ay="Ocak"
        elif str(ttarih.strftime("%B"))=="February":
            ay="Şubat"
        elif str(ttarih.strftime("%B"))=="March":
            ay="Mart"
        elif str(ttarih.strftime("%B"))=="April":
            ay="Nisan"
        elif str(ttarih.strftime("%B"))=="May":
            ay="Mayıs"
        elif str(ttarih.strftime("%B"))=="June":
            ay="Haziran"
        elif str(ttarih.strftime("%B"))=="July":
            ay="Temmuz"
        elif str(ttarih.strftime("%B"))=="August":
            ay="Ağustos"
        elif str(ttarih.strftime("%B"))=="September":
            ay="Eylül"
        elif str(ttarih.strftime("%B"))=="October":
            ay="Ekim"
        elif str(ttarih.strftime("%B"))=="November":
            ay="Kasım"
        elif str(ttarih.strftime("%B"))=="December":
            ay="Aralık"
        if language==True:
            ay= str(ttarih.strftime("%B"))
        if str(ttarih.strftime("%A"))=="Monday":
            gun="PAZARTESİ"
        elif str(ttarih.strftime("%A"))=="Tuesday":
            gun="SALI"
        elif str(ttarih.strftime("%A"))=="Wednesday":
            gun="ÇARŞAMBA"
        elif str(ttarih.strftime("%A"))=="Thursday":
            gun="PERŞEMBE"
        elif str(ttarih.strftime("%A"))=="Friday":
            gun="CUMA"
        elif str(ttarih.strftime("%A"))=="Saturday":
            gun="CUMARTESİ"
        elif str(ttarih.strftime("%A"))=="Sunday":
            gun="PAZAR"
        if language==True:
            gun= str(ttarih.strftime("%A"))
        tarih = "\n" + str(ttarih.day) + " " + ay + " " + str(
            ttarih.year) + "\n" + gun
        print(tarih)
        return tarih
def transform_for_nature_func():
    pass
def profile_func():
    pass
def marketing_func():
    def come_back_func():
        if language == False:
            res = messagebox.askquestion("Geri dön", "Geri dönmek istediğine emin misin?")
            if res == 'yes':
                # markt_window.quit()
                markt_window.destroy()
                ws.overrideredirect(False)
                ws.attributes('-fullscreen', True)
        else:
            res = messagebox.askquestion("Come back","Are you sure you want to come back?")
            if res == 'yes':
                # markt_window.quit()
                markt_window.destroy()
                ws.overrideredirect(False)
                ws.attributes('-fullscreen', True)
    def spend_to_markt_func():
        global result_markt
        # BURADA MARKET FİYATLARI SQL DOSYASINDAN GELECEK...
        # BURADA MARKET FİYATLARI SQL DOSYASINDAN GELECEK...
        # BURADA MARKET FİYATLARI SQL DOSYASINDAN GELECEK...
        # BURADA MARKET FİYATLARI SQL DOSYASINDAN GELECEK...
        # BURADA MARKET FİYATLARI SQL DOSYASINDAN GELECEK...
        price_file=10
        price_mask=20
        price_weigher=120
        price_clock=180
        price_tshirt=120
        price_canteen=150
        price_book=200
        price_cup=200
        price_pencilset=250
        price_tablet=1000
        price_bycle=750
        price_bycletf=1500

        stFile=st_file.get()
        stMask=st_mask.get()
        stWeigher=st_weigher.get()
        stClock=st_clock.get()
        stTshirt=st_tshirt.get()
        stCanteen=st_canteen.get()
        stBook=st_book.get()
        stCup=st_cup.get()
        stPencilset=st_pencilset.get()
        stTablet=st_tablet.get()
        stBycle=st_bycle.get()
        stBycletf=st_bycletf.get()

        result_file=stFile*price_file
        result_mask=stMask*price_mask
        result_weigher =stWeigher*price_weigher
        result_clock =stClock*price_clock
        result_tshirt =stTshirt*price_tshirt
        result_canteen =stCanteen*price_canteen
        result_book =stBook*price_book
        result_cup =stCup*price_cup
        result_pencilset =stPencilset*price_pencilset
        result_tablet =stTablet*price_tablet
        result_bycle =stBycle*price_bycle
        result_bycletf =stBycletf*price_bycletf
        result_markt=result_bycle+result_bycletf+result_tablet+result_cup+result_book+result_pencilset+result_canteen+result_tshirt+result_mask+result_clock+result_file+result_weigher
        lbl_my_spend.configure(text=f"Harcamam: {result_markt}p")
        return result_markt
    def buy_to_markt_func():
        result_markt=spend_to_markt_func()
        print(result_markt)
        if result_markt==0:
            pass
        elif int(result_markt) <= int(MYpoint):
            if language == False:
                res = messagebox.askquestion("ONAY",
                                             "Alışveriş için puanınız yeterli, Alışverişi onaylıyor musunuz?")
                if res == 'yes':
                    result_markt = MYpoint - result_markt
                    lbl_my_point.configure(text=f"Puanım: {result_markt}p")
                    stFile = st_file.get()
                    stMask = st_mask.get()
                    stWeigher = st_weigher.get()
                    stClock = st_clock.get()
                    stTshirt = st_tshirt.get()
                    stCanteen = st_canteen.get()
                    stBook = st_book.get()
                    stCup = st_cup.get()
                    stPencilset = st_pencilset.get()
                    stTablet = st_tablet.get()
                    stBycle = st_bycle.get()
                    stBycletf = st_bycletf.get()
                    stList = [stFile, stMask, stWeigher, stClock, stTshirt, stCanteen, stBook, stCup, stPencilset,
                              stTablet, stBycle, stBycletf]
                    orders = "1)File, 2)Mask, 3)Weigher, 4)Clock, 5)Tshirt, 6)Canteen, 7)Book, 8)Cup, 9)Pencilset, 10)Tablet, 11)Bycle, 12)Bycletf\nSiparişler:\n"
                    for i in range(len(stList)):
                        if int(stList[i]) != 0:
                            order = f"Liste {str(i)}. üründen {str(stList[i])} adet sipariş edildi...\n"
                            orders = orders + order
                    print(orders)
            else:
                res = messagebox.askquestion("Confirmation",
                                             "You have enough points for shopping, do you approve the shopping?")
                if res == 'yes':
                    result_markt = MYpoint - result_markt
                    lbl_my_point.configure(text=f"My Point: {result_markt}p")
                    stFile = st_file.get()
                    stMask = st_mask.get()
                    stWeigher = st_weigher.get()
                    stClock = st_clock.get()
                    stTshirt = st_tshirt.get()
                    stCanteen = st_canteen.get()
                    stBook = st_book.get()
                    stCup = st_cup.get()
                    stPencilset = st_pencilset.get()
                    stTablet = st_tablet.get()
                    stBycle = st_bycle.get()
                    stBycletf = st_bycletf.get()
                    stList = [stFile, stMask, stWeigher, stClock, stTshirt, stCanteen, stBook, stCup, stPencilset,
                              stTablet, stBycle, stBycletf]
                    orders = "1)File, 2)Mask, 3)Weigher, 4)Clock, 5)Tshirt, 6)Canteen, 7)Book, 8)Cup, 9)Pencilset, 10)Tablet, 11)Bycle, 12)Bycletf\nSiparişler:\n"
                    for i in range(len(stList)):
                        if int(stList[i]) != 0:
                            order = f"Liste {str(i)}. üründen {str(stList[i])} adet sipariş edildi...\n"
                            orders = orders + order
                            st_file.set(value=0)
                            st

                            
                    print(orders)
        else:
            if language == False:
                messagebox.showerror("Hata", "Yetersiz Puan...")
            else:
                messagebox.showerror("Eror", "Insufficient Point...")
            lbl_my_spend.configure(fg="red")
    result_markt=0
    ws.attributes('-fullscreen', False)
    ws.geometry("0x0")
    ws.overrideredirect(True)
    markt_window = tkinter.Toplevel()
    markt_window.title('Petrikor')
    markt_window.attributes('-fullscreen', True)
    markt_window.iconbitmap('image\icon.ico')
    C = Frame(markt_window, bd=25, bg="dark green")
    frame_markt = Frame(C, bd=10, bg="#514c6d")
    frame_markt_btn = Frame(C, bd=10, bg="#514c6d")
    scroll = Scrollbar(frame_markt)
    scroll.pack(side=RIGHT, fill=Y)
    metin = Text(frame_markt,yscrollcommand=scroll.set,cursor="hand1")
    metin.pack(fill=BOTH)
    scroll.config(command=metin.yview)
    frame_markt_1 = Frame(metin, bd=8, bg="#514c6d")
    frame_markt_2 = Frame(metin, bd=8, bg="#514c6d")
    frame_markt_3 = Frame(metin, bd=8, bg="#514c6d")
    frame_markt_title1 = Frame(frame_markt_1, bd=5, bg="#514c6d")
    frame_markt_title2 = Frame(frame_markt_2, bd=5, bg="#514c6d")
    frame_markt_title3 = Frame(frame_markt_3, bd=5, bg="#514c6d")
    frame_markt_spin1 = Frame(frame_markt_1, bd=5, bg="#514c6d")
    frame_markt_spin2 = Frame(frame_markt_2, bd=5, bg="#514c6d")
    frame_markt_spin3 = Frame(frame_markt_3, bd=5, bg="#514c6d")
    frame_markt_img1 = Frame(frame_markt_1, bd=8, bg="#514c6d")
    frame_markt_img2 = Frame(frame_markt_2, bd=8, bg="#514c6d")
    frame_markt_img3 = Frame(frame_markt_3, bd=8, bg="#514c6d")
    award_img1 = ImageTk.PhotoImage(file="image/award_file.png")
    award_img2 = ImageTk.PhotoImage(file="image/award_labtop.png")
    award_img3 = ImageTk.PhotoImage(file="image/award_labtop.png")
    award_img4 = ImageTk.PhotoImage(file="image/award_labtop.png")
    award_img5 = ImageTk.PhotoImage(file="image/award_labtop.png")
    award_img6 = ImageTk.PhotoImage(file="image/award_labtop.png")
    award_img7 = ImageTk.PhotoImage(file="image/award_labtop.png")
    award_img8 = ImageTk.PhotoImage(file="image/award_kalem.png")
    award_img9 = ImageTk.PhotoImage(file="image/award_labtop.png")
    award_img10 = ImageTk.PhotoImage(file="image/award_labtop.png")
    award_img11 = ImageTk.PhotoImage(file="image/award_bisiklet.png")
    award_img12 = ImageTk.PhotoImage(file="image/award_bisiklet.png")
    award_shopping_file = Label(frame_markt_img1, image=award_img1)
    award_mask = Label(frame_markt_img1, image=award_img2)
    award_weigher = Label(frame_markt_img1, image=award_img3)
    award_clock = Label(frame_markt_img2, image=award_img4)
    award_tshirt = Label(frame_markt_img1, image=award_img5)
    award_canteen = Label(frame_markt_img2, image=award_img6)
    award_cup = Label(frame_markt_img2, image=award_img7)
    award_pencilset = Label(frame_markt_img3, image=award_img8)
    award_book = Label(frame_markt_img2, image=award_img9)
    award_tablet = Label(frame_markt_img3, image=award_img10)
    award_bycle = Label(frame_markt_img3, image=award_img11)
    award_bycle_transformation_kid = Label(frame_markt_img3, image=award_img12)
    # award_ = Label(frame_markt, image=award_img13)
    title_shopping_file = Label(frame_markt_title1, text="Alışveriş Filesi\nADET: -10puan", bg="orange", bd=5, fg="white",font="times 16 bold")
    title_mask = Label(frame_markt_title1, text="50'li Maske\nADET: -20puan", bg="orange", bd=5,fg="white", font="times 16 bold")
    title_weigher = Label(frame_markt_title1, text="Tartı\nADET: -120puan", bg="orange", bd=5, fg="white", font="times 16 bold")
    title_clock = Label(frame_markt_title1, text="Saat\nADET: -180puan", bg="orange", bd=5, fg="white", font="times 16 bold")
    title_tshirt = Label(frame_markt_title2, text="T-Shirt\nADET: -120puan", bg="orange", bd=5, fg="white", font="times 16 bold")
    title_canteen = Label(frame_markt_title2, text="Matara\nADET: -150puan", bg="orange", bd=5, fg="white", font="times 16 bold")
    title_cup = Label(frame_markt_title2, text="Özel Kupa\nADET: -200puan", bg="orange", bd=5, fg="white", font="times 16 bold")
    title_pencilset = Label(frame_markt_title3, text="Kalem Seti\nADET: -250puan", bg="orange", bd=5, fg="white", font="times 16 bold")
    title_book = Label(frame_markt_title2, text="Kitap\nADET: -200puan", bg="orange", bd=5, fg="white", font="times 16 bold")
    title_tablet = Label(frame_markt_title3, text="Tablet\nADET: -1000puan", bg="orange", bd=5, fg="white", font="times 16 bold")
    title_bycle = Label(frame_markt_title3, text="Bisiklet\nADET: -750puan", bg="orange", bd=5, fg="white", font="times 16 bold")
    title_bycle_transformation_kid = Label(frame_markt_title3, text="Bisiklet Elektrik\nDönüşüm Kiti\nADET: -1500puan", bg="orange", bd=5, fg="white", font="times 16 bold")
    st_file = tkinter.IntVar(value=0)
    st_mask = tkinter.IntVar(value=0)
    st_weigher = tkinter.IntVar(value=0)
    st_clock = tkinter.IntVar(value=0)
    st_tshirt = tkinter.IntVar(value=0)
    st_canteen = tkinter.IntVar(value=0)
    st_cup = tkinter.IntVar(value=0)
    st_pencilset = tkinter.IntVar(value=0)
    st_book = tkinter.IntVar(value=0)
    st_tablet = tkinter.IntVar(value=0)
    st_bycle = tkinter.IntVar(value=0)
    st_bycletf = tkinter.IntVar(value=0)
    spin_shopping_file = Spinbox(frame_markt_spin1,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_file,command=spend_to_markt_func)
    spin_mask = Spinbox(frame_markt_spin1,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_mask,command=spend_to_markt_func)
    spin_weigher = Spinbox(frame_markt_spin1,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_weigher,command=spend_to_markt_func)
    spin_clock = Spinbox(frame_markt_spin1,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_clock,command=spend_to_markt_func)
    spin_tshirt = Spinbox(frame_markt_spin2,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_tshirt,command=spend_to_markt_func)
    spin_canteen = Spinbox(frame_markt_spin2,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_canteen,command=spend_to_markt_func)
    spin_cup = Spinbox(frame_markt_spin2,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_cup,command=spend_to_markt_func)
    spin_pencilset = Spinbox(frame_markt_spin3,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_pencilset,command=spend_to_markt_func)
    spin_book = Spinbox(frame_markt_spin2,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_book,command=spend_to_markt_func)
    spin_tablet= Spinbox(frame_markt_spin3,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_tablet,command=spend_to_markt_func)
    spin_bycle_transform = Spinbox(frame_markt_spin3,from_=0,to=10, bd=5, bg="#27234c", fg="white", font="times 16 bold",cursor="hand2",textvariable=st_bycletf,command=spend_to_markt_func)
    spin_bycle= Spinbox(frame_markt_spin3,from_=0,to=10,bd=5,bg="#27234c",fg="white", font="times 16 bold",cursor="hand2",textvariable=st_bycle,command=spend_to_markt_func)
    lbl_note = Label(frame_markt_btn,text="NOT: Puanınızın yeterli olması durumunda marketten seçip aldığınız ürünlerden sonra yaptığınız ilk geri dönüşüm talebinizde size gönderilecektir.",bg="#514c6d", bd=5, fg="white", font="times 15 bold")
    frame_points= Frame(frame_markt_btn,bd=5,bg="#27234c")
    lbl_my_point = Label(frame_points,text=f"Puanım: {MYpoint}p", bg="#27234c", bd=5, fg="white", font="times 16 bold")
    lbl_my_spend = Label(frame_points, text=f"Harcamam: {result_markt}p", bg="#27234c", bd=5, fg="white", font="times 16 bold")
    btn_buy = Button(frame_markt_btn, bd=5, text="SATIN AL", bg="dark green", fg="white", command=buy_to_markt_func,cursor="hand2", font="times 20 bold")
    btn_exit = Button(frame_markt_btn, bd=5, text="ÇIKIŞ YAP", bg="red", fg="white", command=log_out_func,cursor="hand2", font="times 20 bold")
    btn_return = Button(frame_markt_btn, bd=5, text="GERİ DÖN", bg="orange", fg="white", command=come_back_func,cursor="hand2", font="times 20 bold")
    award_shopping_file.pack(side=LEFT, anchor=NW, expand=True)
    award_mask.pack(side=LEFT,anchor=NW, expand=True)
    award_weigher.pack(side=LEFT,anchor=NW, expand=True)
    award_tshirt.pack(side=LEFT, anchor=NW,expand=True)
    award_cup.pack(side=LEFT, anchor=NW, expand=True)
    award_pencilset.pack(side=LEFT, anchor=NW, expand=True)
    award_canteen.pack(side=LEFT, anchor=NW, expand=True)
    award_book.pack(side=LEFT,anchor=NW, expand=True)
    award_clock.pack(side=LEFT, anchor=NW,expand=True)
    award_bycle.pack(side=LEFT, anchor=NW, expand=True)
    award_bycle_transformation_kid.pack(side=LEFT, anchor=NW, expand=True)
    award_tablet.pack(side=LEFT, anchor=NW, expand=True)
    title_shopping_file.pack(side=LEFT, anchor=NW,expand=True)
    spin_shopping_file.pack(side=LEFT, anchor=SW, expand=True)
    title_mask.pack(side=LEFT, anchor=NW,expand=True)
    title_weigher.pack(side=LEFT, anchor=NW,expand=True)
    title_tshirt.pack(side=LEFT, anchor=NW,expand=True)
    title_cup.pack(side=LEFT, anchor=NW,expand=True)
    title_pencilset.pack(side=LEFT, anchor=NW,expand=True)
    title_canteen.pack(side=LEFT, anchor=NW,expand=True)
    title_book.pack(side=LEFT, anchor=NW,expand=True)
    title_clock.pack(side=LEFT, anchor=NW,expand=True)
    title_tablet.pack(side=LEFT, anchor=NW,expand=True)
    title_bycle.pack(side=LEFT, anchor=NW,expand=True)
    title_bycle_transformation_kid.pack(side=LEFT, anchor=NW,expand=True)

    spin_mask.pack(side=LEFT, anchor=SW,expand=True)
    spin_weigher.pack(side=LEFT, anchor=SW,expand=True)
    spin_tshirt.pack(side=LEFT, anchor=SW,expand=True)
    spin_cup.pack(side=LEFT, anchor=SW,expand=True)
    spin_pencilset.pack(side=LEFT, anchor=SW,expand=True)
    spin_canteen.pack(side=LEFT, anchor=SW,expand=True)
    spin_book.pack(side=LEFT, anchor=SW,expand=True)
    spin_clock.pack(side=LEFT, anchor=SW,expand=True)
    spin_tablet.pack(side=LEFT, anchor=SW,expand=True)
    spin_bycle.pack(side=LEFT, anchor=SW,expand=True)
    spin_bycle_transform.pack(side=LEFT, anchor=SW,expand=True)
    lbl_note.pack(side=TOP, expand=True, pady=5)
    btn_exit.pack(side=RIGHT, expand=True, pady=2)
    btn_return.pack(side=RIGHT, expand=True, pady=2)
    btn_buy.pack(side=RIGHT, expand=True, pady=2)
    frame_points.pack(side=RIGHT, expand=True, pady=2)
    lbl_my_point.pack(side=TOP, expand=True)
    lbl_my_spend.pack(side=TOP, expand=True)
    frame_markt_btn.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt.pack(side=BOTTOM, expand=False, fill=X)
    frame_markt_1.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_2.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_3.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_img1.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_title1.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_spin1.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_img2.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_title2.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_spin2.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_img3.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_title3.pack(side=TOP, expand=True, fill=BOTH)
    frame_markt_spin3.pack(side=TOP, expand=True, fill=BOTH)

    C.pack(expand=True, fill=BOTH)
def point_system_func():
    def come_back_func():
        if language == False:
            res = messagebox.askquestion("Geri dön", "Geri dönmek istediğine emin misin?")
            if res == 'yes':
                # point_window.quit()
                point_window.destroy()
                ws.overrideredirect(False)
                ws.attributes('-fullscreen', True)
        else:
            res = messagebox.askquestion("Come back","Are you sure you want to come back?")
            if res == 'yes':
                # point_window.quit()
                point_window.destroy()
                ws.overrideredirect(False)
                ws.attributes('-fullscreen', True)

    ws.attributes('-fullscreen', False)
    ws.geometry("0x0")
    ws.overrideredirect(True)
    point_window=tkinter.Toplevel()
    point_window.title('Petrikor')
    point_window.attributes('-fullscreen', True)
    point_window.iconbitmap('image\icon.ico')
    C = Frame(point_window,bd=25, bg="dark green")
    frame_atik=Frame(C,bd=10,bg="#514c6d")
    frame_atik_btn = Frame(C, bd=10, bg="#514c6d")
    frame_atik_title = Frame(C, bd=5, bg="#514c6d")
    frame_atik_txt = Frame(C, bd=8, bg="#514c6d")
    atik_img1 = ImageTk.PhotoImage(file="image/plastik_atik.png")
    atik_img2 = ImageTk.PhotoImage(file="image/kagit_atik.png")
    atik_img3 = ImageTk.PhotoImage(file="image/metal_atik.png")
    atik_img4 = ImageTk.PhotoImage(file="image/elektronik_atik.png")
    atik_plastic = Label(frame_atik,image=atik_img1)
    atik_paper = Label(frame_atik, image=atik_img2)
    atik_metal = Label(frame_atik, image=atik_img3)
    atik_electronic = Label(frame_atik, image=atik_img4)
    platic_title=Label(frame_atik_title,text="Plastik Atıklar\nKg başı: +10puan",bg="orange",bd=5,fg="white",font="times 20 bold")
    paper_title = Label(frame_atik_title, text="Kağıt Atıklar\nKg başı: +6puan", bg="orange", bd=5, fg="white", font="times 20 bold")
    metal_title = Label(frame_atik_title, text="Metal Atıkları\nKg başı: +4puan", bg="orange", bd=5, fg="white", font="times 20 bold")
    electronic_title = Label(frame_atik_title, text="Pil ve\nElektronik Atıklar\nKg başı: +15puan", bg="orange", bd=5, fg="white",font="times 20 bold")
    plastic_txt = Label(frame_atik_txt, text="Plastik Atıklar doğada en fazla\nbulunan ve çevremizi\nen çok kirleten atıklardır.\nDönüşümü ile tonlarca sera gazı\nönlenir.Ayrıca elektirik\nüretimine ciddi fayda sağlar", bg="#27234c", bd=5, fg="white", font="times 13 bold")
    paper_txt = Label(frame_atik_txt, text="Kağıt Atıklar değerledirilebildiği\ntakdirde çok önemli\nolan bir atık türüdür.", bg="#27234c", bd=5, fg="white", font="times 13 bold")
    metal_txt = Label(frame_atik_txt, text="Metal Atıkları geri dönüşümü ile en\nfazla kazanç sağlanabilen\nve atıldığı takdirde doğaya\nçok büyük zarar veren bir atıkdır.", bg="#27234c", bd=5, fg="white", font="times 13 bold")
    electronic_txt = Label(frame_atik_txt,text="Elektronik ve pil Atık değeri en az\nbilinen atıklardır. Birden\nfazla madeni barındrırlar.\nGeri dönüşümleri ekonomiye\nbüyük katkı sağlar.", bg="#27234c",bd=5, fg="white", font="times 13 bold")
    lbl_note1 = Label(frame_atik_btn, text="Atıkları atık toplama merkezine her kendiniz götürdüğünüzde atığın kilogramı başına ekstra 1 puan kazanırsınız...",bg="#514c6d",bd=5, fg="white", font="times 15 bold")
    lbl_note2=Label(frame_atik_btn,text="Not: Organik ve cam atıkları da toplandığında puansız olarak Petrikor Projesine verilebilir.\n(<<<Ayrıca çağırmak için Organik atık en az: 5litre/////Cam atık en az:5Kg>>>)",bg="#514c6d",bd=5, fg="white", font="times 15 bold")
    btn_exit = Button(frame_atik_btn, bd=5, text="ÇIKIŞ YAP", bg="red", fg="white", command=log_out_func, cursor="hand2",font="times 20 bold")
    btn_return = Button(frame_atik_btn, bd=5, text="GERİ DÖN", bg="orange", fg="white", command=come_back_func,cursor="hand2", font="times 20 bold")
    atik_plastic.pack(side=LEFT,expand=True)
    atik_metal.pack(side=LEFT, expand=True)
    atik_paper.pack(side=LEFT,expand=True)
    atik_electronic.pack(side=LEFT, expand=True)
    platic_title.pack(side=LEFT,expand=True)
    metal_title.pack(side=LEFT, expand=True)
    paper_title.pack(side=LEFT, expand=True)
    electronic_title.pack(side=LEFT, expand=True)
    plastic_txt.pack(side=LEFT, expand=True)
    metal_txt.pack(side=LEFT, expand=True)
    paper_txt.pack(side=LEFT, expand=True)
    electronic_txt.pack(side=LEFT, expand=True)
    lbl_note1.pack(side=TOP, expand=True, pady=5)
    lbl_note2.pack(side=TOP,expand=True,pady=5)
    btn_exit.pack(side=RIGHT,expand=True,pady=2)
    btn_return.pack(side=RIGHT, expand=True,pady=2)
    frame_atik.pack(side=TOP, expand=True, fill=BOTH)
    frame_atik_title.pack(side=TOP, expand=True, fill=BOTH)
    frame_atik_txt.pack(side=TOP, expand=True, fill=BOTH)
    frame_atik_btn.pack(side=BOTTOM, expand=True,fill=X)
    C.pack(expand=True, fill=BOTH)
    if language==True:
        btn_exit.configure(text="EXIT")
        btn_return.configure(text="RETURN")
        platic_title.configure(text="Plastic Wastes\nPer Kg:+10puan")
        paper_title.configure(text="Paper Wastes\nPer Kg:+5puan")
        metal_title.configure(text="Metal Wastes\nPer Kg:+15puan")
        electronic_title.configure(text="Electronic Wastes\nPer Kg:+20puan")
        plastic_txt.configure(text="Plastic Wastes are the most\nabundant wastes in nature and\npollute our environment the most.\nWith its conversion, tons of\ngreenhouse gases are prevented.\nIt also provides serious benefits\nto electricity production.")
        paper_txt.configure(text="Paper Waste is a very important\ntype of waste if it can be evaluated.")
        metal_txt.configure(text="The most gain can be achieved with\nthe recycling of metal\nWaste and it is a waste that causes\ngreat harm to the nature if discarded.")
        electronic_txt.configure(text="Electronic Waste is the least\nknown waste. They contain\nmore than one mine. Recycling\ncontributes greatly to the economy.")
        lbl_note1.configure(text="Each time you take away the waste yourself, you earn an extra 1 point per kilogram of waste...")
        lbl_note2.configure(text="Note: When organic and glass wastes are collected, they can be given to the Petrikor Project without any points.\n(<<<Organic minimum: 5liter/////Glass waste minimum:5Kg>>>)")
def grade_system_func(totalMYpoint,MYgrade):
    # seviye sistemi fonk.
    global New_Ugrade
    for i in range (0,1000000,100):
        if (i-totalMYpoint)>=totalMYpoint and (i-(2*totalMYpoint))<=100:
            New_Ugrade=math.floor(totalMYpoint/100)
            if New_Ugrade!=MYgrade:
                lbl_head.configure(text=f"PETRİKOR'a hoşgeldin, KULLANICI şu anlık mevcut seviyen: {New_Ugrade}")
                #               Burada SQL dosyasına yeni seviye kaydı olacak...
                #               Burada SQL dosyasına yeni seviye kaydı olacak...
                #               Burada SQL dosyasına yeni seviye kaydı olacak...
                #               Burada SQL dosyasına yeni seviye kaydı olacak...
def calendar_page_change2_func():
    if language==False:
        lbl_calendar.configure(text="Petrikor Projesi\nsayesinde günlük\n10ton çöp geri\ndönüştürülerek ülke\nekonomisine geri\nkazandırılmaktadır.")
        lbl_point.configure(text="")
    else:
        lbl_calendar.configure(
            text="Thanks to the\nPetrikor Project,\n10 tons of garbage\nper day is recycled and\nbrought back to the\ncountry's economy.")
        lbl_point.configure(text="")
def calendar_page_change1_func():
    if language==False:
        lbl_calendar.configure(text=f"Günün Tarihi:\n{str(calendar)}")
        lbl_point.configure(text=f"Mevcut Puanım: {MYpoint}puan")
    else:
        lbl_calendar.configure(text=f"Date of the Day:\n{str(calendar)}")
        lbl_point.configure(text=f"My Current Score: {MYpoint}score")
def mapping_func():
    pass
def fun_func():
    pass
def settings_func():
    pass
calendar = date_func()
global MYpoint,MYgrade,totalMYpoint
MYgrade=0
totalMYpoint=1200
MYpoint=999
ws = Tk()
ws.title('Petrikor')
ws.iconbitmap('image\icon.ico')
ws.attributes('-fullscreen', True)
# C = Canvas(ws, bd=50, bg="#514c6d")
# C.pack(fill=tkinter.BOTH, expand=True)
frame_headline=Frame(ws,bd=8,bg="#514c6d")
headline=Label(frame_headline,bd=8,bg="orange",fg="white",text="PETRİKOR Projesi",font="times 28 bold")
btn_help=Button(headline,bg="dark green",fg="white",command=help_me_func,cursor="hand2",text="YARDIM",font="times 20 bold")
btn_sss=Button(headline,bg="dark green",fg="white",command=F_Q_A_func,cursor="hand2",text="S.S.S.",font="times 20 bold")
lbl_head= Label(frame_headline,bd=8,bg="#514c6d",fg="white",text=f"PETRİKOR'a hoşgeldin, KULLANICI şu anlık mevcut seviyen: {MYgrade}",font="times 16 bold")
frame_right= Frame(ws,bg="#514c6d",bd=25)
frame_calendar= Frame(frame_right,bg="#27234c",bd=5)
frame_calendar1= Frame(frame_calendar,bg="#27234c",bd=5)
lbl_calendar= Label(frame_calendar1,bd=25,text=f"Günün Tarihi:\n{str(calendar)}",bg="#27234c",fg="turquoise",font="times 20 bold")
lbl_point= Label(frame_calendar1,bd=25,text=f"Mevcut Puanım: {MYpoint}puan",bg="#27234c",fg="turquoise",font="times 20 bold")
btn_calendar1= Button(frame_calendar,text="<",command=calendar_page_change1_func,bd=5,bg="#27234c",cursor="hand2",fg="turquoise",font="times 18 bold")
btn_calendar2= Button(frame_calendar,text=">",command=calendar_page_change2_func,bd=5,bg="#27234c",cursor="hand2",fg="turquoise",font="times 18 bold")
frame_score_table= Frame(frame_right,bg="#514c6d",bd=10)
frame_city_score= Frame(frame_score_table,bg="#27234c",bd=5)
frame_district_score= Frame(frame_score_table,bg="#27234c",bd=5)
lbl_city_title= Label(frame_city_score,bd=5,bg="orange",text="Şehir Liderlik Tablosu",font="times 16 bold",fg="white")
lbl_district_title= Label(frame_district_score,bd=5,bg="orange",text="İlçe Liderlik Tablosu",font="times 16 bold",fg="white")
frame_top_users_city= Frame(frame_city_score,bg="dark green",bd=5)
frame_top_users_district= Frame(frame_district_score,bg="dark green",bd=5)
lbl_top_Cuser1= Label(frame_top_users_city,text="1)Nick1\t\t500p",font="times 12 bold",fg="white",bd=5,bg="dark green")
lbl_top_Cuser2= Label(frame_top_users_city,text="2)Nick2\t\t450p",font="times 12 bold",fg="white",bd=5,bg="dark green")
lbl_top_Cuser3= Label(frame_top_users_city,text="3)Nick3\t\t350p",font="times 12 bold",fg="white",bd=5,bg="dark green")
lbl_top_Cuser4= Label(frame_top_users_city,text="4)Nick4\t\t150p",font="times 12 bold",fg="white",bd=5,bg="dark green")
lbl_top_Cuser5= Label(frame_top_users_city,text="5)Nick5\t\t50p",font="times 12 bold",fg="white",bd=5,bg="dark green")
lbl_top_Duser1= Label(frame_top_users_district,text="1)Nick1\t\t350p",font="times 12 bold",fg="white",bd=5,bg="dark green")
lbl_top_Duser2= Label(frame_top_users_district,text="2)Nick2\t\t150p",font="times 12 bold",fg="white",bd=5,bg="dark green")
lbl_top_Duser3= Label(frame_top_users_district,text="3)Nick3\t\t48p",font="times 12 bold",fg="white",bd=5,bg="dark green")
lbl_top_Duser4= Label(frame_top_users_district,text="4)Nick4\t\t20p",font="times 12 bold",fg="white",bd=5,bg="dark green")
lbl_top_Duser5= Label(frame_top_users_district,text="5)Nick5\t\t5p",font="times 12 bold",fg="white",bd=5,bg="dark green")
frame_btn= Frame(ws,bg="#514c6d",bd=50)
btn_now= Button(frame_btn,bd=5,text="DOĞA için DÖNÜŞTÜR...",bg="dark green",fg="white",command=transform_for_nature_func,cursor="hand2",font="times 20 bold")
btn_profile= Button(frame_btn,bd=5,text="Profilim",bg="#008B45",fg="white",command=profile_func,cursor="hand2",font="times 20 bold")
btn_point= Button(frame_btn,bd=5,text="Puanlama Sistemi",bg="#008B45",fg="white",command=point_system_func,cursor="hand2",font="times 20 bold")
btn_fun= Button(frame_btn,bd=5,text="Eğlence",bg="#008B45",fg="white",command=fun_func,cursor="hand2",font="times 20 bold")
btn_map= Button(frame_btn,bd=5,text="Bölge Haritam",bg="#008B45",fg="white",command=mapping_func,cursor="hand2",font="times 20 bold")
btn_markt= Button(frame_btn,bd=5,text="Market",bg="#008B45",fg="white",command=marketing_func,cursor="hand2",font="times 20 bold")
btn_setting= Button(frame_btn,bd=5,text="Ayarlar",bg="#008B45",fg="white",command=settings_func,cursor="hand2",font="times 20 bold")
btn_exit= Button(frame_btn,bd=5,text="ÇIKIŞ YAP",bg="red",fg="white",command=log_out_func,cursor="hand2",font="times 20 bold")
frame_headline.pack(side=TOP,expand=False,fill=BOTH)
headline.pack(side=TOP,expand=True,fill=X)
btn_help.pack(side=RIGHT,expand=False,fill=Y)
btn_sss.pack(side=LEFT,expand=False,fill=Y)
lbl_head.pack(side=BOTTOM,expand=False,fill=X)
frame_right.pack(side=RIGHT,expand=True,fill=BOTH)
frame_calendar.pack(side=TOP,expand=False)
btn_calendar1.pack(side=LEFT,expand=True,anchor=W)
frame_calendar1.pack(side=LEFT,expand=False)
lbl_calendar.pack(side=TOP,expand=True,fill=X)
lbl_point.pack(side=TOP,expand=True,fill=X)
btn_calendar2.pack(side=RIGHT,expand=True,anchor=E)
frame_score_table.pack(side=BOTTOM,expand=True,fill=BOTH)
frame_city_score.pack(side=LEFT,expand=True,fill=BOTH)
frame_district_score.pack(side=RIGHT,expand=True,fill=BOTH)
lbl_city_title.pack(side=TOP,expand=False,fill=X)
lbl_district_title.pack(side=TOP,expand=False,fill=X)
frame_top_users_city.pack(expand=True,fill=X)
frame_top_users_district.pack(expand=True,fill=X)
lbl_top_Cuser1.pack(side=TOP,expand=False,fill=X)
lbl_top_Cuser2.pack(side=TOP,expand=False,fill=X)
lbl_top_Cuser3.pack(side=TOP,expand=False,fill=X)
lbl_top_Cuser4.pack(side=TOP,expand=False,fill=X)
lbl_top_Cuser5.pack(side=TOP,expand=False,fill=X)
lbl_top_Duser1.pack(side=TOP,expand=False,fill=X)
lbl_top_Duser2.pack(side=TOP,expand=False,fill=X)
lbl_top_Duser3.pack(side=TOP,expand=False,fill=X)
lbl_top_Duser4.pack(side=TOP,expand=False,fill=X)
lbl_top_Duser5.pack(side=TOP,expand=False,fill=X)
frame_btn.pack(side=LEFT,expand=True,fill=BOTH)
btn_now.pack(expand=True,fill=X)
btn_profile.pack(expand=True,fill=X)
btn_point.pack(expand=True,fill=X)
btn_fun.pack(expand=True,fill=X)
btn_map.pack(expand=True,fill=X)
btn_markt.pack(expand=True,fill=X)
btn_setting.pack(expand=True,fill=X)
btn_exit.pack(expand=True,fill=X)

grade_system_func(totalMYpoint,MYgrade)


if language == True:
    headline.configure(text="The PETRICHOR Project")
    btn_sss.configure(text="F.A.Q.")
    btn_help.configure(text="HELP ME")
    lbl_head.configure(text="Welcome to PETRICHOR, USER current Level: 0")
    lbl_calendar.configure(text=f"Date of the Day:\n{str(calendar)}")
    lbl_district_title.configure(text="District Leaderboard")
    lbl_city_title.configure(text="City Leaderboard")
    lbl_point.configure(text="My Current Score: 0score")
    btn_fun.configure(text="ENTERTAINMENT")
    btn_point.configure(text="SCORING SYSTEM")
    btn_now.configure(text="TRANSFORM for NATURE...NOW!")
    btn_profile.configure(text="MY PROFILE")
    btn_map.configure(text="MY AREA MAP")
    btn_exit.configure(text="EXIT")
    btn_setting.configure(text="SETTINGS")
    btn_markt.configure(text="MARKT")

ws.mainloop()

# **********************************************************************************************************************
# *********************************************THE PETRİKOR PROJECT*****************************************************
# ************************************************BY ONUR CAGLAR********************************************************
# **********************************************************************************************************************
# **********************************************************************************************************************