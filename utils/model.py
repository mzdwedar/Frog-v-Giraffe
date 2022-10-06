from tf.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.optimizers import RMSprop

import os
import pandas as pd


def model_builder():
    pre_trained_model = InceptionV3(input_shape=(150,150,3), 
                                include_top=False,
                                weights='imagenet')

    for layer in pre_trained_model.layers:
        layer.trainable = False
    
    last_layer = pre_trained_model.get_layer('mixed4')
    print("last layer shape: ", last_layer.output_shape)
    last_output = last_layer.output

    x = layers.Flatten()(last_output)
    x = layers.Dense(1080, activation='relu')(x)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.Dense(1, activation='sigmoid')(x)

    model = Model(pre_trained_model.input, x)

    model.compile(optimizer=RMSprop(learning_rate=0.0001),
              loss='binary_crossentropy',
              metrics=['acc'])
    
    return model

def save_model(model, model_name, history):
    ''' save the model and the metrics'''
    os.makedirs('saved_models', exist_ok=True)

    model_saved_name = model_name + ".h5"
    
    model.save("saved_model/" + model_saved_name)

    hist_df = pd.DataFrame(history.history) 
    hist_csv_file =  "history_" + model_name + ".csv"
    filepath = "saved_models/" + hist_csv_file 
    with open(filepath, mode='w') as f:
        hist_df.to_csv(f)

    print(f'{model_saved_name} saved')
    print(f'{hist_csv_file} saved')