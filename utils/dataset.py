from zipfile import ZipFile
import os

import random
from shutil import copyfile

def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
  """
  copy the instances of a particular class and split them into training and testing
  SOURCE: directory of all instances
  TRAINING/TESTING: directories of train/test
  SPLIT_SIZE: the proportion of the train set
  """
  
  files = []
  for filename in os.listdir(SOURCE):
    file = SOURCE + filename
    if (os.path.getsize(file) > 0):
      files.append(filename)
    else:
      print(f'{filename} is empty')


  train_length = int(len(files) * SPLIT_SIZE)
  test_length = int(len(files) - train_length)
  shuffled_set = random.sample(files, len(files))
  train_set = shuffled_set[0:train_length]
  test_set = shuffled_set[train_length:]

  for filename in train_set:
    this_file = SOURCE + filename
    destination = TRAINING + filename
    copyfile(this_file, destination)

  for filename in test_set:
    this_file = SOURCE + filename
    destination = TESTING + filename
    copyfile(this_file, destination)

def extract_dataset():
    """
    extract the files that belong to either fron or giraffe.
    """
    with ZipFile('caltech256.zip', 'r') as zipObj:
    # Extract all the contents of zip file in current directory
        listOfFileNames = zipObj.namelist()
        for file in listOfFileNames:
            if (file.startswith('256_ObjectCategories/080.frog') or file.startswith('256_ObjectCategories/084.giraffe')):
                zipObj.extract(file)

    print("the number of frog instances: {}".format( len(os.listdir('./256_ObjectCategories/080.frog'))))
    print("The numebr of giraffe instances: {}".format(len(os.listdir('./256_ObjectCategories/084.giraffe'))))


def build_dataset():
    extract_dataset()
    
    os.makedirs('./frog-v-giraffe/training/frog')
    os.makedirs('./frog-v-giraffe/training/giraffe')
    os.makedirs('./frog-v-giraffe/testing/frog')
    os.makedirs('./frog-v-giraffe/testing/giraffe')

    FROG_SOURCE_DIR = "./256_ObjectCategories/080.frog/"
    TRAINING_FROG_DIR = "./frog-v-giraffe/training/frog/"
    TESTING_FROG_DIR = "./frog-v-giraffe/testing/frog/"

    GIRAFFE_SOURCE_DIR = "./256_ObjectCategories/084.giraffe/"
    TRAINING_GIRAFFE_DIR = "./frog-v-giraffe/training/giraffe/"
    TESTING_GIRAFFE_DIR = "./frog-v-giraffe/testing/giraffe/"

    split_size = .80
    split_data(FROG_SOURCE_DIR, TRAINING_FROG_DIR, TESTING_FROG_DIR, split_size)
    split_data(GIRAFFE_SOURCE_DIR, TRAINING_GIRAFFE_DIR, TESTING_GIRAFFE_DIR, split_size)

    print(f'frog training number: { len(os.listdir("./frog-v-giraffe/training/frog")) }')
    print(f'frog testing numebr: { len(os.listdir("./frog-v-giraffe/testing/frog")) }')
    print(f'giraffe training number: { len(os.listdir("./frog-v-giraffe/training/giraffe")) }')
    print(f'giraffe testing number: { len(os.listdir("./frog-v-giraffe/testing/giraffe")) }')