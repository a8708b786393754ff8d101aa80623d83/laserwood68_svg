#! /usr/bin/python3
from src.models.PersonneModel import PersonneModel
from src.models.CadreModel import CadreModel

personn = PersonneModel('svg/famille.svg')
personn.parse()
root = personn.root()
print(root.attrib)
