#Run this Third
import json
import numpy as num
import string
import random
#from nltkFunctions import token, stem, bag_of_words 
#use above from, if nltkFunc and nltkTrain files are separate
import torch
import torch.nn as Neural
from torch.utils.data import Dataset, DataLoader
from Coalnltk import bag_of_words, token, stem
from CoalNeural import NeuralNetwork

with open('Responses.json', 'r') as file:
    intents=json.load(file)
#print(intents)

AllWords=[]  
tags=[]
Q_to_Tag=[]

for int in intents['intents']:
    t=int['tag']
    tags.append(t)
    for pattern in int['patterns']:
        w=token(pattern) 
        AllWords.extend(w)
        Q_to_Tag.append((w,t))

punctuate=string.punctuation     #string consist of all punctuations
remove_punctuation=[*punctuate]  #convert string to list of punctuations
AllWords=[stem(w) for w in AllWords if w not in remove_punctuation]

AllWords=sorted(set(AllWords))
tags=sorted(set(tags))
#print(AllWords)
#print(tags)


Q_train=[]
Tag_train=[]
for(m,t) in Q_to_Tag:
    bag=bag_of_words(m,AllWords)
    Q_train.append(bag)
    label=tags.index(t)
    Tag_train.append(label)

Q_train=num.array(Q_train)
Tag_train=num.array(Tag_train)
#print(Q_train)
#print(Tag_train)


input_size=len(Q_train[0])
output_size=len(tags)
batch_size=8
HiddenSize=8
num_epochs=1000
learningRate = 0.001
#print(input_size,output_size)

class ChatDataset(Dataset):
    def __init__(self):
        self.No_of_samples=len(Q_train)
        self.Q_data=Q_train
        self.Tag_data=Tag_train

    def __len__(self):
        return self.No_of_samples
    
    def __getitem__(self, index):
        return self.Q_data[index], self.Tag_data[index]
        

dataset = ChatDataset()
train_loader=DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model=NeuralNetwork(input_size, HiddenSize, output_size).to(device)

crit=Neural.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)

for e in range(num_epochs):
    for(words, labels) in train_loader:
        words=words.to(device)
        labels=labels.to(dtype=torch.long).to(device)

        outputs=model(words)
        loss=crit(outputs,labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if(e+1)%100==0:
        print(f'Epoch[{e+1}/{num_epochs}], Loss:{loss.item():.4f}')
print(f'final loss:{loss.item():.4f}')

data={
    "model_state": model.state_dict(),
    "input_size": input_size,
    "hidden_size": HiddenSize,
    "output_size": output_size,
    "all_words": AllWords,
    "tags": tags
}

File="data.pth"
torch.save(data, File)
print(f'Training Done and File saved to {File}')