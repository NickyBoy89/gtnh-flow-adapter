from enum import Enum
from typing import Any, Iterable, List, Optional, Dict, Self


class Ingredient:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def recycled(self) -> Self:
        return Ingredient(name=f"'[recycle] {self.name}'")


class Product:
    ingredient: Ingredient
    amount: float


def prod(i: Ingredient, amount: float) -> Product:
    p = Product()
    p.ingredient = i
    p.amount = amount
    return p


class Tier(Enum):
    ULV = 0
    LV = 1
    MV = 2
    HV = 3
    EV = 4
    IV = 5
    LUV = 6
    ZPM = 7
    UV = 8
    UHV = 9

    def __str__(self) -> str:
        match self:
            case Tier.ULV:
                return "ULV"
            case Tier.LV:
                return "LV"
            case Tier.MV:
                return "MV"
            case Tier.HV:
                return "HV"
            case Tier.EV:
                return "EV"
            case Tier.IV:
                return "IV"
            case Tier.LUV:
                return "LuV"
            case Tier.ZPM:
                return "ZPM"
            case Tier.UV:
                return "UV"
            case Tier.UHV:
                return "UHV"

        raise Exception(f"Tier {self} does not have a string representation!")


class Recipe:
    machine_name: str
    inputs: List[Product]
    outputs: List[Product]
    tier: Tier
    duration: float
    eut: Optional[int]
    group: Optional[str]

    custom_args: Dict[str, Any]

    # Target numbers
    target_number: Optional[int]
    target_prod: Optional[Product]

    def __init__(
        self,
        machine: str,
        inputs: List[Product],
        outputs: List[Product],
        tier: Tier,
        duration: float,
        eut: Optional[int],
        group=None,
        custom_args={},
    ) -> None:
        self.machine_name = machine
        self.inputs = inputs
        self.outputs = outputs
        self.tier = tier
        self.duration = duration
        self.eut = eut
        self.group = group
        self.custom_args = custom_args

        self.target_number = None
        self.target_prod = None

    def set_target_machine_number(self, n: int) -> None:
        assert self.target_prod == None
        self.target_number = n

    def set_target_production(self, out: Product) -> None:
        assert self.target_number == None
        self.target_prod = out


class Generator:
    recipes: List[Recipe]

    def __init__(self) -> None:
        self.recipes = []

    def add(self, r: Recipe) -> None:
        self.recipes.append(r)

    def add_recipes_from(self, recipes: Iterable[Recipe]) -> None:
        for recipe in recipes:
            self.add(recipe)

    def write_to_file(self, file_name: str) -> None:
        with open(file_name, "w") as outfile:
            for recipe in self.recipes:
                outfile.write(f"- m: {recipe.machine_name}\n")
                outfile.write(f"  tier: {recipe.tier}\n")

                if len(recipe.inputs) == 0:
                    outfile.write("  I: {}\n")
                else:
                    outfile.write(f"  I:\n")
                    for inp in recipe.inputs:
                        outfile.write(f"    {inp.ingredient.name}: {inp.amount}\n")

                if len(recipe.outputs) == 0:
                    outfile.write("  O: {}\n")
                else:
                    outfile.write(f"  O:\n")
                    for out in recipe.outputs:
                        outfile.write(f"    {out.ingredient.name}: {out.amount}\n")

                outfile.write(f"  eut: {recipe.eut}\n")
                outfile.write(f"  dur: {recipe.duration}\n")

                if recipe.group != None:
                    outfile.write(f"  group: {recipe.group}\n")

                for k, v in recipe.custom_args.items():
                    outfile.write(f"  {k}: {v}\n")

                if recipe.target_number != None:
                    outfile.write(f"  number: {recipe.target_number}\n")
                if recipe.target_prod != None:
                    outfile.write(
                        f"  target:\n    {recipe.target_prod.ingredient.name}: {recipe.target_prod.amount}\n"
                    )
                outfile.write("\n\n")
