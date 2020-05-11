from PIL import Image, ImageDraw, ImageFont
import json

template = "1"
config = ""
with open('template-config.json') as configFile:
    config = json.load(configFile)[template]

certificate = Image.open('templates/' + template + '.jpg')
drawHandler = ImageDraw.Draw(certificate)
values = ['Lakshya Khatri', 'Data Science', 'Lakshya Khatri', '10 / May / 2020', 'LAKSHYA KHATRI']

i = 0
for field in config:
    if field['type'] == 'text':
        fieldValue = values[i]
        font = ImageFont.truetype('fonts/' + field['font'], field['size'])
        textWidth, textHeight = drawHandler.textsize(fieldValue, font=font)
        drawHandler.text((field['x'] - (textWidth // 2), field['y'] - (textHeight // 2)),
                         fieldValue, fill=field['color'], font=font)
        i += 1

    elif field['type'] == 'image':
        image = Image.open(field['path']).convert('RGBA')
        imageWidth, imageHeight = image.size
        certificate.paste(image, (field['x'] - (imageWidth // 2),
                                  field['y'] - (imageHeight // 2)), image)

certificate.save('../certificates/' + values[0] + '.pdf')
