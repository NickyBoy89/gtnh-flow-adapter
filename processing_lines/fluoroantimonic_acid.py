import sys

sys.path.append("..")  # Adds higher directory to python modules path.


from gtnh_flow.generate import Recipe, Ingredient, Tier, prod


group_fluoroantimonic = "fluoroantimonic acid processing"


fluoroantimonic_acid = Ingredient("fluoroantimonic acid")
antimony_pentafluoride = Ingredient("antimony pentafluoride")
hydrofluoric = Ingredient("hydrofluoric acid")

fluoroantimonic_acid_recipe = Recipe(
    machine="LCR",
    tier=Tier.EV,
    inputs=[prod(antimony_pentafluoride, 1000), prod(hydrofluoric, 1000)],
    outputs=[prod(fluoroantimonic_acid, 1000)],
    eut=1920,
    duration=42,
    group=group_fluoroantimonic,
)

ether = Ingredient("ether")
ether_recycle = Ingredient("'[recycle] ether'")
pentafluoride_solution = Ingredient("antimony pentafluoride solution")

pentafluoride_recipe = Recipe(
    machine="distillation tower",
    tier=Tier.MV,
    inputs=[prod(pentafluoride_solution, 4000)],
    outputs=[prod(antimony_pentafluoride, 4000), prod(ether_recycle, 500)],
    eut=120,
    duration=5,
    group=group_fluoroantimonic,
)

fluorine = Ingredient("fluorine")
crushed_ice = Ingredient("crushed_ice")

pentafluoride_solution_recipe = Recipe(
    machine="LCR",
    tier=Tier.IV,
    inputs=[prod(ether, 1000), prod(fluorine, 40_000), prod(crushed_ice, 8000)],
    outputs=[prod(pentafluoride_solution, 8000)],
    eut=7680,
    duration=40,
    group=group_fluoroantimonic,
)

fluoroantimonic_acid_processing_line = [
    fluoroantimonic_acid_recipe,
    pentafluoride_recipe,
    pentafluoride_solution_recipe,
]
