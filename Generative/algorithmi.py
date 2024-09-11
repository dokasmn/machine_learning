import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Reshape, Flatten, LeakyReLU
from tensorflow.keras.models import Sequential
from tensorflow.keras.datasets import mnist

# 1. Carregando e preparando o conjunto de dados MNIST
(X_train, _), (_, _) = mnist.load_data()

# 2. Normalizando os dados para a escala [0, 1]
X_train = X_train / 255.0

# 3. Aplanando (flatten) as imagens de 28x28 pixels em vetores de 784 pixels
X_train = X_train.reshape(-1, 784)

# 4. Definindo o gerador
def build_generator():
    model = Sequential()
    # Entrada: vetor de ruído de 100 dimensões
    model.add(Dense(128, input_dim=100))
    model.add(LeakyReLU(alpha=0.01))
    # Camada oculta densa com 784 saídas (28x28 pixels)
    model.add(Dense(784, activation='sigmoid'))
    model.add(Reshape((28, 28)))
    return model

# 5. Definindo o discriminador
def build_discriminator():
    model = Sequential()
    # Entrada: imagem de 28x28 pixels aplanada em um vetor de 784
    model.add(Flatten(input_shape=(28, 28)))
    model.add(Dense(128))
    model.add(LeakyReLU(alpha=0.01))
    # Saída: decisão binária (real ou gerada)
    model.add(Dense(1, activation='sigmoid'))
    return model

# 6. Compilando o discriminador
discriminator = build_discriminator()
discriminator.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 7. Compilando o gerador
generator = build_generator()

# 8. Ligando o discriminador e o gerador para formar a GAN
discriminator.trainable = False
gan = Sequential([generator, discriminator])
gan.compile(loss='binary_crossentropy', optimizer='adam')

# 9. Função para treinar a GAN
def train_gan(gan, generator, discriminator, X_train, epochs=10000, batch_size=128):
    half_batch = batch_size // 2
    
    for epoch in range(epochs):
        # Treinando o discriminador com dados reais
        idx = np.random.randint(0, X_train.shape[0], half_batch)
        real_images = X_train[idx]
        real_labels = np.ones((half_batch, 1))  # Rótulos reais = 1
        
        # Treinando o discriminador com dados gerados
        noise = np.random.normal(0, 1, (half_batch, 100))
        fake_images = generator.predict(noise)
        fake_labels = np.zeros((half_batch, 1))  # Rótulos falsos = 0
        
        # Treinando o discriminador
        d_loss_real = discriminator.train_on_batch(real_images, real_labels)
        d_loss_fake = discriminator.train_on_batch(fake_images, fake_labels)
        
        # Treinando o gerador via GAN (o discriminador está congelado)
        noise = np.random.normal(0, 1, (batch_size, 100))
        valid_labels = np.ones((batch_size, 1))  # Queremos que o gerador faça imagens "válidas"
        g_loss = gan.train_on_batch(noise, valid_labels)
        
        if epoch % 1000 == 0:
            print(f"{epoch} [D loss: {0.5 * np.add(d_loss_real, d_loss_fake)}] [G loss: {g_loss}]")

# 10. Treinando a GAN
train_gan(gan, generator, discriminator, X_train)
