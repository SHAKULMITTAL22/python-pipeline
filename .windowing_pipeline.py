from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.common.typeinfo import Types
from pyflink.common.watermark_strategy import WatermarkStrategy
from datetime import datetime, timedelta

def run_pipeline():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Sample data with timestamps
    data = [
        ('Alice', 5, datetime.now().timestamp()),
        ('Bob', 2, datetime.now().timestamp()),
        ('Alice', 3, (datetime.now() + timedelta(seconds=10)).timestamp()),
        ('Bob', 7, (datetime.now() + timedelta(seconds=10)).timestamp()),
    ]

    ds = env.from_collection(data, type_info=Types.TUPLE([Types.STRING(), Types.INT(), Types.FLOAT()]))

    # Correct Watermark Strategy with timedelta conversion
    watermark_strategy = WatermarkStrategy.for_bounded_out_of_orderness(timedelta(seconds=5))

    ds.assign_timestamps_and_watermarks(watermark_strategy) \
      .key_by(lambda x: x[0]) \
      .window(TumblingEventTimeWindows.of(int(timedelta(seconds=15).total_seconds() * 1000))) \
      .reduce(lambda a, b: (a[0], a[1] + b[1], a[2])) \
      .print()

    env.execute("Windowing Example")

if __name__ == "__main__":
    run_pipeline()
