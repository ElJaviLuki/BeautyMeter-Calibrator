import os
from tkinter import Tk, Label, Button, StringVar
from PIL import Image, ImageTk

# Path to the folder containing the images to classify
folder_path = "./imgs"

# List of custom criteria
criteria = ["HOT", "AVERAGE", "UGLY"]

# Function to display the next image
def show_next_image():
    global current_image_index
    global image_label
    global label_text

    if current_image_index < len(images):
        image_path = images[current_image_index]
        img = Image.open(image_path)
        ratio = 640/img.height.real
        img = img.resize((int(img.width.real*ratio), int(img.height.real*ratio)))
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
        label_text.set(f"Classify the image {image_path} as: ")

        current_image_index += 1
    else:
        root.quit()

# Function to classify the current image according to the selected criterion
def classify_image(criterion):
    global current_image_index
    with open("dataset.txt", "a") as file:
        file.write(f"{images[current_image_index - 1]}: {criterion}\n")
    show_next_image()

root = Tk()
root.title("BeautyMeter Calibrator")

images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
current_image_index = 0

image_label = Label(root)
image_label.pack()

label_text = StringVar()
label = Label(root, textvariable=label_text)
label.pack()

for criterion in criteria:
    button = Button(root, text=criterion, command=lambda c=criterion: classify_image(c))
    button.pack()

show_next_image()
root.mainloop()
