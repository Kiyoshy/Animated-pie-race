from sjvisualizer import DataHandler, Canvas, PieRace
from PIL import Image, ImageTk

file_name = "data/co2_country.xlsx"


# load the data into a data frame
df = DataHandler.DataHandler(excel_file=file_name, number_of_frames=2200).df

# Defining the rgb values of the colors (a json file can also be used)
colors = {
    "Canada": (255, 0, 0),
    "China" : (211, 239, 21),
    "Iran" : (46, 179, 158),
    "Russia" : (200, 118, 29),
    "Italy" : (186, 215, 117),
    "Japan": (234, 124, 117),
    "Germany" : (234, 124, 28),
    "Saudi Arabia" : (9, 124, 188),
    "United Kingdom" : (9, 212, 188),
    "United States": (3, 52, 249),
    "France" : (12, 90, 116),
    "India": (165, 175, 101),
    "Poland" : (165, 175, 172),
    "Ukraine" : (230, 140, 160)
}

# creatig the canvas animation
canvas = Canvas.canvas()

# adding the background image
background_image = Image.open("CO2.png")
background_photo = ImageTk.PhotoImage(background_image)
canvas.canvas.create_image(0, 0, anchor="nw", image=background_photo)

# adding decoration with TkInter
line = canvas.canvas.create_line(630, 20, 630, 150, width=8, fill=Canvas._from_rgb((75, 75, 155)))
tons = canvas.canvas.create_text(980, 940, text="Tons of CO\u2082", font=("Arial", 22), fill=Canvas._from_rgb((120,120,120)))
source = canvas.canvas.create_text(1680, 970, text="Source: Global Carbon Budget for 2022", font=("Arial", 14), fill=Canvas._from_rgb((120,120,120)))


# adding the pie race
pie_race = PieRace.pie_plot(canvas=canvas.canvas, df=df, colors=colors)
canvas.add_sub_plot(pie_race)

# adding a title
canvas.add_title("CO\u2082 emissions per Country", color=(0,0,0))
canvas.add_sub_title("From 1920 - 2021", color=(150,150,150))

# adding a time
canvas.add_time(df=df, time_indicator="year", color=(254, 85, 0))

# adding a title image
co2_img = Image.open("co2_tl.png")
co2_img = co2_img.resize((125, 125))
title_img = ImageTk.PhotoImage(co2_img)
canvas.canvas.create_image(470, 20, anchor="nw", image=title_img)

canvas.play()