# Finetune ResNet50 model on Cats and Dogs Dataset:

1. Dataset for Cats and Dogs can be found on kaggle. With kaggle api, download the dataset using the api command.
2. Using tensorflow, we can create a dataloader for training and testing data and we can pass the images to the model in batches directly without loading all the images.
3. Since ResNet50 model returns feature blocks of size 7x7x2048, we will add additional layers onto it to train the classification.
4. We add a GlobalAveragePooling2D() to convert it features into a single 2048 element vector.
5. After this, we'll add a dense layer on top of this to get a single prediction per image based on the output from the previous layer.
6. After training this model, we get training accuracy of 99.1% and validation accuracy of 97.9%.
7. Upon testing the model on the test dataset, the testing accuracy comes out to be 97.5%.
