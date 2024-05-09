# Blood Cancer Classification

This project aims to classify leukemia cells using Convolutional Neural Networks (CNNs). It utilizes a dataset containing single-cell images taken from peripheral blood smears of patients diagnosed with Acute Myeloid Leukemia.

## Dataset

The dataset contains 10,000 single-cell images (64x64 pixels) split into training, testing, and validation sets.

## Model Architecture

We employed a CNN architecture named LeukoNet for the classification task. LeukoNet consists of three convolutional layers followed by max-pooling layers, a flatten layer, and two fully connected layers.

## Training

The model was trained on the training set using the Adam optimizer and binary cross-entropy loss. We trained the model for 10 epochs, achieving perfect accuracy on the test set.

## Evaluation

We evaluated the model's performance using precision, recall, and F1-score metrics, achieving perfect scores for the absence of leukemia cells.

## Next Steps

- Further evaluation on unseen data.
- Apply regularization techniques to prevent overfitting.
- Explore model interpretability techniques.
- Optimize hyperparameters for better performance.

For detailed implementation, refer to the notebook [here](notebooks/Leukemia_Cell_Classification.ipynb).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
