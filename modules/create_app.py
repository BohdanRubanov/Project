import customtkinter 
import PIL
import modules.create_path as c_path
class App(customtkinter.CTk):
    def __init__(self, app_width, app_heigth):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_heigth
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        self.X = self.PC_SCREEN_WIDTH - self.APP_WIDTH + self.APP_WIDTH // 2
        self.Y = self.PC_SCREEN_HEIGHT - self.APP_HEIGHT
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.X}+{self.Y}")
        self.title("Додаток")
        self.resizable(False, False)
        self.IMAGE = customtkinter.CTkImage(
            dark_image = PIL.Image.open(c_path.create_path("img/1.jpg")),
            size = (self.APP_WIDTH, self.APP_HEIGHT)
        )
        self.IMAGE_LABEL = customtkinter.CTkLabel(master = self, text= "моя перша практична робота з customtkinter", image = self.IMAGE)
        self.IMAGE_LABEL.grid(row =1, column = 1)
app = App(app_width = 500, app_heigth= 400)

