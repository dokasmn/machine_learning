# FastAPI libs
from fastapi import FastAPI, File, UploadFile, status, HTTPException
from fastapi.responses import JSONResponse


# Project libs



# Config project
app = FastAPI(debug=True)


@app.post("/upload-image/")
async def process_image(file: UploadFile):
    
    # Verifica tipo de arquivo
    if file.content_type not in ["image/jpeg", "image/png"]:
        return JSONResponse(content={"error" : "Invalid file type!"}, status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    # Salva arquivo no servidor
    with open(f"uploaded_images/{file.filename}", "wb") as image:
        content = await file.read()
        image.write(content)
    
    return JSONResponse(content={"message" : "OK"}, status_code=status.HTTP_200_OK)


# Inicializar servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)