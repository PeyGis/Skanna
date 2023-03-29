from typing import Optional

from pydantic import BaseModel, Field

class JumiaSchema(BaseModel):
    """A Pyndantic schema to validate Jumia"""
    title: str = Field(...)
    price: int = Field(...)
    url: str = Field(...)
    image_url: str = Field(...)
    stock_quantity: int = Field(...)
    description: str = Field(...)
    rating: float = Field(..., le=5, ge=0)
    num_verified_rating: int = Field(...)
    brand: str = Field(...)
    category: str = Field(...)
    sub_category: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Google Pixel 7 Pro - Black",
                "price": 6000,
                "url": "https://jumia.com/assets/google-pixel-7.png",
                "image_url": "https://jumia.com/assets/google-pixel-7.png",
                "stock_quantity": 2,
                "description": "Designed to capture stunning videos and images",
                "rating": 4.5,
                "num_verified_rating": 25,
                "brand": "Google",
                "category": "Mobile Phones",
                "sub_category": "Smart phones"

            }
        }