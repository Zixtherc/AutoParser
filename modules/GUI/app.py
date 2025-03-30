import customtkinter as ctk

from .classes.button import Button
from .classes.entry import EntryText
from .classes.frame import Frame

class App(ctk.CTk):
    '''
    
    ### Основной `экран` нашего приложение, на `нём` мы будем `размещать` наши `Frame` ###
    '''
    # В будущем буду использовать ctk.set_appearance_mode("light")
    def __init__(self):
        
        ctk.CTk.__init__(self, fg_color = '#888888')

        self.WIDTH = int(self.winfo_screenwidth() )

        self.HEIGHT = int(self.winfo_screenheight() )

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.title("Your Reminder!")
        self.resizable(False, False)
        
        # Список всех наших Frame
        self.frames = {}
        self.entry = {}
        self.label = {}

        self.header()

    def header(self):

        self.frames['HEADER'] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = '#f2d5ff'
        )
        self.frames['HEADER'].place(x = 0, y = 0)
app = App()
app.mainloop()