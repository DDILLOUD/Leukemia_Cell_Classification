from sklearn.metrics import classification_report

def evaluate_model(model, test_images, test_labels):
    y_pred = model.predict(test_images)
    y_pred_binary = (y_pred > 0.5).astype(int)
    report = classification_report(test_labels, y_pred_binary)
    print(report)
