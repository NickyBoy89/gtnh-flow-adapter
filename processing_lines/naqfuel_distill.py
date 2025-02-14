import sys

sys.path.append("..")  # Adds higher directory to python modules path.


from gtnh_flow.generate import Ingredient, Recipe, Tier, prod
from processing_lines.fluoroantimonic_acid import fluoroantimonic_acid

naq_heavy = Ingredient("heavy naquadah fuel")
naq_light = Ingredient("light naquadah fuel")
naq_solution = Ingredient("naquadah solution")
naq_asphalt = Ingredient("naquadah asphalt")
naq_gas = Ingredient("naquadah gas")

naq_solution_distil_recipe = Recipe(
    machine="distillation tower",
    tier=Tier.EV,
    inputs=[prod(naq_solution, 20)],
    outputs=[
        prod(naq_asphalt, 2),
        prod(naq_heavy, 5),
        prod(naq_light, 10),
        prod(naq_gas, 60),
    ],
    eut=1920,
    duration=1,
    group="naqfuel fractions",
)

naq_emulsion = Ingredient("naquadah emulsion")
rad_sludge_dust = Ingredient("radioactive sludge dust")

naq_solution_recipe = Recipe(
    machine="centrifuge",
    tier=Tier.MV,
    inputs=[prod(naq_emulsion, 1000)],
    outputs=[prod(rad_sludge_dust, 5.46), prod(naq_solution, 500)],
    eut=120,
    duration=40,
    group="naqfuel fractions",
)

acid_naq_emul = Ingredient("acid naquadah emulsion")
quicklime = Ingredient("quicklime")
fluorspar = Ingredient("fluorospar")
antimony_triox = Ingredient("antimony trioxide")

naq_emulsion_recipe = Recipe(
    machine="LCR",
    tier=Tier.LV,
    inputs=[prod(acid_naq_emul, 1000), prod(quicklime, 8)],
    outputs=[
        prod(fluorspar, 4),
        prod(antimony_triox, 0.25),
        prod(naq_emulsion, 1000),
    ],
    eut=20,
    duration=12,
    group="naqfuel fractions",
)

naquadria_dust = Ingredient("naquadriah dust")
extreme_unstable = Ingredient("extremely unstable naquadah dust")

acid_naq_emul_recipe = Recipe(
    machine="LCR",
    tier=Tier.IV,
    inputs=[prod(fluoroantimonic_acid, 4000), prod(naquadria_dust, 32)],
    outputs=[prod(acid_naq_emul, 8000), prod(extreme_unstable, 17)],
    eut=3840,
    duration=180,
    custom_args={
        "coils": "naquadah",
        "heat": 3400,
    },
    group="naqfuel fractions",
)


naq_distill_processing_line = [
    naq_solution_distil_recipe,
    naq_solution_recipe,
    naq_emulsion_recipe,
    acid_naq_emul_recipe,
]
