import itertools
import re


def heading(title):
    print("\n" + "=" * 64)
    print(title.center(64))
    print("=" * 64)


def pause():
    input("\nPress ENTER to return...")


def notes(title, text):
    heading(title)
    print(text)
    pause()


# ============================================================
# 1. BINARY SYSTEMS & CALCULATIONS
# ============================================================

BINARY_NOTES = """
BINARY SYSTEM
- Binary is base 2 and uses only 0 and 1.
- 1 is HIGH; 0 is LOW.
- Each position is a power of 2.

PLACE VALUES (right to left)
2^7  2^6  2^5  2^4  2^3  2^2  2^1  2^0
128   64   32   16    8    4    2    1

BINARY -> DECIMAL
Multiply each bit by its place value, then add.
Example: 1101_2 = 8 + 4 + 0 + 1 = 13_10.

DECIMAL -> BINARY
Repeatedly divide by 2. Record remainders.
Read remainders from BOTTOM to TOP.
Example:
13 / 2 = 6 remainder 1
 6 / 2 = 3 remainder 0
 3 / 2 = 1 remainder 1
 1 / 2 = 0 remainder 1
Answer: 1101_2.

BINARY ADDITION
0+0=0
0+1=1
1+0=1
1+1=10       (write 0, carry 1)
1+1+1=11     (write 1, carry 1)

ASCII
- ASCII = American Standard Code for Information Interchange.
- Represents characters using numeric codes.
- Includes letters, digits and punctuation.
- Standard ASCII codes range from 0 to 127.

MEMORY SIZE (base-2 convention in the workbook)
1 bit = one binary digit
1 byte = 8 bits
1 KByte = 1024 bytes = 2^10 bytes
1 MByte = 1024 KByte
1 GByte = 1024 MByte
1 TByte = 1024 GByte

For n binary inputs, number of combinations = 2^n.
2 inputs = 4 rows; 3 inputs = 8 rows; 4 inputs = 16 rows.
"""


def binary_to_decimal():
    heading("BINARY -> DECIMAL")
    value = input("Binary number: ").strip()
    if not value or any(c not in "01" for c in value):
        print("Invalid binary number. Use only 0 and 1.")
        return
    total = 0
    for p, bit in enumerate(reversed(value)):
        amount = int(bit) * (2 ** p)
        print(f"{bit} x 2^{p} = {amount}")
        total += amount
    print(f"Answer: {value}_2 = {total}_10")


def decimal_to_binary():
    heading("DECIMAL -> BINARY")
    try:
        number = int(input("Non-negative whole number: "))
        if number < 0:
            raise ValueError
    except ValueError:
        print("Enter a non-negative whole number.")
        return
    if number == 0:
        print("Answer: 0_10 = 0_2")
        return
    original, remainders = number, []
    while number:
        quotient, remainder = divmod(number, 2)
        print(f"{number} / 2 = {quotient} remainder {remainder}")
        remainders.append(str(remainder))
        number = quotient
    print("Read remainders from bottom to top.")
    print(f"Answer: {original}_10 = {''.join(reversed(remainders))}_2")


def binary_addition():
    heading("BINARY ADDITION")
    a = input("First binary number: ").strip()
    b = input("Second binary number: ").strip()
    if not a or not b or any(c not in "01" for c in a + b):
        print("Use only 0 and 1.")
        return
    result = bin(int(a, 2) + int(b, 2))[2:]
    width = max(len(a), len(b), len(result))
    print(a.rjust(width))
    print("+" + b.rjust(width))
    print("-" * (width + 1))
    print(result.rjust(width))
    print(f"Answer: {a}_2 + {b}_2 = {result}_2")


def ascii_lookup():
    heading("ASCII LOOKUP")
    char = input("Enter one character: ")
    if len(char) != 1:
        print("Enter exactly one character.")
        return
    code = ord(char)
    if code > 127:
        print("Outside standard ASCII (0-127).")
        return
    print("Character:", repr(char))
    print("Decimal code:", code)
    print("8-bit binary:", format(code, "08b"))


