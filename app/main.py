import os
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="FastAPI-K8s-Mongo-Stateful")

# Credentials from environment variables
DB_USER = os.getenv("MONGO_USER", "admin")
DB_PASS = os.getenv("MONGO_PASS", "password")
DB_HOST = os.getenv("MONGO_HOST", "mongodb-0.mongodb-service")
DB_NAME = "test_db"

# Connection URI
MONGO_URI = f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

class DataEntry(BaseModel):
    title: str
    content: dict

@app.get("/")
async def root():
    return {"status": "connected", "database": DB_NAME}

# --- STORE FUNCTION ---
@app.post("/store")
async def store_data(entry: DataEntry):
    # This actually inserts the data into the 'collection'
    result = await db.collection.insert_one(entry.model_dump())
    return {"message": "Data saved!", "id": str(result.inserted_id)}

# --- ADDED FETCH FUNCTION ---
@app.get("/fetch")
async def fetch_data():
    # This retrieves the data from the 'collection'
    docs = await db.collection.find().to_list(length=100)
    for d in docs: 
        d["_id"] = str(d["_id"])  # Convert ObjectId to string for JSON compatibility
    return docs