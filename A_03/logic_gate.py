import numpy as np

class LogicGate:
    def print_output(self, gate, x1, x2):
        match gate:
            case "OR":
                out = self.or_gate(x1, x2)            
            case "NOR":
                out = self.nor_gate(x1, x2)
            case "AND":
                out = self.and_gate(x1, x2)
            case "NAND":
                out = self.nand_gate(x1, x2)
            case "XOR":
                out = self.xor_gate(x1, x2)
            case _:
                raise ValueError(f"Unknown logic gate: '{gate}'")

        print(f"Output of {gate} logic is: {out}, with x1 = {x1}, x2 = {x2}")

    def not_gate(self, x1):
        if x1 == 1:
            return 0
        else:
            return 1

    def or_gate(self, x1, x2):
        w1 = 0.5
        w2 = 0.5
        th = 0.0
        
        x = np.array([x1, x2])
        w = np.array([w1, w2])

        if np.dot(x, w) > th:
            return 1
        else:
            return 0

    def nor_gate(self, x1, x2):
        return self.not_gate(self.or_gate(x1, x2))

    def and_gate(self, x1, x2):
        w1 = 0.5
        w2 = 0.5
        th = 0.99

        x = np.array([x1, x2])
        w = np.array([w1, w2])

        if np.dot(x,w) > th:
            return 1
        else:
            return 0

    def nand_gate(self, x1, x2):
        return self.not_gate(self.and_gate(x1, x2))

    def xor_gate(self, x1, x2):
        c = self.or_gate(x1, x2)
        d = self.nand_gate(x1, x2)
        return self.and_gate(c, d)
