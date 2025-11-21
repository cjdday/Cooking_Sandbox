"""Data models for recipes and ingredients using Pydantic."""

from datetime import UTC, datetime, timedelta

from pydantic import BaseModel, Field, HttpUrl, field_validator

from constants.recipie_tags import VALID_TAGS


class Ingredient(BaseModel):
    name: str
    quantity: str
    notes: str | None = None


class Recipe(BaseModel):
    id: str
    name: str
    average_cost_per_serving: float | None = None
    estimated_calories_per_serving: int | None = None
    ingredients: list[Ingredient]
    instructions: list[str]
    cooking_time: timedelta  # actual duration in seconds, not text
    tags: list[str]  # validated against VALID_TAGS
    image_url: HttpUrl | None = None  # blob storage link
    embedding_vector: list[float] | None = None  # for LLM semantic search
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @field_validator("tags", pre=True)
    def validate_tags(cls, tags: list[str]):
        clean = [t.lower().strip() for t in tags]
        for t in clean:
            if t not in VALID_TAGS:
                raise ValueError(f"Invalid tag: {t}")
        return clean
