import json
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream.connectors import FlinkKafkaConsumer, FlinkKafkaProducer

def detect_fraud(transaction):
    """
    Simple fraud detection function.
    Flags a transaction as suspicious if the amount exceeds a threshold.
    In a real-world scenario, this could be replaced or augmented by a machine learning model.
    """
    # For example, mark transactions over 10,000 as suspicious
    transaction['fraud'] = transaction.get('amount', 0) > 10000
    return transaction

def main():
    # Create the execution environment
    env = StreamExecutionEnvironment.get_execution_environment()

    # Define Kafka properties
    kafka_props = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'transaction-group'
    }

    # Create a Kafka consumer to read transactions from the "transactions" topic.
    consumer = FlinkKafkaConsumer(
        topics='transactions',
        deserialization_schema=SimpleStringSchema(),
        properties=kafka_props
    )
    
    # Create a Kafka producer to send alerts to the "alerts" topic.
    producer = FlinkKafkaProducer(
        topic='alerts',
        serialization_schema=SimpleStringSchema(),
        producer_config=kafka_props
    )
    
    # Ingest the data stream
    stream = env.add_source(consumer)
    
    # Process the stream:
    # 1. Parse each record from JSON string to a Python dictionary.
    # 2. Apply the fraud detection logic.
    # 3. Filter only the suspicious transactions.
    # 4. Convert the alert record back to a JSON string.
    processed_stream = stream.map(lambda x: json.loads(x)) \
                             .map(detect_fraud) \
                             .filter(lambda txn: txn.get('fraud')) \
                             .map(lambda txn: json.dumps(txn))
    
    # Send the flagged transactions to the alerts topic.
    processed_stream.add_sink(producer)
    
    # Execute the pipeline
    env.execute("Real-Time Fraud Detection Pipeline")

if __name__ == '__main__':
    main()
