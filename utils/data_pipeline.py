from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_train_gen(TRAINING_DIR="./frog-v-giraffe/training"):

    train_datagen = ImageDataGenerator(rescale=1./255, 
                                    rotation_range=40,
                                    width_shift_range=0.2,
                                    height_shift_range=0.2,
                                    shear_range=0.2,
                                    zoom_range=0.2,
                                    horizontal_flip=True,
                                    fill_mode='nearest')
    train_generator = train_datagen.flow_from_directory(TRAINING_DIR, batch_size=20,
                                                        class_mode='binary', target_size=(150, 150))

    return train_generator

def get_valid_gen(VALIDATION_DIR="./frog-v-giraffe/testing"):
    valid_datagen = ImageDataGenerator(rescale=1./255)
    valid_generator = valid_datagen.flow_from_directory(VALIDATION_DIR, 
                                                        class_mode='binary', 
                                                        target_size=(150, 150))
    
    return valid_generator