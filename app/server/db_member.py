from bson.objectid import ObjectId
import motor.motor_asyncio
import os

MONGO_DB_URL = os.environ.get('MONGO_DB_URL')

print("MONGO_DB_URL = ",MONGO_DB_URL)
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URL)

database = client.memberdb

collection = database.get_collection("members_collection")


# helpers

def member_helper(data) -> dict:
    return {
        "id": str(data["_id"]),
        "fullname": data["fullname"],
        "email": data["email"],
        "mobile": data["mobile"],
        "address": data["address"],

    }

# Retrieve all member present in the database
async def db_get_all():
    members = []
    async for member in collection.find():
        members.append(member_helper(member))
    return members


# Add a new member into to the database
async def db_add_member(data: dict) -> dict:
    member = await collection.insert_one(data)
    new_member = await collection.find_one({"_id": member.inserted_id})
    return member_helper(new_member)

 
# Retrieve a member with a matching ID
async def db_get_member(id: str) -> dict:
    member = await collection.find_one({"_id": ObjectId(id)})
    if member:
        return  member_helper(member)


# Update a member with a matching ID
async def db_update_member(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    member = await collection.find_one({"_id": ObjectId(id)})
    if member:
        updated_member = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_member:
            return True
        return False


# Delete a member from the database
async def db_delete_member(id: str):
    member = await collection.find_one({"_id": ObjectId(id)})
    if member:
        await collection.delete_one({"_id": ObjectId(id)})
        return True