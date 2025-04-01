# pipeline.py
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common import Types
from transformations import MultiplyByTwo

def run_pipeline(data):
    # Set up the streaming execution environment.
    env = StreamExecutionEnvironment.get_execution_environment()
    
    # Create a data stream from an in-memory collection.
    ds = env.from_collection(data, type_info=Types.INT())
    
    # Apply the MultiplyByTwo transformation.
    ds = ds.map(MultiplyByTwo(), output_type=Types.INT())
    
    # Execute the pipeline and collect results.
    result = []
    for value in ds.execute_and_collect():
        result.append(value)
    return result

if __name__ == '__main__':
    # Example run: Multiply each number in the list by 2.
    data = [1, 2, 3, 4]
    output = run_pipeline(data)
    print("Pipeline Output:", output)