def binary_menu():
    while True:
        heading("1. BINARY SYSTEMS & CALCULATIONS")
        print("1. Revision notes")
        print("2. Binary -> decimal")
        print("3. Decimal -> binary")
        print("4. Binary addition")
        print("5. ASCII lookup")
        print("0. Main menu")
        c = input("Choose: ").strip()
        if c == "1":
            notes("BINARY NOTES", BINARY_NOTES)
        elif c == "2":
            binary_to_decimal(); pause()
        elif c == "3":
            decimal_to_binary(); pause()
        elif c == "4":
            binary_addition(); pause()
        elif c == "5":
            ascii_lookup(); pause()
        elif c == "0":
            return
        else:
            print("Invalid choice."); pause()


# ============================================================
# 2. COMPUTER SYSTEMS & ARCHITECTURE
# ============================================================

COMPUTER_NOTES = """
COMPUTER COMPONENTS
- Input: accepts data/commands (keyboard, mouse, microphone, camera, sensors).
- Output: displays or produces results (monitor, printer, speakers, actuators).
- Motherboard: main circuit board connecting components.
- I/O ports: connection points for external physical devices.
- Hardware: physical components.
- Software: programs that instruct hardware what tasks to perform.
- Operating System: first software to run when computer starts.

CPU (CENTRAL PROCESSING UNIT)
- Processes inputs and activates/triggers outputs.
- CU (Control Unit): handles instructions and manages data flow.
- ALU (Arithmetic & Logic Unit): performs mathematical and logic calculations.
- Memory: stores data.
- Workbook describes Von Neumann architecture (1945), and notes modern CPUs
  combine aspects of Harvard architecture with separate data/instruction caches.

INSTRUCTION CYCLE
FETCH -> DECODE -> EXECUTE -> STORE
Fetch: retrieve instruction.
Decode: determine what it means.
Execute: perform the instruction.
Store: store the result when needed.
The cycle repeats as the CPU processes instructions.

BUSES
- Bus: electrical pathway connecting I/O ports, CPU and memory.
- Allows components to communicate.
- Bus width: number of bits transmitted at one time.

ADDRESS BUS
- Carries the address/location of a memory location or I/O port.
- Unidirectional: CPU sends the address.

DATA BUS
- Carries actual data between CPU, memory and I/O.
- Bidirectional: data can travel both ways.

CONTROL BUS
- Carries control signals such as READ and WRITE.
- Workbook describes it as bidirectional: CPU sends control type;
  devices return handshaking status such as interrupt/acknowledgement.

MEMORY
RAM (Random Access Memory)
- Volatile: data is lost when power is off.
- Used for active tasks and temporary working data.
- Very fast; smaller capacity than storage.

ROM (Read-Only Memory)
- Non-volatile: data remains when power is off.
- Workbook describes it as used for system startup and saved files.
- Workbook comparison describes it as slower and larger-capacity than RAM.

CACHE
- Between CPU and RAM.
- Very fast, but slower than registers.
- Stores frequently used data and reduces delay from RAM.

REGISTERS
- Inside CPU, very close to ALU.
- Fastest memory; very small (few bytes).
- Holds data currently being processed and used directly in calculations.

SECONDARY / EXTERNAL STORAGE
- HDD, portable HDD, SSD and cloud storage.
- Stores files/programs for long-term or archival storage.
- Saved files on disk remain when power is off.

POWER FAILURE
- Data stored only in volatile RAM is lost.
- Unsaved work can be lost.
- Files already saved on disk/SSD remain.

QUICK SPEED / ROLE REMINDER
Registers: fastest, smallest, inside CPU.
Cache: very fast, between CPU and RAM.
RAM: fast temporary working memory, volatile.
ROM: non-volatile memory used for system startup.
Secondary storage: long-term files and programs.
"""


