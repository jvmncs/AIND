import numpy as np

from keras.models import Model
from keras.layers import Dense, Input
from keras.layers import LSTM
import keras

# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    """Takes a series and returns input/output pairs, 
    where input is a batch of window_size previous sequence elements"""
    output = np.zeros((len(series)-window_size+1,window_size+1))
    for i in range(len(series)-window_size+1):
        output[i,:window_size] = series[i:i+window_size]
        output[i,window_size] = series[i+window_size-1]
    return output[:,:-1], output[:,-1]

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    # given - fix random seed - so we can all reproduce the same results on our default time series
    np.random.seed(0)

    ins = Input(shape = (window_size,step_size,)
    x = LSTM(5)(ins)
    outs = Dense(1)(x)
    model = Model(ins,outs)

    # build model using keras documentation recommended optimizer initialization
    optimizer = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

    # compile the model
    model.compile(loss='mean_squared_error', optimizer=optimizer)
    return model

### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    unique = set(list(text))
    # remove as many non-english characters and character sequences as you can 
    for x in unique:
        if x in string.ascii_lowercase or x in [' ', '!', ',', '.', ':', ';', '?']:
            continue
        text = text.replace(x,' ')
    return text
    

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    inputs = [text[i:i+window_size] for i in range(len(text)-window_size) ]
    outputs =[text[i+window_size] for i in range(len(text)-window_size) ]
    return inputs,outputs
