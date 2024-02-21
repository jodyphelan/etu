from .interface import Interface, Result
import json

class PyMOI(Interface):
    def parse(self,infile:str) -> None:
        data = json.load(open(infile, 'r'))
        id = infile.split('/')[-1].split('.')[0]
        self.result = Result(
            id=id, 
            coi=data['moi'], 
            software=data['software'], 
            version=data['version'])