def computer_menu():
    while True:
        heading("2. COMPUTER SYSTEMS & ARCHITECTURE")
        print("1. Complete revision notes")
        print("2. CPU and instruction cycle")
        print("3. Bus comparison")
        print("4. Memory comparison")
        print("0. Main menu")
        c = input("Choose: ").strip()
        if c == "1":
            notes("COMPUTER SYSTEMS & ARCHITECTURE", COMPUTER_NOTES)
        elif c == "2":
            notes("CPU & INSTRUCTION CYCLE", """
CU = Control Unit: handles instructions and manages data flow.
ALU = Arithmetic & Logic Unit: mathematical and logic calculations.
Memory stores data.

FETCH -> DECODE -> EXECUTE -> STORE
Fetch = retrieve instruction.
Decode = determine meaning.
Execute = perform instruction.
Store = store result when needed.
""")
        elif c == "3":
            notes("SYSTEM BUSES", """
ADDRESS BUS: carries memory/I/O location; unidirectional.
DATA BUS: carries actual data; bidirectional.
CONTROL BUS: carries control signals (e.g. READ/WRITE);
workbook describes it as bidirectional.
BUS WIDTH: number of bits transmitted at one time.
""")
        elif c == "4":
            notes("MEMORY COMPARISON", """
REGISTERS: inside CPU; fastest; very small; currently processed data.
CACHE: between CPU and RAM; very fast; frequently used data.
RAM: volatile; active tasks; data lost when power is off.
ROM: non-volatile; used for system startup in workbook.
SECONDARY STORAGE: HDD/SSD/cloud; long-term files and programs.
""")
        elif c == "0":
            return
        else:
            print("Invalid choice."); pause()


# ============================================================
# 3. BOOLEAN ALGEBRA -> TRUTH TABLE
# ============================================================

BOOLEAN_NOTES = """
BOOLEAN ALGEBRA
- Mathematics used in digital systems to study and analyse logic circuits.
- Variables have two possible values: 0 or 1.
- Number of truth-table rows = 2^n, where n is number of inputs.

NOTATION
AND: A.B or A*B       OR: A+B
NOT: A'               XOR: A^B
NAND: (A.B)'          NOR: (A+B)'

BOOLEAN IDENTITIES
Identity:       A+0=A       A.1=A
Null:           A+1=1       A.0=0
Idempotent:     A+A=A       A.A=A
Complement:     A+A'=1      A.A'=0
Double NOT:     (A')'=A
Commutative:    A+B=B+A     A.B=B.A
Associative:    (A+B)+C=A+(B+C)
                (A.B).C=A.(B.C)
Distributive:   A.(B+C)=A.B+A.C
                A+(B.C)=(A+B).(A+C)
Absorption:     A+A.B=A     A.(A+B)=A

DE MORGAN'S THEOREM
(A.B)' = A' + B'
(A+B)' = A'.B'
When a NOT bar moves across brackets:
1. Complement each variable.
2. Swap AND and OR.

Simplification can reduce the number of gates, cost and power.

CONVERTER INPUT
+ = OR
. or * = AND
' = NOT (postfix complement)
Brackets = grouping
Examples: A.B + C'
          (A+B)'.C
          A.B + A.C
          (A+B).(C+D)
"""


