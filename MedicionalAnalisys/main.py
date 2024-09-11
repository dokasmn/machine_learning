# fastapi libs

from fastapi import FastAPI, HTTPException
from typing import List, Optional
from sqlalchemy.exc import IntegrityError
import sqlite3
from typing import Any, Dict

# myapp

app = FastAPI()

# endpoints

@app.post("/use_model/")
async def root():
    query = clubs.select()
    return await database.fetch_all(query)

