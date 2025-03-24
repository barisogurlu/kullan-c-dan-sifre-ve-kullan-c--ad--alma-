from tkinter import *

def giris():
    # Kullanıcı adı ve şifreyi al
    username = username_entry.get()
    password = password_entry.get()

    # Kullanıcı adı ve şifreyi kontrol et
    if username == "admin" and password == "123":
        result_label.config(text="Giriş başarılı!")
    else:
        result_label.config(text="Kullanıcı adı veya şifre hatalı.")

# Ana pencere oluştur
root = Tk()
root.title("KULLANICI ARAYÜZÜ")

# Kullanıcı adı etiketi ve giriş alanı
username_label = Label(root, text="Kullanıcı adı")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

# Şifre etiketi ve giriş alanı
password_label = Label(root, text="Şifre")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

# Giriş yap butonu
login_button = Button(root, text="Giriş Yap", command=giris)
login_button.pack()

# Giriş sonucu etiketi
result_label = Label(root, text="")
result_label.pack()

# Pencereyi çalıştır
root.mainloop()