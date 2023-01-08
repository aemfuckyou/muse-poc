from View.MenuScreen import MenuPage

class MenuScreenController:

    def __init__(self, model):
        self.model = model
        self.view = MenuPage(controller=self, model=self.model)

    def get_screen(self):
        return self.view
