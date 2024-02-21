import argparse
from etu.coi.interface import Interface as COIInterface

base_classes = [COIInterface]


def main():
    parser = argparse.ArgumentParser(description='Etract-Transform-Unify CLI')
    subparsers_type = parser.add_subparsers(help='Type of result to parse', dest='subparser_name')
    for base_class in base_classes:
        parser_software = subparsers_type.add_parser('COI', help='Parse result file for COI/MOI analysis')
        subparser_software = parser_software.add_subparsers(help='Software to parse', dest='subparser_software')
        for interface in base_class.__subclasses__():
            interface().add_subparser(subparser_software)

    args = parser.parse_args()

    if hasattr(args,'func'):
        args.func(args)
    else:
        parser.print_help()