class BooleanParser:
    """Parses NOT > AND > OR; supports implied AND such as AB."""

    def __init__(self, expression):
        self.expression = expression.upper().replace(" ", "")
        self.tokens = re.findall(r"[A-Z][A-Z0-9_]*|[01]|[()+.*'!~]",
                                 self.expression)
        if "".join(self.tokens) != self.expression or not self.tokens:
            raise ValueError("Unrecognised character or empty expression.")
        self.pos = 0
        self.variables = sorted(set(
            t for t in self.tokens
            if re.fullmatch(r"[A-Z][A-Z0-9_]*", t)
        ))

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def take(self):
        token = self.peek()
        if token is not None:
            self.pos += 1
        return token

    def parse(self):
        tree = self.parse_or()
        if self.peek() is not None:
            raise ValueError("Unexpected token: " + str(self.peek()))
        return tree

    def parse_or(self):
        node = self.parse_and()
        while self.peek() == "+":
            self.take()
            node = ("OR", node, self.parse_and())
        return node

    def parse_and(self):
        node = self.parse_unary()
        while True:
            t = self.peek()
            if t in (".", "*"):
                self.take()
                node = ("AND", node, self.parse_unary())
            elif (t == "(" or t in ("!", "~") or
                  (t is not None and
                   (re.fullmatch(r"[A-Z][A-Z0-9_]*", t) or t in ("0", "1")))):
                node = ("AND", node, self.parse_unary())
            else:
                break
        return node

    def parse_unary(self):
        if self.peek() in ("!", "~"):
            self.take()
            return ("NOT", self.parse_unary())
        node = self.parse_primary()
        while self.peek() == "'":
            self.take()
            node = ("NOT", node)
        return node

    def parse_primary(self):
        t = self.take()
        if t is None:
            raise ValueError("Unexpected end of expression.")
        if t == "(":
            node = self.parse_or()
            if self.take() != ")":
                raise ValueError("Missing closing bracket.")
            return node
        if re.fullmatch(r"[A-Z][A-Z0-9_]*", t):
            return ("VAR", t)
        if t in ("0", "1"):
            return ("CONST", int(t))
        raise ValueError("Unexpected token: " + t)


def eval_boolean(tree, values):
    kind = tree[0]
    if kind == "VAR":
        return int(values[tree[1]])
    if kind == "CONST":
        return tree[1]
    if kind == "NOT":
        return 1 - eval_boolean(tree[1], values)
    if kind == "AND":
        return int(eval_boolean(tree[1], values) and
                   eval_boolean(tree[2], values))
    if kind == "OR":
        return int(eval_boolean(tree[1], values) or
                   eval_boolean(tree[2], values))


def boolean_converter():
    heading("BOOLEAN EXPRESSION -> TRUTH TABLE")
    print("Use + for OR, . or * for AND, ' for NOT.")
    print("Brackets are supported. Example: (A+B').C")
    expression = input("\nBoolean expression: ").strip()
    try:
        parser = BooleanParser(expression)
        tree = parser.parse()
        variables = parser.variables
        if len(variables) > 4:
            print("Maximum supported: 4 variables.")
            return
        if not variables:
            print("Output:", eval_boolean(tree, {}))
            return
        print("\nExpression:", expression)
        print("Rows:", 2 ** len(variables))
        print(" | ".join(variables) + " | Y")
        print("-" * (len(variables) * 4 + 6))
        for combo in itertools.product([0, 1], repeat=len(variables)):
            values = dict(zip(variables, combo))
            row = [str(values[v]) for v in variables]
            row.append(str(eval_boolean(tree, values)))
            print(" | ".join(row))
    except ValueError as error:
        print("Could not parse expression:", error)


def boolean_menu():
    while True:
        heading("3. BOOLEAN ALGEBRA")
        print("1. Revision notes and laws")
        print("2. Boolean expression -> truth table")
        print("0. Main menu")
        c = input("Choose: ").strip()
        if c == "1":
            notes("BOOLEAN ALGEBRA NOTES", BOOLEAN_NOTES)
        elif c == "2":
            boolean_converter(); pause()
        elif c == "0":
            return
        else:
            print("Invalid choice."); pause()


# ============================================================
# 4. FLOWCHARTS & PROGRAM PLANNING
# ============================================================

