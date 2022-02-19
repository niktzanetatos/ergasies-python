import json

def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

with open('askisi7.txt') as file:
    for line in file:
        k=json.loads(line)

print('Τα keys του dictionary ειναι',k.keys())
print('Για ποιο κλειδί ενδιαφέρεσαι να μάθεις τις πληροφορίες του;')
yourkey=input()

max=k[yourkey]
min=k[yourkey]
lista=[]
with open('opa.txt') as file:
     for line in file:
      k = json.loads(line)
      lista.append(k[yourkey])


lista.sort()
print('Η μεγαλυτερη τιμη του ',yourkey,'ειναι: ',lista[-1:])
print('Η μικρότρερη τιμη του ',yourkey,'ειναι: ',lista[0])
print('Η δημοφιλέστερη τιμή είναι:',most_frequent(lista))
