# transformations.py
from pyflink.datastream.functions import MapFunction

class MultiplyByTwo(MapFunction):
    def map(self, value):
        # Multiply the incoming value by 2.
        return value * 2