FLOWCHART_NOTES = """
PROBLEM SPECIFICATIONS: INPUT / PROCESS / OUTPUT

INPUTS
- What information is entered?
- Example: supervisor name, weight per box, number of boxes.

PROCESSING
- What calculation or action is needed?
- Example: cargo_wt = wt_box * num_box.

OUTPUTS
- What result must be displayed?
- Example: total cargo weight.

FLOWCHART
- Shows the sequence of steps from start to finish.
- Does not depend on a particular programming language.
- Arrows / flowlines show the direction of the process.

COMMON FLOWCHART SYMBOLS
OVAL / ROUNDED TERMINATOR: Start / End.
PARALLELOGRAM: Input / Output (read or display data).
RECTANGLE: Process (calculation, assignment, initialisation).
DIAMOND: Decision (condition, often Yes / No branches).
ARROW / FLOWLINE: Direction of flow.

FLOWCHART CONVENTIONS
- Have a clear Start and End.
- Connect steps with arrows.
- Label decision branches (e.g. Yes / No).
- Keep the flow easy to follow, usually top to bottom.
- A process box contains an action.
- A decision diamond contains a condition/question.

PROGRAM PLANNING
1. Understand the problem.
2. Identify inputs.
3. Identify processing / calculations.
4. Identify outputs.
5. Arrange steps in the correct sequence.
6. Represent the algorithm using a flowchart or pseudocode.
7. Translate the plan into code.
8. Test using suitable data and check the result.

VARIABLE INITIALISATION
- Workbook recommends numeric variables start at 0.
- Workbook recommends text variables start at "".
- Initialisation makes starting values clear.

PSEUDOCODE
- Plain-language description of an algorithm.
- Not tied to exact syntax of a programming language.
- Common words: INPUT, SET, CALCULATE, IF, ELSE, OUTPUT.

BASIC CONTROL STRUCTURES
SEQUENCE: instructions run one after another.
SELECTION: choose a path based on a condition (IF / ELSE).
ITERATION: repeat instructions (loop).

EXAMPLE: TOTAL CARGO WEIGHT
START
INPUT weight_per_box
INPUT number_of_boxes
total_weight = weight_per_box * number_of_boxes
OUTPUT total_weight
END
"""


def flowchart_menu():
    while True:
        heading("4. FLOWCHARTS & PROGRAM PLANNING")
        print("1. Complete revision notes")
        print("2. IPO / problem specifications")
        print("3. Flowchart symbols")
        print("4. Pseudocode and control structures")
        print("0. Main menu")
        c = input("Choose: ").strip()
        if c == "1":
            notes("FLOWCHARTS & PROGRAM PLANNING", FLOWCHART_NOTES)
        elif c == "2":
            notes("INPUT / PROCESS / OUTPUT", """
INPUT: What information is entered?
PROCESS: What calculation/action is required?
OUTPUT: What result must be displayed?

Example:
Input: weight_per_box, number_of_boxes
Process: total_weight = weight_per_box * number_of_boxes
Output: total_weight
""")
        elif c == "3":
            notes("FLOWCHART SYMBOLS", """
OVAL / ROUNDED TERMINATOR = Start / End
PARALLELOGRAM = Input / Output
RECTANGLE = Process / calculation / assignment
DIAMOND = Decision / condition (Yes or No branches)
ARROW / FLOWLINE = Direction of flow
""")
        elif c == "4":
            notes("PSEUDOCODE & CONTROL STRUCTURES", """
Pseudocode describes an algorithm in plain language.

SEQUENCE: steps run in order.
SELECTION: choose a path (IF / ELSE).
ITERATION: repeat steps (loop).

Example:
START
INPUT mark
IF mark >= 50
    OUTPUT "Pass"
ELSE
    OUTPUT "Try again"
END IF
END
""")
        elif c == "0":
            return
        else:
            print("Invalid choice."); pause()


# ============================================================
# 5. LOGIC CIRCUIT BUILDER & SOLVER
# ============================================================

def gate_result(gate, a, b=None):
    if gate == "NOT":
        return 1 - a
    if gate == "AND":
        return int(a and b)
    if gate == "OR":
        return int(a or b)
    if gate == "NAND":
        return int(not (a and b))
    if gate == "NOR":
        return int(not (a or b))
    if gate == "XOR":
        return int(a != b)


def overline(text):
    # Combining overline characters; rendering depends on console font.
    return "".join(char + "\u0305" for char in text)


