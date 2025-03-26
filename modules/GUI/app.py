import customtkinter as ctk

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
app = App()
app.mainloop()