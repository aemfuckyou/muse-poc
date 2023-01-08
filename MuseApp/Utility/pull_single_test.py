"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream, local_clock
from datetime import datetime
from time import time


def read_stream(self):
    # first resolve an EEG stream on the lab network
    #print('looking for an EEG stream...')
    streams = resolve_stream('type', 'EEG')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    while True:
        #print(self.manager.stop.is_set())
        if self.manager.stop.is_set():
            return
        sample, timestamp = inlet.pull_sample()
        timestamp = datetime.fromtimestamp(time())

        #print(timestamp, sample)
        #print(type(timestamp))
        #print(type(sample[0]))
