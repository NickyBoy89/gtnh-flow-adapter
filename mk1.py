from gtnh_flow.generate import Recipe, Ingredient, Tier, Generator, prod
from processing_lines.naqfuel_distill import (
    naq_distill_processing_line,
    naq_light,
    naq_heavy,
)
from processing_lines.fluoroantimonic_acid import fluoroantimonic_acid_processing_line


g = Generator()

naqMk1 = Ingredient("naquadah fuel mk1")

# Fuel production
fuelProd = Recipe(
    machine="fusion reactor",
    tier=Tier.LUV,
    inputs=[prod(naq_heavy, 30), prod(naq_light, 65)],
    outputs=[prod(naqMk1, 100)],
    duration=0.25,
    eut=26000,
    custom_args={
        "start": 1,
        "mk": 1,
    },
)

# Naq Distillation

# g.add_recipes_from(fluoroantimonic_acid_processing_line)
# g.add_recipes_from(naq_distill_processing_line)

# Liquid Air

liqAir = Ingredient("liquid air")
air = Ingredient("air")

g.add(
    Recipe(
        machine="air intake hatch",
        tier=Tier.LV,
        inputs=[],
        outputs=[prod(air, 1000)],
        eut=0,
        duration=0.2,
        group="air",
    )
)


g.add(
    Recipe(
        machine="vacuum freezer",
        tier=Tier.LUV,
        inputs=[prod(air, 2000)],
        outputs=[prod(liqAir, 1000)],
        eut=480,
        duration=1.4,
        group="air",
    )
)

# Cryotheum

gelidCryo = Ingredient("gelid cryotheum")
cryoDust = Ingredient("cryotheum dust")
cryoComb = Ingredient("cryotheum comb")
refractWax = Ingredient("refractory wax")

g.add(
    Recipe(
        machine="fluid extractor",
        tier=Tier.IV,
        inputs=[prod(cryoDust, 1)],
        outputs=[prod(gelidCryo, 250)],
        eut=240,
        duration=10,
        group="bee gelid cryotheum",
    )
)

g.add(
    Recipe(
        machine="industrial centrifuge",
        tier=Tier.LUV,
        inputs=[prod(cryoComb, 1)],
        outputs=[prod(cryoDust, 1), prod(refractWax, 0.5)],
        eut=240,
        duration=12.8,
        group="bee gelid cryotheum",
    )
)

# Atomic separation

atomicSep = Ingredient("atomic separation catalyst")
atomicSepIngot = Ingredient("atomic separation catalyst ingot")
atomicSepIngotHot = Ingredient("hot atomic separation catalyst ingot")

g.add(
    Recipe(
        machine="fluid extractor",
        tier=Tier.EV,
        inputs=[prod(atomicSepIngot, 1)],
        outputs=[prod(atomicSep, 144)],
        eut=2,
        duration=15,
        group="atomic separation catalyst",
    )
)

g.add(
    Recipe(
        machine="vacuum freezer",
        tier=Tier.UV,
        inputs=[prod(atomicSepIngotHot, 1)],
        outputs=[prod(atomicSepIngot, 1)],
        eut=30720,
        duration=10,
        group="atomic separation catalyst",
    )
)

orundPlate = Ingredient("orundum plate")
rawAtomicCata = Ingredient("raw atomic separation catalyst")
moltenPluton239 = Ingredient("molten plutonium 239")

g.add(
    Recipe(
        machine="EBF",
        tier=Tier.ZPM,
        inputs=[
            prod(orundPlate, 2),
            prod(rawAtomicCata, 4),
            prod(moltenPluton239, 144),
        ],
        outputs=[prod(atomicSepIngotHot, 1)],
        eut=480,
        duration=180,
        custom_args={"heat": 5000, "coils": "naquadah"},
        group="atomic separation catalyst",
    )
)

pluton239Dust = Ingredient("plutonium 239 dust")

g.add(
    Recipe(
        machine="fluid extractor",
        tier=Tier.EV,
        inputs=[prod(pluton239Dust, 1)],
        outputs=[prod(moltenPluton239, 144)],
        eut=42,
        duration=1.2,
        group="atomic separation catalyst",
    )
)

blazePow = Ingredient("blaze powder")
draconDust = Ingredient("draconium dust")
arditeDust = Ingredient("ardite dust")
moltenNaq = Ingredient("molten naquadah")

g.add(
    Recipe(
        machine="mixer",
        tier=Tier.EV,
        inputs=[
            prod(blazePow, 32),
            prod(draconDust, 4),
            prod(arditeDust, 4),
            prod(moltenNaq, 144),
        ],
        outputs=[prod(rawAtomicCata, 64)],
        eut=480,
        duration=15,
        group="atomic separation catalyst",
    )
)

tiberPlate = Ingredient("tiberium plate")
rawSiliconPlate = Ingredient("raw silicon plate")

g.add(
    Recipe(
        machine="forming press",
        tier=Tier.ZPM,
        inputs=[prod(tiberPlate, 1), prod(rawSiliconPlate, 8)],
        outputs=[prod(orundPlate, 1)],
        eut=3820,
        duration=20,
        group="atomic separation catalyst",
    )
)

tiberBlock = Ingredient("tiberium block")

g.add(
    Recipe(
        machine="cutting machine",
        tier=Tier.IV,
        inputs=[prod(tiberBlock, 1)],
        outputs=[prod(tiberPlate, 9)],
        eut=30,
        duration=163,
        group="atomic separation catalyst",
    )
)

tiberGem = Ingredient("tiberium gem")

g.add(
    Recipe(
        machine="compressor",
        tier=Tier.IV,
        inputs=[prod(tiberGem, 9)],
        outputs=[prod(tiberBlock, 1)],
        eut=2,
        duration=15,
        group="atomic separation catalyst",
    )
)

rawSiliconIngot = Ingredient("raw silicon ingot")

g.add(
    Recipe(
        machine="bending machine",
        tier=Tier.IV,
        inputs=[prod(rawSiliconIngot, 1)],
        outputs=[prod(rawSiliconPlate, 1)],
        eut=24,
        duration=1.4,
        group="atomic separation catalyst",
    )
)


# Reactor inputs

eu = Ingredient("eu")
mk1Dep = Ingredient("naqfuel mk1 (depleted)")

# Reactor

MK1_EUT = 975_000
CRYO_BOOST = 2.75
ATOMICSEP_PARALLEL = 16
BURN_TIME = 3

reactor = Recipe(
    machine="large naquadah reactor",
    tier=Tier.LV,
    inputs=[
        prod(liqAir, 2400 * BURN_TIME),
        prod(gelidCryo, 1000 * BURN_TIME),
        prod(naqMk1, 1 * ATOMICSEP_PARALLEL),
        prod(atomicSep, 20 * BURN_TIME),
    ],
    outputs=[
        prod(eu, MK1_EUT * CRYO_BOOST * ATOMICSEP_PARALLEL * 20 * BURN_TIME),
        prod(mk1Dep, 1 * ATOMICSEP_PARALLEL),
    ],
    duration=3,
    eut=0,
    custom_args={
        "do_not_overclock": True,
    },
)
reactor.set_target_machine_number(8)


g.add(fuelProd)
g.add(reactor)
g.write_to_file("mk1-output.yaml")
