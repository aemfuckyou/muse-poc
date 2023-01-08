from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty

class CountDownLbl(Label):

    angle = NumericProperty(0)
    startCount = NumericProperty(5)
    Count = NumericProperty()

    def __init__(self, **kwargs):
        super(CountDownLbl, self).__init__(**kwargs)
        Clock.schedule_once(self.set_Circle, 0.1)
        self.Count = self.startCount

    def set_Circle(self, dt):
        self.angle = self.angle + dt*360
        if self.angle >= 360:
            self.angle = 0
            self.Count = self.Count - 1
        if self.Count > 0:
            Clock.schedule_once(self.set_Circle, 1.0/360)
    
    Builder.load_file('View/countdowntimer.kv')
