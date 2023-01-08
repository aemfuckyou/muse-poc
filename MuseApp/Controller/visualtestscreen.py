from View.VisualTestScreen import VisualTestPage

class VisualTestController:

    def __init__(self, model):
        self.model = model
        self.view = VisualTestPage(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def load_text(self):
        self.model.load_text()
