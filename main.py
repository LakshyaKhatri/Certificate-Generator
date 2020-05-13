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
    args = parser.parse_args()

    # This object will handle certificate generation
    certify = Certify(args.template, args.input)
    while certify.has_next_input():
        certify.next_input()
        certify.generate_certificate()


if __name__ == '__main__':
    main()
