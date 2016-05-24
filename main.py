import tkinter
import obd

connection = obd.OBD()

cmd_0 = obd.commands.RPM
cmd_1 = obd.commands.SPEED

#r_RPM = 2000  //THESE ARE FOR TESTING POURPOSES
#r_SPEED = 80


r_RPM = connection.query(cmd_0)
r_SPEED = connection.query(cmd_1)

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="white", height=500, width=600)

speed_var = r_SPEED #input from obd.speedometer
rpm = r_RPM #input from obd.RPM

tacho = 178-((rpm/1000)*16.875) #178(180-extent) // My RPM cap is at 7000 so 16.875 is used here (135 / 8(0...7)=16.875)

#Tachometer visuals
coord_1 = 75, 75, 600, 600
coord_2 = 125, 125, 550, 550
arc = C.create_arc(coord_1, start=45, extent=135, fill="gray90", outline="gray90") #Tachometer background
arc2 = C.create_arc(coord_2, start=45, extent=135, fill="white", outline="white") #Tachometer foreground (Speedometer background)
arc3 = C.create_arc(coord_1, start=tacho, extent=2, fill="#c0392b", outline="#c0392b") #Gauge - Change width by changing the extent

#Tachometer lines
line_0 = C.create_arc(coord_1, start=179, extent=0.2, fill="black")
line_05 = C.create_arc(coord_1, start=170.5625, extent=0.2, outline="gray", fill="gray")
line_1 = C.create_arc(coord_1, start=162.125, extent=0.2, fill="black")
line_15 = C.create_arc(coord_1, start=153.6875, extent=0.2, outline="gray", fill="gray")
line_2 = C.create_arc(coord_1, start=145.25, extent=0.2, fill="black")
line_25 = C.create_arc(coord_1, start=136.8125, extent=0.2, outline="gray", fill="gray")
line_3 = C.create_arc(coord_1, start=128.375, extent=0.2, fill="black")
line_35 = C.create_arc(coord_1, start=119.9375, extent=0.3, outline="gray", fill="gray")
line_4 = C.create_arc(coord_1, start=111.5, extent=0.2, fill="black")
line_45 = C.create_arc(coord_1, start=103.0625, extent=0.2, outline="gray", fill="gray")
line_5 = C.create_arc(coord_1, start=94.625, extent=0.2, fill="black")
line_55 = C.create_arc(coord_1, start=86.1875, extent=0.2, outline="gray", fill="gray")
line_6 = C.create_arc(coord_1, start=77.75, extent=0.2, fill="black")
line_65 = C.create_arc(coord_1, start=69.3125, extent=0.2, outline="gray", fill="gray")
line_7 = C.create_arc(coord_1, start=60.875, extent=0.2, fill="black")
line_8 = C.create_arc(coord_1, start=70.7, extent=6, fill="#c0392b", outline="#c0392b")
line_9 = C.create_arc(coord_1, start=62.3, extent=6, fill="#c0392b", outline="#c0392b")
line_10 = C.create_arc(coord_1, start=45.2, extent=16, fill="#c0392b", outline="#c0392b")

#Tachometer outer rim
rpm_0 = C.create_text(75, 345, anchor="se", text="0", font=("Purisa", 20))
rpm_1 = C.create_text(80, 270, anchor="se", text="1", font=("Purisa", 20))
rpm_2 = C.create_text(115, 200, anchor="se", text="2", font=("Purisa", 20))
rpm_3 = C.create_text(170, 140, anchor="se", text="3", font=("Purisa", 20))
rpm_4 = C.create_text(240, 95, anchor="se", text="4", font=("Purisa", 20))
rpm_5 = C.create_text(325, 75, anchor="se", text="5", font=("Purisa", 20))
rpm_6 = C.create_text(410, 80, anchor="se", text="6", font=("Purisa", 20), fill="#c0392b")
rpm_7 = C.create_text(485, 110, anchor="se", text="7", font=("Purisa", 20), fill="#c0392b")

#Speedometer value output
speed = C.create_text(300, 250, anchor="center")
C.itemconfig(speed, text=speed_var, font=("Purisa", 100), fill="#c0392b")

C.tag_raise(arc3)
C.tag_raise(arc2)#Bring to the front of tachometer
C.tag_raise(speed)#Bring on top of all
C.pack()

top.mainloop()
