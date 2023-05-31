# Saya Adinda Salsabilla 2005319 mengerjakan Latihan 5 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin*/

from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image
import requests
import io

# data input
hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "https://static.vecteezy.com/system/resources/previews/000/554/577/original/apartment-building-vector.jpg"))
hunians.append(Rumah("Sekar MK", 5, 2, "https://img.freepik.com/free-vector/doodle-house-cartoon-design_1308-93798.jpg"))
hunians.append(Indekos("Pak Abdul", "Cahya", "https://taxacademy.id/wp-content/uploads/2022/11/Apakah-Pemilik-Kos-Kosan-Wajib-Bayar-Pajak.jpg"))
hunians.append(Rumah("Satria", 1, 4, "https://img.freepik.com/free-vector/doodle-house-cartoon-design_1308-93798.jpg"))

# root untuk page
root = Tk()
root.title("Praktikum DPBO Python")
photo = []

# page details
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # get image index
    url = hunians[index].get_image()
    response = requests.get(url)
    image = response.content
    img = Image.open(io.BytesIO(image))
    img = img.resize((250, 200))
    photo_img = ImageTk.PhotoImage(img)
    photo.append(photo_img)
    landing_page = Frame(top, padx=5, pady=5)
    landing_page.pack(padx=5, pady=5)
    label_img_landing = Label(landing_page, image=photo_img)
    label_img_landing.pack()

    # detail page atribut
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # SUMMARY
    # d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

    # ECIT BUTTON
    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

# Landing Page & Enter Button - klik main page untuk masuk ke page data residen
def enter():
    # landing page destroy agar tidak muncul main page double
    landing_page.destroy()
    label_img_landing.destroy()
    land_page.destroy()
    b_enter.destroy()

    # MAIN PAGE
    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    # GET DATA & PUT TO TABLE
    for index, h in enumerate(hunians):
        # Set tabel appereance
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        # Get the index data and put it on table
        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

# LANDING PAGE
# Get image
url = "https://media.istockphoto.com/id/539647558/vector/car-track-play-placemat.jpg?s=612x612&w=0&k=20&c=y1z4MKwBWxn4qW2564x-wqEzCdHeA2-b_9TU1CXUAYU="
response = requests.get(url)
image = response.content
img = Image.open(io.BytesIO(image))
img = img.resize((400, 300))
photo_img = ImageTk.PhotoImage(img)
photo.append(photo_img)
landing_page = Frame(root, padx=5, pady=5)
landing_page.pack(padx=5, pady=5)
label_img_landing = Label(landing_page, image=photo_img)
label_img_landing.pack()

# label in landing page
land_page = Label(root, text="Hi you're in landing page, press 'Main Page' to Continue", padx=10, pady=10)
land_page.pack()

# main page button with enter command to go to main page
b_enter = Button(text="Main Page", command=enter)
b_enter.pack(pady=10)

root.mainloop()
