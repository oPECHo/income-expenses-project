import motor.motor_asyncio

MONGODB_URL = "mongodb+srv://nattanon:6510110140@localhost.wrdbqvn.mongodb.net/test?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client['Income-Expense']
