import Controller as c
import Model as m
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from Utility.graphgenerator import GraphGenerator
from Utility.observer import Observer
from kivy.properties import ObjectProperty
import kivy_matplotlib_widget


class PlotTestPage (MDScreen, Observer):

    #<Controller.plottestscreen.PlotTestController object>
    controller = ObjectProperty()
    #<Model.plottestscreen.PlotTestModel object>
    model = ObjectProperty()

    dialog = None
    dismissbutton = None
    reading_time_schedule = None



    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self) #register the view as an observer
        mygraph = GraphGenerator(self.model.transformed_vectors_mean)
        self.lines = []
        
        self.ids.figure_wgt.figure = mygraph.fig
        self.ids.figure_wgt.axes = mygraph.ax1
        self.ids.figure_wgt.xmin = mygraph.xmin
        self.ids.figure_wgt.xmax = mygraph.xmax
        self.ids.figure_wgt.ymin = mygraph.ymin
        self.ids.figure_wgt.ymax = mygraph.ymax
        self.ids.figure_wgt.fast_draw = False #update axis during pan/zoom
        
        #register lines instance if need to be update
        self.lines.append(mygraph.line1)
        self.lines.append(mygraph.line2)
        self.lines.append(mygraph.line3)
        self.lines.append(mygraph.line4)

        self.ids.figure_wgt.register_lines(self.lines)

        self.ids.legend_wgt.set_data(self.lines)


    def model_is_changed(self):
        pass 


    def back_to_choose_menu(self, *args):
        self.model = m.chooseresultscreen.ChooseResultModel(self.model.user)
        self.controller = c.chooseresultscreen.ChooseResultController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="right")


    def set_touch_mode(self,mode):
        self.ids.figure_wgt.touch_mode=mode

    def home(self):
        self.ids.figure_wgt.home()


    Builder.load_file('View/plottestscreen.kv')
