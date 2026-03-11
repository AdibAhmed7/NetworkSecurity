from pymongo.mongo_client import MongoClient
import certifi

# MongoDB connection string
uri = "mongodb+srv://AdibAhmed0425:x8xI5yDlqFEkBZ3v@cluster0.dcbhkm4.mongodb.net/?retryWrites=true&w=majority"

# Get certificate file for TLS connection
ca = certifi.where()

# Create MongoDB client
client = MongoClient(uri, tlsCAFile=ca)

# Test connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)

    