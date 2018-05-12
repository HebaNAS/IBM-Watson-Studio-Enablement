'''
    IBM Deep Learning (IDE) Generated Code.
    Compatible Keras Version : 2.1
    Tested on Python Version : 3.6.3
'''

# Choose the underlying compiler - tensorflow or theano
import json
import os 


# import all the required packages
import numpy as np

import keras
from keras.models import Model
import keras.backend as K
import keras.regularizers as R
import keras.constraints as C
from keras.layers import Activation, AveragePooling2D, BatchNormalization, Convolution2D, Dense, Dropout, Flatten, GlobalAveragePooling2D, GlobalMaxPooling2D, Input, MaxPooling2D
from keras.optimizers import SGD


from os import environ
from keras.callbacks import TensorBoard
from emetrics import EMetrics


defined_metrics = []
defined_loss = []

###############################################################################
# Set up working directories for data, model and logs.
###############################################################################
model_filename = "SignatureCheck.h5"

# writing the train model and getting input data
if environ.get('RESULT_DIR') is not None:
    output_model_folder = os.path.join(os.environ["RESULT_DIR"], "model")
    output_model_path = os.path.join(output_model_folder, model_filename)
else:
    output_model_folder = "model"
    output_model_path = os.path.join("model", model_filename)

os.makedirs(output_model_folder, exist_ok=True)

#writing metrics
if environ.get('JOB_STATE_DIR') is not None:
    tb_directory = os.path.join(os.environ["JOB_STATE_DIR"], "logs", "tb", "test")
else:
    tb_directory = os.path.join("logs", "tb", "test")

os.makedirs(tb_directory, exist_ok=True)
tensorboard = TensorBoard(log_dir=tb_directory)

###############################################################################



###############################################################################
# Set up HPO.
###############################################################################

config_file = "config.json"

if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        json_obj = json.load(f)
    sgd_learning_rate = json_obj["initial_learning_rate"]
    train_batch_size = json_obj["batch_size"]
    num_epochs = json_obj["num_epochs"]
else:
    sgd_learning_rate = 0.001
    train_batch_size = 16
    num_epochs = 5

def getCurrentSubID():
    if "SUBID" in os.environ:
        return os.environ["SUBID"]
    else:
        return None

class HPOMetrics(keras.callbacks.Callback):
    def __init__(self):
        self.emetrics = EMetrics.open(getCurrentSubID())

    def on_epoch_end(self, epoch, logs={}):
        train_results = {}
        test_results = {}

        for key, value in logs.items():
            if 'val_' in key:
                test_results.update({key: value})
            else:
                train_results.update({key: value})

        #print('EPOCH ' + str(epoch))
        self.emetrics.record("train", epoch, train_results)
        self.emetrics.record(EMetrics.TEST_GROUP, epoch, test_results)

    def close(self):
        self.emetrics.close()


###############################################################################
# Load our data, split it, build then model and train
###############################################################################

# Set input shape order
K.set_image_data_format('channels_last')


# Load data from pickle object
import pickle
class_labels_count = 1
with open('training.pickle', 'rb') as f:
    (train_data, train_label) = pickle.load(f)
    if (len(train_data.shape) == 3): 
        if('tensorflow' == 'tensorflow'):
            train_data = train_data.reshape(train_data.shape[0], train_data.shape[1], train_data.shape[2], 1).astype('float32') / 255   
        else:
            train_data = train_data.reshape(train_data.shape[0], 1, train_data.shape[1], train_data.shape[2]).astype('float32') / 255   
    if (len(train_label.shape) == 1) or (len(train_label.shape) == 2 and train_label.shape[1] == 1):
        from keras.utils import np_utils
        class_labels_count = len(set(train_label.flatten()))
        train_label = np_utils.to_categorical(train_label, class_labels_count)
    else:
        class_labels_count = train_label.shape[1]

val_data = []
if(''):
    with open('', 'rb') as f:
        (val_data, val_label) = pickle.load(f)
        if (len(val_data.shape) == 3):
            if('tensorflow' == 'tensorflow'):
                val_data = val_data.reshape(val_data.shape[0], val_data.shape[1], val_data.shape[2], 1).astype('float32') / 255
            else:
                val_data = val_data.reshape(val_data.shape[0], 1, val_data.shape[1], val_data.shape[2]).astype('float32') / 255
        if (len(val_label.shape) == 1) or (len(val_label.shape) == 2 and val_label.shape[1] == 1):
            from keras.utils import np_utils
            val_label = np_utils.to_categorical(val_label, class_labels_count)
else:
    print('Validation set details not provided')
  
test_data = []
if('test.pickle'):
    with open('test.pickle', 'rb') as f:
        (test_data, test_label) = pickle.load(f)
        if (len(test_data.shape) == 3): 
            if('tensorflow' == 'tensorflow'):
                test_data = test_data.reshape(test_data.shape[0], test_data.shape[1], test_data.shape[2], 1).astype('float32') / 255
            else:
                test_data = test_data.reshape(test_data.shape[0], test_data.shape[1], test_data.shape[2]).astype('float32') / 255
        if (len(test_label.shape) == 1) or (len(test_label.shape) == 2 and test_label.shape[1] == 1):
            from keras.utils import np_utils
            test_label = np_utils.to_categorical(test_label, class_labels_count)
