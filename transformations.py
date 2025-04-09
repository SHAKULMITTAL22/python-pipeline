# transformations.py
from pyflink.common import TypeInformation
from pyflink.datastream.functions import MapFunction, FlatMapFunction, FilterFunction, ReduceFunction, KeySelector, ProcessFunction, RuntimeContext

class MultiplyByTwo(MapFunction):
    def map(self, value):
        return value * 2

class ExpandToRange(FlatMapFunction):
    def flat_map(self, value):
        for i in range(value):
            yield i

class IsEven(FilterFunction):
    def filter(self, value):
        return value % 2 == 0

class ModuloKeySelector(KeySelector):
    def get_key(self, value):
        return value % 2  # Group by even/odd

class SumReducer(ReduceFunction):
    def reduce(self, value1, value2):
        return value1 + value2

class CustomProcessFunction(ProcessFunction):
    def process_element(self, value, ctx):
        yield f"Element: {value}, Timestamp: {ctx.timestamp()}"
