# FastAPI libs
from fastapi import FastAPI, File, UploadFile, status, HTTPException
from fastapi.responses import JSONResponse


# Project libs
import tensorflow as tf


# Config project
app = FastAPI(debug=True)


# Variables
IMG_HEIGHT = 180
IMG_WIDTH = 180
BACTH_SIZE = 32


@app.post("/upload-image/")
async def process_image(file: UploadFile):
    
    # Verifica tipo de arquivo
    if file.content_type not in ["image/jpeg", "image/png"]:
        return JSONResponse(content={"error" : "Invalid file type!"}, status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    # Salva arquivo no servidor
    with open(f"uploaded_images/{file.filename}", "wb") as image:
        content = await file.read()
        image.write(content)

    catalog_image(file.filename)
    
    return JSONResponse(content={"message" : "OK"}, status_code=status.HTTP_200_OK)


def catalog_image(file_name):
    validate_skin_cancer_type = tf.keras.preprocessing.image_dataset_from_directory(
        f"uploaded_images/{file_name}"
    )


# Initialize server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)