# tests/utils/visual_diff.py
from PIL import Image, ImageChops
import math

class VisualDiff:
    def compare(self, img1, img2):
        a = Image.open(img1).convert("RGB")
        b = Image.open(img2).convert("RGB")
        diff = ImageChops.difference(a, b)
        h = diff.histogram()
        rms = math.sqrt(sum(value * (idx % 256) ** 2 for idx, value in enumerate(h)) / (a.size[0] * a.size[1]))
        percent = (rms / 255) * 100
        return round(percent, 2)
