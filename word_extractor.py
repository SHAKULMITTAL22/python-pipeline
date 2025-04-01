import unittest
from pyflink.datastream.functions import FlatMapFunction

# Custom FlatMapFunction that splits a sentence into individual words.
class WordExtractor(FlatMapFunction):
    def flat_map(self, value, collector):
        for word in value.split():
            collector.collect(word)

# Dummy collector to simulate Flink's collector interface.
class DummyCollector:
    def __init__(self):
        self.items = []
    def collect(self, item):
        self.items.append(item)

class TestWordExtractor(unittest.TestCase):

    def test_word_extraction(self):
        extractor = WordExtractor()
        collector = DummyCollector()  # Use our dummy collector.
        extractor.flat_map("Apache Flink is awesome", collector)
        expected_words = ["Apache", "Flink", "is", "awesome"]
        self.assertEqual(collector.items, expected_words)

if __name__ == '__main__':
    unittest.main()
