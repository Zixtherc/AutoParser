import customtkinter as ctk
import time

class EntryText(ctk.CTkEntry):
    '''
    ### Класс который позволит нам создавать поле ввода текста ###
    '''
    def __init__(self, ch_master: object, ch_width: int, ch_height: int, ch_fg_color: str,
                ch_corner_radius: int, ch_border_width: int, ch_placeholder_text: str, 
                font_size: int, font_name: str = "Arial", ch_placeholder_text_color : str = "#000000",ch_text_color : str = "#000000",**kwargs):
        ctk.CTkEntry.__init__(
            self,
            master = ch_master,
            width = ch_width,
            height = ch_height,
            fg_color = ch_fg_color,
            corner_radius = ch_corner_radius,
            border_width = ch_border_width,
            placeholder_text = ch_placeholder_text,
            font=(font_name, font_size, "bold"),
            placeholder_text_color = ch_placeholder_text_color,
            text_color = ch_text_color,
            **kwargs)