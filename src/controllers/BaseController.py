class BaseController:
    def __init__(self, frame, model) -> None:
        self.frame = frame()
        self.model = model()

    def cut(self): pass

    def add(self): pass
