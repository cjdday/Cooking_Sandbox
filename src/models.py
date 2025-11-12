from pydantic import BaseModel, Field, field_validator, HttpUrl
from typing import List, Optional
from datetime import datetime, timedelta, timezone

from constants.recipie_tags import VALID_TAGS


class Ingredient(BaseModel):
    name: str
    quantity: Optional[str] = None
    notes: Optional[str] = None


class Recipe(BaseModel):
    id: str
    name: str
    cuisine_types: List[str] = Field(default_factory=list)
    average_cost_per_serving: Optional[float] = None
    estimated_calories_per_serving: Optional[int] = None
    ingredients: List[Ingredient]
    instructions: List[str]
    cooking_time: timedelta  # actual duration in seconds, not text
    tags: List[str]  # validated against VALID_TAGS
    image_url: Optional[HttpUrl] = None  # blob storage link
    embedding_vector: Optional[List[float]] = None  # for LLM semantic search
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("tags", pre=True)
    def validate_tags(cls, tags: List[str]):
        clean = [t.lower().strip() for t in tags]
        for t in clean:
            if t not in VALID_TAGS:
                raise ValueError(f"Invalid tag: {t}")
        return clean
