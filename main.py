# Импортируем всё гуи, можно тольк app
import modules.GUI

# Если мы запускаем этот модуль как основной
if __name__ == "__main__":
    try:
        # Запускаем главное окно приложения
        modules.app.mainloop()
    # Если была нажата клавиша прерывания, выходим из приложения
    except KeyboardInterrupt:
        print("Shutting down")