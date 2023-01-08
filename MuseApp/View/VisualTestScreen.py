import Controller as c
import Model as m
import threading
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock, mainthread
from View import CountdownTimer, ScrollableLabel
from Utility.observer import Observer
from Utility.pull_single_test import read_stream
from kivy.properties import ObjectProperty, NumericProperty
from pylsl import StreamInlet, resolve_byprop
from datetime import datetime
from time import time


class VisualTestPage (MDScreen, Observer):

    reading_time = NumericProperty(300)
    #<Controller.visualtestscreen.VisualTestController object>
    controller = ObjectProperty()
    #<Model.visualtestscreen.VisualTestModel object>
    model = ObjectProperty()

    dialog = None
    dismissbutton = None
    reading_time_schedule = None


    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self) #register the view as an observer
        self.timerlabel = CountdownTimer.CountDownLbl()
        self.ids.layout.add_widget(self.timerlabel)
        Clock.schedule_once(self.start_time_elapsed, 5.42)
        self.dismissbutton = MDFlatButton(
                        text="OK",
                        theme_text_color="Custom"
                    )

    @mainthread
    def start_time_elapsed(self, dt):
        self.ids.layout.remove_widget(self.timerlabel)
        self.controller.load_text()

    @mainthread
    def model_is_changed(self):
        view = ScrollableLabel.ScrollableLabel(text=self.model.reading_text[:11634])
        self.ids.layout.add_widget(view)
        self.reading_time_schedule = Clock.schedule_once(self.reading_time_elapsed, self.reading_time)
        threading.Thread(target=self.read_stream).start()

    @mainthread
    def reading_time_elapsed(self, dt):
        self.manager.stop.set()
        #self.model.create_visual_test()
        self.model.save_raw_data_entries()
        self.show_test_done_dialog()
        

    def read_stream(self):
        # TODO rewrite first resolve an EEG stream on the lab network
        print('looking for an EEG stream...')
        streams = resolve_byprop('type', 'EEG', timeout=2)

        # create a new inlet to read from the stream#
        if len(streams) == 0:
            self.show_alert_dialog()
            self.reading_time_schedule.cancel()
            return
        inlet = StreamInlet(streams[0])

        print('Stream found')
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        while True:
            if self.manager.stop.is_set():
                inlet.close_stream()
                return
            sample, timestamp = inlet.pull_sample()
            timestamp = datetime.fromtimestamp(timestamp)

            #self.model.save_raw_data_etry(timestamp, sample)
            self.model.raw_data.append((timestamp,) + 
                                        (sample[0],) + 
                                        (sample[1],) + 
                                        (sample[2],) + 
                                        (sample[3],) + 
                                        (sample[4],))

    @mainthread
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="No EEG stream found, check your Muse headband and retry.",
                buttons=[self.dismissbutton],
                on_dismiss = self.back_to_choose_menu
            )
            self.dismissbutton.bind(on_press=self.dialog.dismiss)
        self.dialog.open()
        
    @mainthread
    def show_test_done_dialog(self):
        self.dialog = MDDialog(
            text="Test done.",
            buttons=[self.dismissbutton],
            on_dismiss = self.back_to_choose_menu
        )
        self.dismissbutton.bind(on_press=self.dialog.dismiss)
        self.dialog.open()

    @mainthread
    def back_to_choose_menu(self, *args):
        self.model = m.choosetestscreen.ChooseTestModel(self.model.user)
        self.controller = c.choosetestscreen.ChooseTestController(self.model)
        self.manager.switch_to(self.controller.get_screen(), direction="right")


    Builder.load_file('View/visualtestscreen.kv')
