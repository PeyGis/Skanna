from skanna.database.database import database

from skanna.database.database_helper import *

jumia_collection = database.jumia_collection

# Retrieve all products present in the database
async def retrieve_products():
    products = []
    async for student in jumia_collection.find():
        products.append(product_serializer(student))
    return products


# Add a new product into to the database
async def add_jumia_product(product_data: dict) -> dict:
    product = await jumia_collection.insert_one(product_data)
    new_product = await jumia_collection.find_one({"_id": product.inserted_id})
    return product_serializer(new_product)


# # Retrieve a student with a matching ID
# async def retrieve_student(id: str) -> dict:
#     student = await student_collection.find_one({"_id": ObjectId(id)})
#     if student:
#         return student_helper(student)


# # Update a student with a matching ID
# async def update_student(id: str, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     student = await student_collection.find_one({"_id": ObjectId(id)})
#     if student:
#         updated_student = await student_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if updated_student:
#             return True
#         return False


# # Delete a student from the database
# async def delete_student(id: str):
#     student = await student_collection.find_one({"_id": ObjectId(id)})
#     if student:
#         await student_collection.delete_one({"_id": ObjectId(id)})
#         return True