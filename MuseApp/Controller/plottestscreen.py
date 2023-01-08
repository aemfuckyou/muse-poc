from View.PlotTestScreen import PlotTestPage

class PlotTestController:

    def __init__(self, model):
        self.model = model
        self.view = PlotTestPage(controller=self, model=self.model)

    def get_all_tests(self):
        self.model.get_all_tests()

    def get_screen(self):
        return self.view

    def load_text(self):
        self.model.load_text()
