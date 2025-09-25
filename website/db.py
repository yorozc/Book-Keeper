from pymongo import MongoClient

# Sets up MongoDB
uri = "mongodb+srv://yorozcolop49_db_user:3ca3CEtTDJV6HRk1@libraryuser.9t1ek5b.mongodb.net/?retryWrites=true&w=majority&appName=libraryUser"

client = MongoClient(uri)

db = client["libraryUser"]
users = db["users"] # creates collection if doesn't exist
booklist = db["booklist"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)