import os

class Memory:
    def __init__(self) -> None:
        self.BASE_URL = os.getcwd()
        self.short_term_path = os.path.join(self.BASE_URL,"shortTerm.txt")
        