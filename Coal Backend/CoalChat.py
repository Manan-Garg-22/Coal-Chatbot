#Run this Fourth
import random
import json
import torch
from CoalNeural import NeuralNetwork
from Coalnltk import bag_of_words, token, stem
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

f=open('Responses.json','r')
intents=json.load(f)
File="data.pth"
data=torch.load(File)

input_size = data["input_size"]
HiddenSize = data["hidden_size"]
output_size = data["output_size"]
AllWords = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNetwork(input_size, HiddenSize, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Coal Mitra 2.0"
print("Ask me any Query related to our Acts! else you can type 'quit' to exit :)")
while True:
    
    sentence = input("You: ")
    if sentence == "quit" or sentence == "Quit" or sentence == "QUIT" or sentence == "QuiT":
        print("Thank you! You can ask more questions.")
        break

    sentence = token(sentence)
    X = bag_of_words(sentence, AllWords)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand...")