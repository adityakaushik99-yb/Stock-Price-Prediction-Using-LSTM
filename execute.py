from getdata import GetData
from preprocessing import PreProcessing 
from autoencoder import AutoEncoder 
from dataprocessing import DataProcessing 
from model import LSTM_Model

model = LSTM_Model(21, True)
model.make_train_model()