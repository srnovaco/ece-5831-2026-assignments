import logic_gate as lg

logic_gate = lg.LogicGate()

logic_gate.print_output("OR", 0, 0)
logic_gate.print_output("OR", 0, 1)
logic_gate.print_output("OR", 1, 0)
logic_gate.print_output("OR", 1, 1)
print()

logic_gate.print_output("NOR", 0, 0)
logic_gate.print_output("NOR", 0, 1)
logic_gate.print_output("NOR", 1, 0)
logic_gate.print_output("NOR", 1, 1)
print()


logic_gate.print_output("AND", 0, 0)
logic_gate.print_output("AND", 0, 1)
logic_gate.print_output("AND", 1, 0)
logic_gate.print_output("AND", 1, 1)
print()

logic_gate.print_output("NAND", 0, 0)
logic_gate.print_output("NAND", 0, 1)
logic_gate.print_output("NAND", 1, 0)
logic_gate.print_output("NAND", 1, 1)
print()

logic_gate.print_output("XOR", 0, 0)
logic_gate.print_output("XOR", 0, 1)
logic_gate.print_output("XOR", 1, 0)
logic_gate.print_output("XOR", 1, 1)
print()