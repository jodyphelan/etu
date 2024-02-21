import argparse
from .interface import Interface


def runner(args):
    interface = [i for i in Interface.__subclasses__() if i.__name__ == args.type][0](args.filename)
    interface.parse()
    interface.write_result(args.outfile)


def add_subparser(subparsers: argparse._SubParsersAction):
    list_of_interfaces = [i.__name__ for i in Interface.__subclasses__()]
    subparser = subparsers.add_parser('COI', help='Parse result file for COI/MOI analysis')
    subparser.add_argument('type', choices=list_of_interfaces, help='Software used to generate result')
    subparser.add_argument('filename', help='Name of input file to parse')
    subparser.add_argument('outfile', choices=list_of_interfaces, help='Name of unified result file')
    subparser.set_defaults(func=runner)



