# from PIL import Image, ImageDraw, ImageFont
# import json
#
# template = "1"
# config = ""
# with open('template-config.json') as configFile:
#     config = json.load(configFile)[template]
#
# certificate = Image.open('templates/' + template + '.jpg')
# drawHandler = ImageDraw.Draw(certificate)
# values = ['Lakshya Khatri', 'Data Science', 'Lakshya Khatri', '10 / May / 2020', 'LAKSHYA KHATRI']
#
# i = 0
# for field in config:
#     if field['type'] == 'text':
#         fieldValue = values[i]
#         font = ImageFont.truetype('fonts/' + field['font'], field['size'])
#         textWidth, textHeight = drawHandler.textsize(fieldValue, font=font)
#         drawHandler.text((field['x'] - (textWidth // 2), field['y'] - (textHeight // 2)),
#                          fieldValue, fill=field['color'], font=font)
#         i += 1
#
#     elif field['type'] == 'image':
#         image = Image.open(field['path']).convert('RGBA')
#         imageWidth, imageHeight = image.size
#         certificate.paste(image, (field['x'] - (imageWidth // 2),
#                                   field['y'] - (imageHeight // 2)), image)
#
# certificate.save('../certificates/' + values[0] + '.pdf')

import argparse


def certify():
    pass


def main():
    parser = argparse.ArgumentParser(
        prog='certify',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('template', type=int, help='template to use')
    parser.add_argument('-i', '--input', help='name of the input CSV file',
                        default=False)
    parser.add_argument('-o', '--output', help='output directory',
                        default='./')
    certify(parser.parse_args())


if __name__ == '__main__':
    main()
