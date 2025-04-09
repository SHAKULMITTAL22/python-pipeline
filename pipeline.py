# pipeline.py
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common import Types
from transformations import (
    MultiplyByTwo, ExpandToRange, IsEven,
    ModuloKeySelector, SumReducer, CustomProcessFunction
)

def run_pipeline(data):
    env = StreamExecutionEnvironment.get_execution_environment()
    ds = env.from_collection(data, type_info=Types.INT())

    # Apply map transformation
    ds = ds.map(MultiplyByTwo(), output_type=Types.INT())

    # Apply flat_map transformation
    ds = ds.flat_map(ExpandToRange(), output_type=Types.INT())

    # Apply filter transformation
    ds = ds.filter(IsEven())

    # Apply key_by and reduce transformation
    ds = ds.key_by(ModuloKeySelector(), key_type=Types.INT()) \
           .reduce(SumReducer())

    # Apply process function
    ds = ds.process(CustomProcessFunction(), output_type=Types.STRING())

    # Execute and collect results
    result = []
    for value in ds.execute_and_collect():
        result.append(value)
    return result

if __name__ == '__main__':
    data = [1, 2, 3, 4]
    output = run_pipeline(data)
    print("Pipeline Output:", output)
