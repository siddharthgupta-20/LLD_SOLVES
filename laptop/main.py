
from laptopbuilder import LaptopBuilder

laptop = LaptopBuilder().build_color("red").build_graphic("AMD").build_processor("intel").build_ram("16").build()

laptop.show_build()