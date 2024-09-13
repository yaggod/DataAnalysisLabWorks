from PIL import Image, ImageDraw


def draw_border(drawer : ImageDraw.ImageDraw, borderSize : int, color : tuple[int, int, int]) -> None:
    
    drawer.rectangle([0, 0, drawer._image.size[0], borderSize], fill=color)
    drawer.rectangle([0, 0, borderSize, drawer._image.size[1]], fill=color)
    drawer.rectangle([drawer._image.size[0] - borderSize, 0, drawer._image.size[0], drawer._image.size[1]], fill=color)
    drawer.rectangle([0, drawer._image.size[1] - borderSize, drawer._image.size[0], drawer._image.size[1]], fill=color)
    return

def create_card(text : str) -> Image.Image:
    result = Image.new("RGB", (100, 100))
    drawer = ImageDraw.Draw(result)

    draw_border(drawer, 5, (0, 0, 255))
    drawer.text((50, 50), text, fill=(255, 0, 0), anchor="mm")
    return result



for i in range(1, 4):
    image = create_card(str(i))
    image.show()
    image.save(f"card_{i}.png")