def circuit_solver():
    heading("LOGIC CIRCUIT BUILDER & SOLVER")
    print("Build gates from left to right.")
    print("Available gates: NOT, AND, OR, NAND, NOR, XOR")
    try:
        n = int(input("How many original inputs? (2, 3 or 4): "))
        while n not in (2, 3, 4):
            n = int(input("Enter 2, 3 or 4: "))
        gate_count = int(input("How many gates? "))
        if gate_count < 1:
            print("Enter at least one gate.")
            return
    except ValueError:
        print("Enter whole numbers.")
        return

    input_names = ["A", "B", "C", "D"][:n]
    gate_names, gates = [], []

    for i in range(gate_count):
        print(f"\n--- GATE {i + 1} ---")
        kind = input("Gate type: ").strip().upper()
        while kind not in ("NOT", "AND", "OR", "NAND", "NOR", "XOR"):
            kind = input("Choose NOT, AND, OR, NAND, NOR or XOR: ").strip().upper()

        available = input_names + gate_names
        print("Available connections:", ", ".join(available))
        first = input("What connects to input 1? ").strip().upper()
        while first not in available:
            first = input("Choose from " + str(available) + ": ").strip().upper()

        second = None
        if kind != "NOT":
            second = input("What connects to input 2? ").strip().upper()
            while second not in available:
                second = input("Choose from " + str(available) + ": ").strip().upper()

        name = input("Name this output line (e.g. E): ").strip().upper()
        while not re.fullmatch(r"[A-Z][A-Z0-9_]*", name) or name in input_names + gate_names:
            name = input("Enter a valid unused output name: ").strip().upper()

        gates.append([kind, first, second])
        gate_names.append(name)

    print("\nAvailable final outputs:", ", ".join(gate_names))
    final = input("Which output produces Y? ").strip().upper()
    while final not in gate_names:
        final = input("Choose from " + str(gate_names) + ": ").strip().upper()

    def expression_for(connection):
        if connection in input_names:
            return connection
        i = gate_names.index(connection)
        kind, first, second = gates[i]
        left = expression_for(first)
        if kind == "NOT":
            return overline("(" + left + ")")
        right = expression_for(second)
        if kind == "AND":
            return "(" + left + " . " + right + ")"
        if kind == "OR":
            return "(" + left + " + " + right + ")"
        if kind == "NAND":
            return overline("(" + left + " . " + right + ")")
        if kind == "NOR":
            return overline("(" + left + " + " + right + ")")
        return "(" + left + " XOR " + right + ")"

    columns = input_names + gate_names
    print("\n===== COMPLETE TRUTH TABLE =====")
    print(" | ".join(columns))
    print("-" * (len(columns) * 4 + 3))

    for combo in itertools.product([0, 1], repeat=n):
        values = dict(zip(input_names, combo))
        for i, (kind, first, second) in enumerate(gates):
            a = values[first]
            b = values[second] if second is not None else None
            values[gate_names[i]] = gate_result(kind, a, b)
        print(" | ".join(str(values[col]) for col in columns))

    print("\n===== BOOLEAN EXPRESSION =====")
    print("Y =", expression_for(final))


# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:
        heading("DIGITAL LOGIC & PROGRAMMING")
        print("                 MASTER CHEATSHEET\n")
        print("1. Binary Systems & Calculations")
        print("2. Computer Systems & Architecture")
        print("3. Boolean Algebra -> Truth Table Converter")
        print("4. Flowcharts & Program Planning")
        print("5. Logic Circuit Builder & Solver")
        print("0. Exit")
        choice = input("\nChoose a section: ").strip()

        if choice == "1":
            binary_menu()
        elif choice == "2":
            computer_menu()
        elif choice == "3":
            boolean_menu()
        elif choice == "4":
            flowchart_menu()
        elif choice == "5":
            circuit_solver(); pause()
        elif choice == "0":
            print("Good luck with your revision!")
            break
        else:
            print("Invalid choice."); pause()


if __name__ == "__main__":
    main()
