
userid = "7618438"
import random
import hashlib

class TestData:
    def __init__(self):
        pass
    def createphone(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))
    # @ staticmethod
    def get(name):
        if name == "hooli":
            data = [
                ("13520843514","中国","123456")
            ]
        return name



