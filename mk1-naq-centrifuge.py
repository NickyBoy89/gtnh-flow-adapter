from gtnh_flow.generate import Generator, Recipe, Tier, prod


from processing_lines.naqfuel_distill import (
    naq_solution_distil_recipe,
    naq_solution_recipe,
    naq_emulsion_recipe,
    acid_naq_emul_recipe,
    naq_light,
    naq_heavy,
    antimony_triox,
)
from processing_lines.fluoroantimonic_acid import (
    fluoroantimonic_acid_processing_line,
    antimony,
)

naq_solution_distil_recipe.set_target_production(prod(naq_light, 30))

g = Generator()

g.add_recipes_from(fluoroantimonic_acid_processing_line)

g.add(
    Recipe(
        machine="electrolyzer",
        tier=Tier.LV,
        inputs=[prod(antimony_triox, 5)],
        outputs=[prod(antimony.recycled(), 2)],
        eut=30,
        duration=12.5,
    )
)

g.add(naq_solution_distil_recipe)
g.add(naq_solution_recipe)
g.add(naq_emulsion_recipe)
g.add(acid_naq_emul_recipe)

g.write_to_file("mk1-naq-proc.yaml")
