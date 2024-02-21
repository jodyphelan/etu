from pydantic import BaseModel
from abc import ABC, abstractmethod
import argparse

class Result(BaseModel):
    id: str
    coi: int
    software: str
    version: str

class Interface(ABC):
    def __init__(self):
        self.result = None

    @abstractmethod
    def parse(self) -> None:
        pass

    def write_result(self, args: argparse.Namespace):
        self.parse(args.infile)
        with open(args.outfile, 'w') as O:
            O.write(self.result.model_dump_json())

    def add_subparser(self,subparsers: argparse._SubParsersAction):
        subparser = subparsers.add_parser(self.__class__.__name__ , help='Parse result file for COI/MOI analysis')
        subparser.add_argument('infile', help='Name of input file to parse')
        subparser.add_argument('outfile', help='Name of unified result file')
        subparser.set_defaults(func=self.write_result)