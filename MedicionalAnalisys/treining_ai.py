import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
import pathlib

# Definindo o caminho para os dados
data_dir_train = pathlib.Path("./Train/")
data_dir_test = pathlib.Path("./Test/")

# Carregando os dados de treinamento e validação
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir_train,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(180, 180),
    batch_size=32)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir_train,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(180, 180),
    batch_size=32)

# Criando o modelo CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(180, 180, 3)),
    MaxPool2D(),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPool2D(),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPool2D(),
    Dropout(0.2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(9, activation='softmax')  # Supondo que você tenha 9 classes
])

# Compilando o modelo
model.compile(optimizer=Adam(learning_rate=0.001),
            loss=SparseCategoricalCrossentropy(),
            metrics=['accuracy'])

# Treinando o modelo
model.fit(train_ds, validation_data=val_ds, epochs=25)

# Salvando o modelo
model.save("modelo_melanoma.h5")
