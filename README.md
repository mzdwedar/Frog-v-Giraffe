# Frog-v-Giraffe

Used transfer learning with InceptionV3 model.
I've frozen the weights of the lower layers of InceptionV3 model, concatenated them with two dense layers.
Then I've trained the dense layers only.

## run the follow

```
! pip install -q kaggle
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json
! kaggle datasets download jessicali9530/caltech256
```

# Dataset

I've used two categories (that are frog and Giraffe) from the following dataset:
<https://www.kaggle.com/jessicali9530/caltech256>

# Paper

The architecture of the neural network can be found here:
<https://arxiv.org/abs/1512.00567v3>