else:
    print('Test set details not provided')

#print(train_data.shape)
batch_input_shape_ImageData_a6862f2b = train_data.shape[1:]
#print(batch_input_shape_ImageData_a6862f2b)
#train_batch_size = 16


#Input Layer
ImageData_a6862f2b = Input(shape=batch_input_shape_ImageData_a6862f2b)
#Convolution2D Layer
Convolution2D_1 = Convolution2D(32, (3, 3), kernel_initializer = 'glorot_normal', bias_initializer = 'glorot_normal', padding = 'valid', strides = (1, 1), data_format = 'channels_last', use_bias = False, name = 'Convolution2D_a8ba7708')(ImageData_a6862f2b)
#Batch Normalization Layer
Convolution2D_1 = BatchNormalization(axis=3,name='bn_Convolution2D_a8ba7708')(Convolution2D_1)
#Convolution2D Layer
Convolution2D_2 = Convolution2D(64, (3, 3), kernel_initializer = 'glorot_normal', bias_initializer = 'glorot_normal', padding = 'valid', strides = (1, 1), data_format = 'channels_last', use_bias = False, name = 'Convolution2D_21066527')(Convolution2D_1)
#Batch Normalization Layer
Convolution2D_2 = BatchNormalization(axis=3,name='bn_Convolution2D_21066527')(Convolution2D_2)
#Pooling2D Layer
Pooling2D_3 = MaxPooling2D(pool_size = (2, 2), padding = 'valid', data_format = 'channels_last', strides = (1, 1), name = 'Pooling2D_be9d42f6')(Convolution2D_2)
#Dropout Layer
Dropout_4 = Dropout(0.25, name = 'Dropout_ca207ef5')(Pooling2D_3)
#Flatten Layer
Flatten_5 = Flatten(name = 'Flatten_dce6c7dc')(Dropout_4)
#Dense or Fully Connected (FC) Layer
Dense_6 = Dense(128, kernel_initializer = 'glorot_normal', bias_initializer = 'glorot_normal', use_bias = False, name = 'Dense_6d8b03e2')(Flatten_5)
#Dropout Layer
Dropout_7 = Dropout(0.5, name = 'Dropout_c7de54d6')(Dense_6)
#Dense or Fully Connected (FC) Layer
Dense_8 = Dense(2, kernel_initializer = 'glorot_normal', bias_initializer = 'glorot_normal', use_bias = False, name = 'Dense_e8584fc2')(Dropout_7)
#Softmax Activation Layer
SoftmaxWithLoss_9 = Activation('softmax', name = 'SoftmaxWithLoss_8057e7ef')(Dense_8)
defined_loss = 'categorical_crossentropy'

# Define a keras model
model_inputs = [ImageData_a6862f2b]
model_outputs = [SoftmaxWithLoss_9]
model = Model(inputs=model_inputs, outputs=model_outputs)

# Set the required hyperparameters    
#num_epochs = 100

# Defining the optimizer function
#sgd_learning_rate = 0.001
sgd_momentum = 0.1
sgd_decay = 0.1
sgd_nesterov = False
optimizer_fn = SGD(lr=sgd_learning_rate, momentum=sgd_momentum, decay=sgd_decay, nesterov=sgd_nesterov)

# performing final checks
# if "ImageData" == "TextData" and "" == "Lang_Model":
#     # adding a final Dense layer which has (vocab_length+1) units
#layers = [l for l in model.layers]
#     for i in range(len(layers)):
#         if isinstance(layers[i], keras.layers.core.Dense) and isinstance(layers[i+1], keras.layers.core.Activation):
#             d = Dense(vocab_length+1, name = 'Dense_for_LM_' + str(i+1))(layers[i].output)
#             layers[i+1].inbound_nodes = []              # assumption: there are no merges here
#             d = layers[i+1](d)
#model = Model(inputs=layers[0].input, outputs=layers[len(layers)-1].output)


hpo = HPOMetrics()


# Compile and train the model
model.compile(loss='categorical_crossentropy', optimizer=optimizer_fn, metrics=['accuracy'])
#model.summary()
    
if len(model_outputs) > 1: 
    train_label = [train_label] * len(model_outputs)
    if len(val_data) > 0: val_label = [val_label] * len(model_outputs)
    if len(test_data) > 0: test_label = [test_label] * len(model_outputs)
    
# validate the model
if (len(val_data) > 0):
    history = model.fit(train_data, train_label, batch_size=train_batch_size, epochs=num_epochs, verbose=0, validation_data=(val_data, val_label), shuffle=True, callbacks=[tensorboard, hpo])
else:
    history = model.fit(train_data, train_label, batch_size=train_batch_size, epochs=num_epochs, verbose=0, shuffle=True, callbacks=[tensorboard, hpo])


hpo.close()

# test the model
if (len(test_data) > 0):
    test_scores = model.evaluate(test_data, test_label, verbose=0)
        

print("Training history:" + str(history.history))

print('Test loss:', test_scores[0])
print('Test accuracy:', test_scores[1])

# saving the model
print('Saving the model...')
# save the model
model.save(output_model_path)