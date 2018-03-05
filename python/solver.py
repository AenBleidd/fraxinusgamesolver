import json

class Row:
    def __init__(self, value, offset = None):
        self.offset = offset
        self.value = value

    def print(self):
        print("value:", self.value)
        print("offset:", self.offset)

class Task:
    def __init__(self, pattern, rows, target):
        self.pattern = pattern
        self.rows = rows
        self.target = target

    def print(self):
        print("pattern:", self.pattern)
        print("target:", self.target)
        print("rows:")
        for r in self.rows:
            r.print()

class Result:
    def __init__(self, rows, score = None):
        self.rows = rows
        self.score = score

    def print(self):
        print("score:", self.score)
        print("rows:")
        for r in self.rows:
            r.print()

class Solver:
    def __init__(self):
        self.task = None
        self.result = None

    def loadTask(self, file):
        f = open(file)
        task = json.load(f)
        f.close()
        rows = []
        for r in task["rows"]:
            rows.append(Row(r))
        self.task = Task(task["pattern"], rows, task["target"])

    def loadResult(self, file):
        f = open(file)
        result = json.load(f)
        f.close()
        rows = []
        for r in result["result"]["rows"]:
            rows.append(Row(r["row"], r["offset"]))
        self.result = Result(rows, result["result"]["score"])

    def printTask(self):
        if self.task is None:
            return
        print("task:")
        self.task.print()

    def printResult(self):
        if self.result is None:
            return
        print("result:")
        self.result.print()

    def print(self):
        self.printTask()
        self.printResult()
        
