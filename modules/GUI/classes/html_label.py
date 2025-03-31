import customtkinter as ctk
import tkhtmlview

class HtmlLabel(tkhtmlview.HTMLLabel):
    '''
    ### Класс который позволит нам создавать `Label` с поддержкой HTML ###
    '''
    def __init__(self, ch_master: object, ch_html_text: str, ch_width: int, ch_height: int, ch_fg_color: str, 
                 ch_text_color: str, ch_relief='groove', ch_borderwidth: int = 3, ch_cursor: str = 'hand2', **kwargs):
        '''
        #### Метод `конструктор`, который принимает в себя параметры: ####

        - `ch_master:` `Объект` главного окна;
        - `ch_html_text:` Текст в виде `HTML`;
        - `ch_width:` Ширина `Label`;
        - `ch_height:` Высота `Label`;
        - `ch_fg_color:` Цвет фона `Label`;
        - `ch_text_color:` Цвет текста `Label`;
        - `ch_relief:` Тип границы `Label` ('groove', 'raised', 'sunken', 'flat');
        - `ch_borderwidth:` Толщина границы `Label`;
        - `ch_cursor:` Тип курсора при наведении мыши ('arrow', 'hand2')

        Пример использования:
            
        '''
        # Явный вызов конструктора родителя
        tkhtmlview.HTMLLabel.__init__(
            self,
            master = ch_master,
            html = ch_html_text,
            width = ch_width,
            height = ch_height,
            background = ch_fg_color,
            fg = ch_text_color,
            relief = ch_relief,
            borderwidth = ch_borderwidth,
            cursor = ch_cursor,
            **kwargs
        )