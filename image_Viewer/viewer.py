# my_label.grid_forget()
from os import stat
from tkinter import *
from PIL import ImageTk, Image

# Main Window
root = Tk()
root.title("Image Viewer")

# Display image on window
my_img1 = ImageTk.PhotoImage(Image.open("images/ronaldo1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/ronaldo2.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/ronaldo3.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/ronaldo4.jpeg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/ronaldo5.jpeg"))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5] # list of all images

img_label = Label(root, image=my_img1)
img_label.grid(row=0, column=0, columnspan=3)

# functions for previous and next buttons
def forward(image_number):
    global img_list, img_label, btn_forward, btn_back

    img_label.grid_forget() # removes previous image

    # update image 
    img_label = Label(root, image=img_list[image_number-1])
    img_label.grid(row=0, column=0, columnspan=3)

    # update forward button
    btn_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    btn_forward.grid(row=1, column=2)
    
    # update back button 
    btn_back = Button(root, text="<<", command=lambda: back(image_number-1))
    btn_back.grid(row=1, column=0)

    # when image_number == 5 disable forward button 
    if image_number == 5:
        btn_forward = Button(root, text=">>", state=DISABLED)
        btn_forward.grid(row=1, column=2)
    
    # update status bar 
    status = Label(root, text=f"Image {image_number} of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
def back(image_number):
    global img_list, img_label, btn_forward, btn_back
    
    img_label.grid_forget()
    
    # update image 
    img_label = Label(root, image=img_list[image_number-1])
    img_label.grid(row=0, column=0, columnspan=3)

    # update forward button
    btn_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    btn_forward.grid(row=1, column=2)
    
    # update back button
    btn_back = Button(root, text="<<", command=lambda: back(image_number-1))
    btn_back.grid(row=1, column=0)

    # when image_number == 1 disable back button 
    if image_number == 1:
        btn_back = Button(root, text="<<", state=DISABLED)
        btn_back.grid(row=1, column=0)

    # update status bar 
    status = Label(root, text=f"Image {image_number} of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Buttons to show next and previous image
btn_back = Button(root, text="<<", state=DISABLED, command=lambda: back())
btn_close = Button(root, text="Exit Program", command=root.quit) # exit the program
btn_forward = Button(root, text=">>", command=lambda: forward(2))

btn_back.grid(row=1, column=0)
btn_close.grid(row=1, column=1)
btn_forward.grid(row=1, column=2, pady=10)

# STATUS BAR
status = Label(root, text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()