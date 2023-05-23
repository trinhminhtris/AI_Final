#%%
import tkinter as tk
from tkinter.ttk import Button, Label
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
from keras.utils import load_img
from keras.utils.image_utils import img_to_array
from PIL import ImageTk, Image
import tkinter.filedialog as fd

model1 = load_model('D:/Vehicle/Vehicle_train.h5')
        
nsx = ''
ten = ''
mau = ''
value = ''
img = 0
#plt.imshow(img)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vehicle Classification")
        self.geometry('600x400') # chỉnh kích thước của trang hiển thị
        self.ma_tran = None
        global img
        global model1
        global nsx
        global ten
        global mau
        global value
        
        self.nsx = tk.StringVar()
        self.ten = tk.StringVar()
        self.mau = tk.StringVar()

        lbl_nsx = tk.Label(self, text = 'Manufacturer')
        lbl_ten = tk.Label(self, text = 'Name')
        lbl_mau = tk.Label(self, text = 'Color')
        self.lbl_test = tk.Label(self, text = 'test')
        self.label = tk.Label(self, text = "Add Image", font = ('arial', 30))
        self.lbl_manufacturer = tk.Label(self, relief = tk.SUNKEN, font = ('Calibri', 12))
        self.lbl_name = tk.Label(self, relief = tk.SUNKEN, font = ('Calibri', 12))
        self.lbl_color = tk.Label(self, relief = tk.SUNKEN, font = ('Calibri', 12))
        
        btn_add = tk.Button(self, text = 'Add', width = 10, command = self.choose_file)
        btn_result = tk.Button(self, text = 'Result', width = 10, command = self.result)
        btn_clear = tk.Button(self, text = 'Clear', width = 10, command = self.clear)
        
        lbl_nsx.grid(row=0, column=0, padx = 350, pady = 10, sticky = tk.W) 
        lbl_ten.grid(row=1, column=0, padx = 350, pady = 10, sticky = tk.W) 
        lbl_mau.grid(row=2, column=0, padx = 350, pady = 10, sticky = tk.W)
        self.lbl_test.grid(row=3, column=0, padx = 350, pady = 10, sticky = tk.W)
        self.label.place(x = 10, y = 10)
        self.lbl_manufacturer.place(x = 450, y = 10)
        self.lbl_name.place(x = 450, y = 50)
        self.lbl_color.place(x = 450, y = 90)
        
        btn_add.place(x = 20, y = 350)
        btn_result.place(x = 120, y = 350)
        btn_clear.place(x = 220, y = 350)
        
    def choose_file(self):
        global img
        #photo = Image.open('wave_den_4.jpg')
        #photo = photo.resize((300, 300))
        #img = ImageTk.PhotoImage(photo)
        #self.label.configure(image = img)
        #self.label.image = img
        try:
            filename = fd.askopenfilename(initialdir='D:\Vehicle\test',filetypes=[("Images", "*.jpg, *.gif, *.png")])
            photo = Image.open(filename)
            photo = photo.resize((300,300))
            render = ImageTk.PhotoImage(photo)
            img = load_img(filename, target_size = (300,300))
            plt.imshow(img)
            img = img_to_array(img)
            img = img.reshape(1,300,300,3)
            img = img.astype('float32')
            img =img/255
            self.label.configure(image = render)
            self.label.image = render
        except:pass
    
    def result(self):
        global model1
        global img
        global nsx
        global ten
        global mau
        global value
        
        vat = {1: 'Honda Vision Black', 2:'Honda Vision Red', 3:'Honda Vision White', 
               4:'Honda WaveAlpha Black', 5:'Honda WaveAlpha Red', 6:'Honda WaveAlpha White',
               7:'Honda WinnerX Black', 8:'Honda WinnerX Red',
               9:'Yamaha Exciter Black', 10:'Yamaha Exciter Blue', 11:'Yamaha Exciter Red',
               12:'Yamaha Janus Black', 13:'Yamaha Yanus Red', 14:'Yamaha Janus White',
               15:'Yamaha Sirius Black', 16:'Yamaha Sirius Red', 17:'Yamaha Sirius White'}
        
        ket_qua  = np.argmax(model1.predict(img),axis=1)
        self.lbl_test.configure(text='{}'.format(vat[ket_qua[0]]))
        
        value = '{}'.format(vat[ket_qua[0]])
        if value.startswith('Honda'):
            nsx = 'Honda' 
        
        if value.startswith('Yamaha'):
            nsx = 'Yamaha'
        
        if value == 'Yamaha Exciter Blue':
            color = 'Blue'
            
        str1 = {'Honda Vision Black', 'Honda Vision Red', 'Honda Vision White'}
        if value in str1:
            name = 'Vision'
            
        str2 = {'Honda WaveAlpha Black', 'Honda WaveAlpha Red', 'Honda WaveAlpha White'}
        if value in str2:
            name = 'Wave Alpha'
        
        str3 = {'Honda WinnerX Black', 'Honda WinnerX Red'}
        if value in str3:
            name = 'Winner X'
        
        str4 = {'Yamaha Exciter Black', 'Yamaha Exciter Blue', 'Yamaha Exciter Red'}
        if value in str4:
            name = 'Exciter'
        
        str5 = {'Yamaha Janus Black', 'Yamaha Yanus Red', 'Yamaha Janus White'}
        if value in str5:
            name = 'Janus'
        
        str6 = {'Yamaha Sirius Black', 'Yamaha Sirius Red', 'Yamaha Sirius White'}
        if value in str6:
            name = 'Sirius'
            
        str7 = {'Honda Vision Black', 'Honda WaveAlpha Black', 'Honda WinnerX Black', 'Yamaha Exciter Black', 'Yamaha Janus Black', 'Yamaha Sirius Black'}
        if value in str7:
            color = 'Black'
            
        str8 = {'Honda Vision Red', 'Honda WaveAlpha Red', 'Honda WinnerX Red', 'Yamaha Exciter Red', 'Yamaha Janus Red', 'Yamaha Sirius Red'}
        if value in str8:
            color = 'Red'
        
        str9 = {'Honda Vision White', 'Honda WaveAlpha White', 'Yamaha Janus White', 'Yamaha Sirius White'}
        if value in str9:
            color = 'White'
        
        self.lbl_manufacturer.configure(text = nsx)
        self.lbl_name.configure(text = name)
        self.lbl_color.configure(text = color)
        
    def clear(self):
       self.label.destroy()
       self.label = tk.Label(self, text = "Add Image", font = ('arial', 30))
       self.label.place(x = 10, y = 10)
       self.lbl_manufacturer.configure(text = '')
       self.lbl_name.configure(text = '')
       self.lbl_color.configure(text = '')
       self.lbl_test.configure(text='test')

if __name__ == "__main__":
    app = App()
    app.mainloop()
# %%
