from tkinter import *
import psutil
import math
import speedtest
from PIL import Image, ImageTk

def usage():
    # CPU count (static, but you can keep it dynamic)
    cpu_count = psutil.cpu_count()
    cpu_count_label.config(text=cpu_count , image=tk_image,compound=('center'),fg='#00ffff')

    # CPU usage
    cpu_usage = psutil.cpu_percent(1)
    cpu_usage_label.config(text=f"{cpu_usage} %" , image=tk_image,compound=('center'),fg='#00ffff')

    # Total RAM in GB
    ram_total = math.floor(psutil.virtual_memory().total / 1_000_000_000)
    ram_count_label.config(text=f"{ram_total} GB" ,image=tk_image,compound=('center'),fg='#00ffff')


    # ram usage 
    ram_usage = psutil.virtual_memory().percent 
    ram_usage_label.config(text=f"{ram_usage} %",image=tk_image,compound=('center'),fg='#00ffff')

    #ram available
    ram_available = math.floor(psutil.virtual_memory().available / 1_000_000_000)
    ram_available_label.config(text=f"{ram_available} GB", image=tk_image,compound=('center'),fg='#00ffff')

    # Call this function again after 1 second
    root.after(100, usage)


def internet_speed():
    print("Testing internet speed")
    st = speedtest.Speedtest()  
    download_speed = f"{round(st.download() / 1_000_000, 2)} Mbps"
    upload_speed = f"{round(st.upload() / 1_000_000, 2)} Mbps"
    ping = f"{round(st.results.ping, 2)} ms"

    download_label.config(text=download_speed)
    upload_label.config(text=upload_speed)
    ping_label.config(text=ping)

                    




root = Tk()
root.config(bg='black')
image = Image.open('single.png')
tk_image = ImageTk.PhotoImage(image)

root.geometry("1580x980")
root.title("CPU Status")

# CPU count label
cpu_count_label = Label(root,font=("Orbitron",40,'bold'), text="0",bd = -2)
cpu_count_label.grid(row=0, column=0)
label_01 = Label(root,font=("Orbitron",20,'bold'),bg= 'black', fg='#fcba03', text="CPUs" )
label_01.grid(row=1, column=0)

# CPU usage label
cpu_usage_label = Label(root,font=("Orbitron",40,'bold'), text="0",bd= -2)
cpu_usage_label.grid(row=0, column=1)
label_02 = Label(root,font=("Orbitron",20,'bold'),bg= 'black', fg='#fcba03', text="CPU usage in %")
label_02.grid(row=1, column=1)

# RAM total label
ram_count_label = Label(root,font=("Orbitron",40,'bold'), text="0",bd= -2)
ram_count_label.grid(row=0, column=2)
label_03 = Label(root,font=("Orbitron",20,'bold'),bg= 'black', fg='#fcba03', text="Available RAM")
label_03.grid(row=1, column=2)

#ram % usages 
ram_usage_label = Label(root,font=("Orbitron",40,'bold'), text="0",bd= -2)
ram_usage_label.grid(row=0, column=3)
label_04 = Label(root,font=("Orbitron",20,'bold'),bg= 'black', fg='#fcba03', text="Ram Use")
label_04.grid(row=1, column=3)

#available ram 
ram_available_label = Label(root,font=("Orbitron",40,'bold'), text="0",bd= -2)
ram_available_label.grid(row=0, column=4)
label_05 = Label(root, font=("Orbitron",20,'bold'),bg= 'black', fg='#fcba03', text="Ram Available")
label_05.grid(row=1, column=4)

#speed btn 
#speed_button = Button(root,  text="Test internet speed", command = internet_speed , height=3 , width = 15 ,font=("Orbitron",20,'bold'))
#speed_button.grid(row=3, column=0)

speed_button = Button(
    root,
    text="Test internet speed",
    command=internet_speed,
    height=2,
    width=18,
    font=("Orbitron", 16, "bold"),
    bg="#1f1f1f",            # Background color
    fg="#ffffff",            # Text color
    activebackground="#333333",  # Background on click
    activeforeground="#00ffcc",  # Text on click
    bd=4,                    # Border width
    relief="ridge",          # Border style: flat, groove, raised, ridge, sunken
    cursor="hand2"           # Changes mouse cursor on hover
)
speed_button.grid(row=5, column=2, pady=20)

download_label = Label(root, font=("Orbitron",22,'bold'), text="0 MB/s" , image=tk_image,compound=('center'),fg='#00ffff',bd= -2)
download_label.grid(row = 3 ,column=1)
label_06 = Label(root,font=("Orbitron",20,'bold'),bg= 'black', fg='#fcba03', text="Download Speed")
label_06.grid(row=4, column=1)

upload_label = Label(root,font=("Orbitron",22,'bold'), text="0 MB/s" , image=tk_image,compound=('center'),fg='#00ffff',bd= -2)
upload_label.grid(row = 3 ,column=2)
label_07 = Label(root,font=("Orbitron",20,'bold'),bg= 'black', fg='#fcba03', text="Upload Speed")
label_07.grid(row=4, column=2)

ping_label = Label(root,font=("Orbitron",22,'bold'), text="0 ms", image=tk_image,compound=('center'),fg='#00ffff',bd= -2)
ping_label.grid(row = 3 ,column=3)
label_08 = Label(root,font=("Orbitron",20,'bold'),bg= 'black', fg='#fcba03', text="Ping")
label_08.grid(row=4, column=3)

usage()
root.mainloop()
