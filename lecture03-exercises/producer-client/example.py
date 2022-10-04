<<<<<<< HEAD
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
=======
from operator import truediv
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='kafka:9092')
exit = False
while not exit:
    input = input()
    if(input == "exit"):
        exit == True
        break
    producer.send('foobar', )
for _ in range(100):
   
>>>>>>> upstream/main
