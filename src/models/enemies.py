from pydantic import BaseModel, Field
from typing import Optional, Literal

# todo: add more species and weapons
class EnemyModel(BaseModel):
    enemy_name : str = Field(description="Enemy's name")
    enemy_species : Literal["Orc"] = Field(default="Orc", description="Enemy's specie. Only orcs are supported.")
    enemy_hp : int = Field(default=25, gt=0, description="Enemy's health. When 0 enemy dies.")
    enemy_weapon : Literal["Sword"] = Field(default="Sword", description="Enemy's weapon. Only sword is supported.")