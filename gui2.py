from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
from test_lineas import detectaObstaculos, determinaROI, procesaFrame
video = None
video2 = None
video3 = None


def carga_video():
    global video
    global video2
    global video3

    if video is not None:
        lbl_video.image = ""
        video.release()   
        video = None  

        lbl_video2.image = ""
        video2.release()   
        video2 = None

        lbl_video3.image = ""
        video3.release()   
        video3 = None

    video_path = filedialog.askopenfilename(filetypes= [("Archivos MP4", ".mp4"), ("Archivos AVI", ".avi")])
    if(len(video_path)>0):
        lbl_info2.configure(text=video_path.split("/")[-1])
        video = cv2.VideoCapture(video_path)
        video2 = cv2.VideoCapture(video_path)
        video3 = cv2.VideoCapture(video_path)


        muestra_video()
        muestra_video2()
        muestra_video3()
    else:
        lbl_info2.configure(text="No se ha seleccionado un vídeo todavía")

def muestra_video():
    global video
    if video is not None:

        ret, frame = video.read()
        if(ret == True):
            frame = procesaFrame(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image = im)

            lbl_video2.configure(image = img)
            lbl_video2.image = img
            lbl_video2.after(16, muestra_video)

        else:
            lbl_info2.configure(text="No se ha seleccionado un vídeo todavía")
            lbl_video2.image = ""
            video.release()        

def muestra_video2():
    global video2
    if video2 is not None:

        ret, frame = video2.read()
        if(ret == True):
            frame = detectaObstaculos(frame, frame)[1]
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image = im)

            lbl_video3.configure(image = img)
            lbl_video3.image = img
            lbl_video3.after(16, muestra_video2)

        else:
            lbl_info2.configure(text="No se ha seleccionado un vídeo todavía")
            lbl_video3.image = ""
            video2.release()       

def muestra_video3():
    global video3
    if video3 is not None:

        ret, frame = video3.read()
        if(ret == True):
            frame = imutils.resize(frame, 640, 360)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image = im)

            lbl_video.configure(image = img)
            lbl_video.image = img
            lbl_video.after(16, muestra_video3)

        else:
            lbl_info2.configure(text="No se ha seleccionado un vídeo todavía")
            lbl_video.image = ""
            video3.release()        









ventana_principal = Tk()
ventana_principal.geometry()

btn_cargar_video = Button(ventana_principal, text="cargar un vídeo", command=carga_video)
btn_cargar_video.grid(column=0, row=0, padx=5, pady=5, columnspan=2)

lbl_info1 = Label(ventana_principal, text= "Vídeo seleccionado: ")
lbl_info1.grid(column=0, row=1, padx=5, pady=5)

lbl_info2= Label(ventana_principal, text= "No se ha seleccionado un vídeo todavía")
lbl_info2.grid(column=1, row=1, padx=5, pady=5)

lbl_video = Label(ventana_principal)
lbl_video.grid(column=1, row=2, columnspan=2)

lbl_video2 = Label(ventana_principal)
lbl_video2.grid(column=0, row=3, columnspan=2)

lbl_video3 = Label(ventana_principal)
lbl_video3.grid(column=2, row=3, columnspan=2)

ventana_principal.mainloop()



