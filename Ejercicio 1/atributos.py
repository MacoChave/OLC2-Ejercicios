class Atributo:
    temp = ''
    c3d = ''
    true_label = []
    false_label = []
    
    def __init__(self, temp, c3d, true_label = [], false_label = []) -> None:
        self.temp = temp
        self.c3d = c3d
        self.true_label = true_label
        self.false_label = false_label