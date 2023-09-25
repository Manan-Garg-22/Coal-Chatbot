#Run this Second
import torch
import torch.nn as Neural
class NeuralNetwork(Neural.Module):
    def __init__(self, input_size, HiddenSize, No_Classes):
        super(NeuralNetwork, self).__init__()
        self.Layer1=Neural.Linear(input_size, HiddenSize)
        self.Layer2=Neural.Linear(HiddenSize, HiddenSize)
        self.Layer3=Neural.Linear(HiddenSize, No_Classes)
        self.relu=Neural.ReLU()

    def forward(self, x):
        out=self.Layer1(x)
        out=self.relu(out)
        out=self.Layer2(out)
        out=self.relu(out)
        out=self.Layer3(out)
        return out