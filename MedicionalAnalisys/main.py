# FastAPI libs
from fastapi import FastAPI, File, UploadFile, status, HTTPException
from fastapi.responses import JSONResponse

# TensorFlow and image processing
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Configuração do projeto
app = FastAPI()

# Variáveis do modelo e tamanho da imagem
MODEL_PATH = "modelo_melanoma.h5"
IMG_HEIGHT = 180
IMG_WIDTH = 180

# Verifica se o diretório uploaded_images existe, caso contrário, cria-o
if not os.path.exists("uploaded_images"):
    os.makedirs("uploaded_images")

# Carregando o modelo treinado
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Modelo carregado com sucesso!")
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Erro ao carregar o modelo: {str(e)}")


@app.post("/upload-image/")
async def process_image(file: UploadFile):
    # Verifica tipo de arquivo
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        return JSONResponse(content={"error": "Tipo de arquivo inválido!"}, status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    # Salva arquivo no servidor temporariamente
    try:
        file_location = f"uploaded_images/{file.filename}"
        with open(file_location, "wb") as image_file:
            content = await file.read()
            image_file.write(content)

        # Faz a classificação da imagem
        result = catalog_image(file_location)
        
        # Retorna o resultado da classificação
        return JSONResponse(content={"message": "OK", "prediction": result}, status_code=status.HTTP_200_OK)

    except Exception as e:
        return JSONResponse(content={"error": f"Erro ao salvar ou processar o arquivo: {str(e)}"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


def catalog_image(file_path):
    try:
        # Carregar e pré-processar a imagem
        img = image.load_img(file_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Expande dimensões para batelada (batch)
        img_array /= 255.0  # Normaliza os valores da imagem

        # Faz a previsão
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])  # Classe com maior probabilidade
        confidence = np.max(predictions[0])  # Maior valor de probabilidade

        return {"class": int(predicted_class), "confidence": float(confidence)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a imagem: {str(e)}")


# Initialize server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
