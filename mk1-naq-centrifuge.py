from gtnh_flow.generate import Generator, prod


from processing_lines.naqfuel_distill import (
    naq_solution_distil_recipe,
    naq_solution_recipe,
    naq_emulsion_recipe,
    acid_naq_emul_recipe,
    naq_light,
    naq_heavy,
)
from processing_lines.fluoroantimonic_acid import fluoroantimonic_acid_processing_line

naq_solution_distil_recipe.set_target_production(prod(naq_light, 30))

g = Generator()

g.add_recipes_from(fluoroantimonic_acid_processing_line)

g.add(naq_solution_distil_recipe)
g.add(naq_solution_recipe)
g.add(naq_emulsion_recipe)
g.add(acid_naq_emul_recipe)

g.write_to_file("mk1-naq-proc.yaml")
