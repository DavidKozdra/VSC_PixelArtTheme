from PIL import Image, ImageOps
import os

os.makedirs("icons", exist_ok=True)
os.makedirs("icons/128", exist_ok=True)

def process(fn, size, outdir):
    img = Image.open(fn).convert("RGBA")
    img.thumbnail((size,size), Image.NEAREST)
    bg = Image.new("RGBA", (size,size), (255,255,255,0))
    bg.paste(img, ((size-img.width)//2, (size-img.height)//2), img)
    bg.save(os.path.join(outdir, os.path.basename(fn)))

for fn in os.listdir("icons"):
    if fn.lower().endswith(".png"):
        process(os.path.join("icons",fn), 64, "icons")
        process(os.path.join("icons",fn), 128, "icons/128")
