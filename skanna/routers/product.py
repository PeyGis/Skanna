from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from skanna.database.jumia_schema import (retrieve_products, add_jumia_product)
from skanna.models.jumia_model import JumiaSchema
from skanna.models.helper import (ResponseModel, ErrorResponseModel)

router = APIRouter()

@router.post("/", response_description="Jumia Product data added into the database")
async def post_jumia_product(product: JumiaSchema = Body(...)):
    product = jsonable_encoder(product)
    new_product = await add_jumia_product(product)
    return ResponseModel(new_product, "Product added successfully.")

@router.get("/", response_description="Jumia Product data retrieved from the database")
async def get_jumia_product():
    products = await retrieve_products()
    if products:
        return ResponseModel(products, "Product fetched successfully.")
    else:
        return ResponseModel(products, "Empty list returned")