import tkinter as tk
import PIL
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk


root = tk.Tk()
root.geometry('1000x600')
root.title("Image Editing Tool")
root.config(bg="white")

pen_color = "black"
pen_size = 5
file_path = ""
image_width=0
image_height=0

#function add_image
def add_image():
   global file_path
   file_path=filedialog.askopenfilename(initialdir=r"C:\Users\Hi\Desktop\anagha_projects\Python_projects\Tkinter_Image_Editor\Pictures")
   image = Image.open(file_path)
   #resize image to fit the canvas
   width,height = int(image.width/2),int(image.height/2)
   image=image.resize((width+250,height+250),Image.ANTIALIAS)
   image_width = image.width
   image_height = image.height
   canvas.config(width=image.width,height=image.height)
   print("canvas width = ",width)
   print("canvas height = ",height)
   image=ImageTk.PhotoImage(image)
   canvas.image = image
   canvas.create_image(0,0,image=image,anchor="nw")

#function draw
def draw(event):
   x1,y1=(event.x-pen_size),(event.y-pen_size)
   x2,y2=(event.x+pen_size),(event.y+pen_size)
   canvas.create_oval(x1,y1,x2,y2,fill=pen_color,outline='')

#function change pen color
def change_color():
   global pen_color
   pen_color = colorchooser.askcolor(title="Select Pen color")[1]

#function pen size
def change_size(size):
   global pen_size
   pen_size=size

#function to clear canvas
def clear_canvas():
   canvas.delete("all")
   canvas.create_image(0,0,image=canvas.image,anchor="nw")

#to add frame
left_frame = tk.Frame(root,width=200,height=600,bg="white")
left_frame.pack(side="left",fill="y")

#to add button to add image
image_button = tk.Button(left_frame,text="Add Image",command=add_image,bg="white")
image_button.pack(pady=20)

#button to change pen color
color_button = tk.Button(left_frame,text="Change Pen Color",command=change_color,bg="white")
color_button.pack(padx=25,pady=25)

#to change pen size
pen_size_frame = tk.Frame(left_frame,bg="white")
pen_size_frame.pack(pady=5)

#create radio buttons small,medium and large pen size
#small
pen_size_1 = tk.Radiobutton(pen_size_frame,text="Small",value=3,command=lambda:change_size(3),bg="white")
pen_size_1.pack(side="left")

#medium
pen_size_2 = tk.Radiobutton(pen_size_frame,text="Medium",value=5,command=lambda:change_size(5),bg="white")
pen_size_2.pack(side="left")
pen_size_2.select()

#large
pen_size_3 = tk.Radiobutton(pen_size_frame,text="Large",value=7,command=lambda:change_size(7),bg="white")
pen_size_3.pack(side="left")

#button to clear canvas
clear_button = tk.Button(left_frame,text="Clear",command=clear_canvas,bg="#FF9797")
clear_button.pack(pady=10)



#to add the filters
filter_label = tk.Label(left_frame,text="Select Filter",bg="white")
filter_label.pack()

filter_combobox = ttk.Combobox(left_frame,values=["Black and white","Blur","Emboss","Sharpen","Smooth","Contour","Detail","Smooth_more"])
filter_combobox.pack()

filter_combobox.bind("<<ComboboxSelected>>",lambda event:apply_filter(filter_combobox.get()))

#function to apply filters
def apply_filter(filter):
   image = Image.open(file_path)
   width,height = int(image.width/2),int(image.height/2)
   image=image.resize((width+250,height+250),Image.ANTIALIAS)
   if filter == "Black and white":
      image = ImageOps.grayscale(image)
   elif filter == "Blur":
      image = image.filter(ImageFilter.BLUR)
   elif filter == "Emboss":
      image = image.filter(ImageFilter.EMBOSS) 
   elif filter == "Sharpen":
      image = image.filter(ImageFilter.SHARPEN)
   elif filter == "Smooth":
      image = image.filter(ImageFilter.SMOOTH)
   elif filter == "Contour":
      image = image.filter(ImageFilter.CONTOUR)
   elif filter == "Detail":
      image = image.filter(ImageFilter.DETAIL)
   elif filter == "Smooth_more":
      image = image.filter(ImageFilter.SMOOTH_MORE)



   image = ImageTk.PhotoImage(image)
   canvas.image=image
   canvas.create_image(0,0,image=image,anchor="nw")


def save_img():
   fileloc = filedialog.asksaveasfilename(initialdir=r"C:\Users\Hi\Desktop\anagha_projects\Python_projects\Tkinter_Image_Editor\Pictures\output",defaultextension='.jpg')
   #x = root.winfo_rootx()
   #y = root.winfo_rooty()+100
   root.update()
   x = root.winfo_rootx()
   y = root.winfo_rooty()+100
   print(x,y)
   img = ImageGrab.grab(bbox=(x,y,x+1900,y+890))
   #img.resize(900,900)
   #img = ImageGrab.grab(image)
   img.show()
   img.save(fileloc)


#button to save the image
save_button = tk.Button(left_frame,text="Save",command=save_img,bg="white")
save_button.pack(pady=20)


   





#to create canvas
canvas = tk.Canvas(root,width=500,height=500)
canvas.pack()

canvas.bind("<B1-Motion>",draw)

root.mainloop()
