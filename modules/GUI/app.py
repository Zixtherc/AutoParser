import customtkinter as ctk

import asyncio

from .classes.button import Button
from .classes.entry import EntryText
from .classes.frame import Frame

from ..function_pars.parser import auto_parser


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
        self.button = {}

        self.header()

    def header(self):

        self.frames['HEADER'] = Frame(
            ch_master = self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT,
            ch_fg_color = '#f2d5ff'
        )
        self.frames['HEADER'].place(x = 0, y = 0)

        self.entry['URL'] = EntryText(
            ch_master = self.frames['HEADER'],
            ch_width = 300,
            ch_height = 2,
            ch_fg_color = '#f2d5ff',
            ch_corner_radius = 5,
            ch_border_width = 3,
            ch_placeholder_text = 'Hello',
            font_size = 13
        )
        self.entry['URL'].pack()

        self.button['PARSE'] = Button(
            ch_master = self.frames["HEADER"],
            text = "Login",
            ch_fg_color = "#61004f",
            size = 35,
            ch_command = lambda: asyncio.run(auto_parser(url = self.entry['URL'].get(), parse_mode = 'all'))
        )
        self.button['PARSE'].place(x=250, y=10)

app = App()
app.mainloop()