from pywinauto import application

def run_desktop_task():
    # Abre el Bloc de notas
    app = application.Application().start("notepad.exe")
    
    # Selecciona la ventana del Bloc de notas
    notepad = app['Untitled - Notepad']
    
    # Escribe algo en el Bloc de notas
    notepad.edit.type_keys("Hola, esto es una prueba de Pywinauto!", with_spaces=True)
    
    # Guarda el archivo (Ctrl+S)
    notepad.menu_select("File -> Save As")
    app.SaveAs.edit.set_text("example_notepad.txt")
    app.SaveAs.Save.click()
