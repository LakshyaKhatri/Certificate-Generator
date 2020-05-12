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
import json
import sys


class Certify:
    def __init__(self, template, input, output):
        self.__template = template
        self.__input = input
        self.__output = output
        self.__has_more_input = True
        self.__fields = []
        self.__config()

    def __ask_for_input(self):
        print('[certify] Enter field values:')
        for i in range(len(self.__fields)):
            self.__fields[i]['value'] = input(
                '[certify] ' + self.__fields[i]['name'] + ':'
            )
        return False

    def __config(self):
        try:
            with open('template-config.json') as configFile:
                # configure fields for specified template
                self.__fields = json.load(configFile)[self.__template]
        except FileNotFoundError:
            sys.exit("[certify] Configuration Error: Missing configuration file")
        except json.decoder.JSONDecodeError as e:
            print("[certify] Configuration Error: Invalid JSON Format")
            sys.exit(str(e))
        except Exception as e:
            sys.exit(str(e))
        print("[certify] Using template " + self.__template + '.jpg')

    def __parse_csv(self):
        pass

    def has_next_input(self):
        return self.__has_more_input

    def generate_certificate(self):
        pass

    def next_input(self):
        # if input CSV file is not provided
        if not self.__input:
            # ask user for prividing values
            self.__has_more_input = self.__ask_for_input()
        else:
            # set values from CSV file
            self.__has_more_input = self.__parse_csv()


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
    args = parser.parse_args()

    # This object will handle certificate generation
    certify = Certify(args.template, args.input, args.output)
    while certify.has_next_input():
        certify.next_input()
        certify.generate_certificate()


if __name__ == '__main__':
    main()
