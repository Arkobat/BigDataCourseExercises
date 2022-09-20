from kafka import KafkaProducer

producer = KafkaProducer( 
    bootstrap_servers=['kafka:9092']
    )


  
# output
while True:
    # input
    string = str(input())
    string = string.encode('UTF-8')

    producer.send('foo', value=string)
    print(string)