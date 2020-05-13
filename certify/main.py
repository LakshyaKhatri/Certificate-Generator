from certify import Certify
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='certify',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('template', help='template to use')
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