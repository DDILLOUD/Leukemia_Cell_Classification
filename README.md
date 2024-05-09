# Blood Cancer Classification

This project aims to classify leukemia cells using Convolutional Neural Networks (CNNs). It utilizes a dataset containing single-cell images taken from peripheral blood smears of patients diagnosed with Acute Myeloid Leukemia.

## Dataset

The dataset contains 10,000 single-cell images (64x64 pixels) split into training, testing, and validation sets.
The dataset used in this project contains single-cell images taken from peripheral blood smears of patients diagnosed with Acute Myeloid Leukemia (AML), a type of blood cancer. You can find the dataset on [Kaggle](https://www.kaggle.com/datasets/akhiljethwa/blood-cancer-image-dataset).

### Citations

- Matek, C., Schwarz, S., Marr, C., & Spiekermann, K. (2019). A Single-cell Morphological Dataset of Leukocytes from AML Patients and Non-malignant Controls [Data set]. The Cancer Imaging Archive. [DOI](https://doi.org/10.7937/tcia.2019.36f5o9ld)
- Matek, C., Schwarz, S., Spiekermann, K. et al. Human-level recognition of blast cells in acute myeloid leukaemia with convolutional neural networks. Nat Mach Intell 1, 538–544 (2019). [DOI](https://doi.org/10.1038/s42256-019-0101-9)

## What Does This Model Do?

This model is designed to classify leukemia cells in blood smear images. Given an input image, the model predicts whether the cells present in the image are indicative of Acute Myeloid Leukemia (AML) or non-malignant cells. This classification is crucial for diagnosing and monitoring leukemia, aiding healthcare professionals in making timely and accurate decisions.

## Model Architecture

We employed a **CNN architecture**  named LeukoNet for the classification task. LeukoNet consists of three convolutional layers followed by max-pooling layers, a flatten layer, and two fully connected layers.

## Training

The model was trained on the training set using the Adam optimizer and binary cross-entropy loss. We trained the model for 10 epochs, achieving perfect accuracy on the test set.

## Evaluation

We evaluated the model's performance using precision, recall, and F1-score metrics, achieving perfect scores for the absence of leukemia cells.

## Next Steps

- Further evaluation on unseen data.
- Apply regularization techniques to prevent overfitting.
- Explore model interpretability techniques.
- Optimize hyperparameters for better performance.



