from pydantic import BaseModel, Field
from typing import Optional, Literal

# todo: add more classes and weapons, inventory
class CharacterModel(BaseModel):
    char_name : str = Field(description="Character's name")
    char_class : Literal["Warrior"] = Field(default="Warrior", description="Character's class. Only warrior characters are supported.")
    char_hp : int = Field(default=25, gt=0, description="Character's health. When 0 character dies.")
    char_weapon : Literal["Sword"] = Field(default="Sword", description="Character's weapon. Only sword is supported.")