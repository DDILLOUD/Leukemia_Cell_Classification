def train_model(model, train_images, train_labels, val_images, val_labels, epochs):
    history = model.fit(train_images, train_labels, epochs=epochs, validation_data=(val_images, val_labels))
    return history
