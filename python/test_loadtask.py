import os
from solver import Solver

solver = Solver()
solver.loadTask(os.path.join(os.path.dirname(__file__), "../templates/01t.json"))
solver.printTask()

