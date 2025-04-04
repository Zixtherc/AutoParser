'''
    `Модуль`, который вмещает в себя класс `Button`
'''
# Необходимый модуль для работы GUI
import customtkinter as ctk

class Button(ctk.CTkButton):
    '''
    ### Класс который позволит нам создавать `Button` используя `наследование` ###
    '''
    def __init__(self, ch_master: object,  text: str, ch_fg_color: str,
                ch_hover_color: str = '#373535', size: float = 20,
                ch_corner_radius: int = 10, ch_command : object = None,
                icon_name: str = None,
                **kwargs):
        '''
        #### Метод `конструктор` который принимает в себя параметры: ####

        - `ch_master`: Объект главного окна;
        - `icon_name`: Название файла из папки `static/icons/` для иконки;
        - `text`: Текст на кнопке;
        - `ch_fg_color`: Цвет самой `кнопки`;
        - `ch_hover_color`: Цвет `кнопки` при `наведении мыши`;
        - `size`: Размер `кнопки`;
        - `ch_corner_radius`: Радиус `скругления` углов `кнопки`;
        - `ch_command`: Команда, которая будет выполняться `при нажатии` на `кнопку`;
        - `kwargs`: Дополнительные параметры для `кнопки` (например, `font`, `border_width`, `padding`)

        Пример использования:
        ```python 
        button = Button(self.frames["HEADER"], "logout.png", "Выйти", "#ffffff", "#373535", 25, 10, command=self.logout)
        ```
        '''
        # Создаём атрибуты класса

        # Атрибут, который отвечает за название иконки
        self.ICON_NAME = icon_name
        # Атрибут, который отвечает за размер, выглядит в виде tuple (кортеж, т.к параметр size, в ctk.CtkImage принимает исключительно tuple)
        self.SIZE = (int(size), int(size))
        # Атрибут, который отвечает за текст кнопки
        self.TEXT = text

        # Вызываем конструктор родительского класса (CTkButton) и передаём в него необходимые аргументы
        ctk.CTkButton.__init__(
            self,
            master = ch_master,
            # В параметр image передаём наш метод, он возвращает нужное нам разрешение
            image = None,
            text = self.TEXT,
            width = int(size),
            height = int(size),
            fg_color = ch_fg_color,
            hover_color = ch_hover_color,
            corner_radius = ch_corner_radius,
            command = ch_command,
            **kwargs)