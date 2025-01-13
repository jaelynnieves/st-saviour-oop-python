from beauty import Beauty

class Hair(Beauty):
    def __init__(self, brand: str, styles: list, design: str):
        super().__init__(brand, styles)
        self.design = design
        