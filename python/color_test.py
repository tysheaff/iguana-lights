import board
import neopixel
import time
import helpers
from random import randrange, uniform
from colour import Color

PIN = board.D18
PIXELS_PER_STRAND = 50
NUM_STRANDS = 1
NUM_PIXELS = PIXELS_PER_STRAND * NUM_STRANDS

pixels = neopixel.NeoPixel(PIN, NUM_PIXELS, auto_write=False)
pixel_colors = list(map(lambda x: Color("#000000"), [None] * NUM_PIXELS))

while True:
    pixels.fill(helpers.color_to_rgb(helpers.random_color()))
    time.sleep(2.0)
