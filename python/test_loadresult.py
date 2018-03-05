import os
from solver import Solver

solver = Solver()
solver.loadResult(os.path.join(os.path.dirname(__file__), "../templates/01r.json"))
solver.printResult()

