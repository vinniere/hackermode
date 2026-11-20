"""
DIGITAL LOGIC & PROGRAMMING — INTERACTIVE CHEAT SHEET
Designed for the PFP Student Workbook AY2026/2027.
Uses only Python's standard library (Tkinter).

Run in Spyder:
1. Save this file as digital_logic_cheatsheet.py
2. Run it with F5.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import ast
import operator


# ----------------------------- Reference content -----------------------------

CHEAT_SHEETS = {
    "1. Computer fundamentals": """
COMPUTER SYSTEMS
• Hardware = physical parts; software = instructions/programs.
• CPU = Central Processing Unit. It processes instructions.
• ALU = Arithmetic Logic Unit; performs arithmetic and logical operations.
• Control Unit (CU) directs and coordinates CPU operations.
• Registers are very small, very fast storage locations inside the CPU.
• Cache stores frequently needed data/instructions for quick access.
• RAM is volatile working memory: contents are lost when power is off.
• ROM is non-volatile memory: it retains stored instructions without power.

FETCH–DECODE–EXECUTE–STORE CYCLE
1. Fetch: CPU gets the next instruction from memory.
2. Decode: Control Unit interprets the instruction.
3. Execute: CPU/ALU performs the operation.
4. Store: result is written to a register or memory when needed.

MEMORY UNITS
• 1 bit = one binary digit (0 or 1).
• 1 nibble = 4 bits; 1 byte = 8 bits.
• 1 KB = 1,024 bytes; 1 MB = 1,024 KB; 1 GB = 1,024 MB
  (Use the convention specified by your question/workbook.)
""",
    "2. Number systems": """
BINARY AND DECIMAL
• Decimal (base 10) uses digits 0–9.
• Binary (base 2) uses only 0 and 1.
• Binary place values, from right to left: 1, 2, 4, 8, 16, 32, 64, ...

BINARY → DECIMAL
Multiply each bit by its place value, then add.
Example: 1011₂ = 8 + 0 + 2 + 1 = 11₁₀.

DECIMAL → BINARY
Repeatedly divide by 2 and record each remainder. Read remainders
from bottom to top. Alternatively, subtract powers of 2.

BINARY ADDITION
  0 + 0 = 0
  0 + 1 = 1
  1 + 0 = 1
  1 + 1 = 10  (write 0, carry 1)
  1 + 1 + 1 = 11 (write 1, carry 1)

ASCII
ASCII represents characters using numeric codes. A character such as
'A' has a numeric code; the code can be represented in binary.
Use the ASCII lookup tool in this app for common characters.
""",
    "3. Logic gates": """
LOGIC GATES
A logic gate takes binary inputs (0 or 1) and produces a binary output.

AND: output is 1 only when BOTH inputs are 1.
OR: output is 1 when AT LEAST ONE input is 1.
NOT: reverses the input (0 becomes 1; 1 becomes 0).
NAND: opposite of AND.
NOR: opposite of OR.
XOR: output is 1 when the inputs are DIFFERENT.

TRUTH TABLE
A truth table lists every possible input combination and its output.
For two inputs there are 2² = 4 combinations: 00, 01, 10, 11.
For n inputs there are 2ⁿ possible combinations.

BOOLEAN EXPRESSIONS
• AND is often written A · B or AB.
• OR is often written A + B.
• NOT is written A' or ¬A.
• XOR is often written A ⊕ B.

BOOLEAN IDENTITIES
• A + 0 = A          • A · 1 = A
• A + 1 = 1          • A · 0 = 0
• A + A = A          • A · A = A
• A + A' = 1         • A · A' = 0
• (A')' = A
• A + B = B + A      • AB = BA
• A(B + C) = AB + AC (distributive law)

DE MORGAN'S THEOREMS
• (A · B)' = A' + B'
• (A + B)' = A' · B'
Tip: the complement moves inside and AND/OR swaps.
""",
    "4. Programming languages": """
PROGRAMMING FOUNDATIONS
• Machine code: instructions represented in binary; hardware-specific.
• Assembly language: low-level symbolic instructions.
• High-level language: more human-readable (e.g. Python).
• Compiler: translates a program before execution (often into machine code).
• Interpreter: executes/translates instructions as a program runs.
• System software manages hardware/platform resources.
• Application software helps users perform tasks.

PYTHON / SPYDER
• Spyder is an environment for writing and running Python.
• A statement is an instruction executed by Python.
• Comments begin with # and are ignored by Python.
• Use meaningful variable names; names are case-sensitive.
• Indentation matters in Python blocks.
""",
    "5. Input, output and variables": """
OUTPUT: print()
print("Hello")
print(7)
print("Total:", 7)

INPUT: input()
name = input("Enter your name: ")
input() returns text (a string), even when the user types digits.

VARIABLES
score = 10
student_name = "Kai"
temperature = 26.5
is_ready = True

COMMON DATA TYPES
• int  = whole number, e.g. 12
• float = decimal number, e.g. 3.5
• str  = text, e.g. "hello"
• bool = True or False

TYPE CONVERSION (CASTING)
int("25")     → 25
float("2.5")  → 2.5
str(25)       → "25"
bool(1)       → True

IMPORTANT
age = int(input("Age: "))
Without int(), input is text. For example, "2" + "3" gives "23";
int("2") + int("3") gives 5.

F-STRINGS
name = "Kai"
score = 18
print(f"{name} scored {score}")

OPERATORS
Arithmetic: +  -  *  /  //  %  **
Relational/comparison: ==  !=  >  <  >=  <=
Logical: and  or  not
Assignment: =, +=, -=, *=, ...
""",
    "6. Expressions and precedence": """
OPERATOR PRECEDENCE (GENERAL PYTHON ORDER)
1. Parentheses: ( )
2. Exponentiation: **
3. Unary + and -
4. Multiplication, division, floor division, modulo: *, /, //, %
5. Addition and subtraction: +, -
6. Comparisons: ==, !=, <, >, <=, >=
7. not
8. and
9. or

Use parentheses when they make an expression clearer.
Examples:
• 2 + 3 * 4 = 14
• (2 + 3) * 4 = 20
• 10 // 3 = 3 (floor division)
• 10 % 3 = 1 (remainder)
• 2 ** 3 = 8
""",
    "7. Selection / conditionals": """
IF / ELIF / ELSE
if mark >= 80:
    print("A")
elif mark >= 50:
    print("Pass")
else:
    print("Try again")

• if checks a condition.
• elif checks another condition if earlier conditions were false.
• else runs when no earlier condition was true.
• A colon : begins a block; indentation defines the block.
• Use == to compare; = assigns a value.

NESTED IF
An if statement placed inside another if/else block.
Use it when a second check depends on the first check.

BOOLEAN CONDITIONS
• and: all conditions must be True.
• or: at least one condition must be True.
• not: reverses True/False.
""",
    "8. Iteration / loops": """
FOR LOOP
for i in range(5):
    print(i)
Prints 0, 1, 2, 3, 4.

range(stop) starts at 0 and stops BEFORE stop.
range(start, stop) includes start, excludes stop.
range(start, stop, step) changes by step each time.

WHILE LOOP
count = 0
while count < 5:
    print(count)
    count += 1

A while loop repeats while its condition is True.
Make sure the condition can eventually become False.

COUNTER AND ACCUMULATOR
counter = 0       # counts occurrences
total = 0         # accumulates a running total
total += number

break: exits the loop immediately.
continue: skips to the next iteration.
""",
    "9. Flowcharts": """
COMMON FLOWCHART SYMBOLS
• Terminator (oval): Start / End.
• Process (rectangle): calculation or instruction.
• Input / Output (parallelogram): read or display data.
• Decision (diamond): condition with branches such as Yes/No.
• Flowline (arrow): direction of the process.

FLOWCHART TIPS
• Usually one Start and one or more End points.
• Label decision branches (e.g. Yes / No).
• Keep the flow moving clearly from top to bottom.
• A process box contains an action; a decision diamond contains a question.
• The flowchart workspace in this app lets you add and arrange basic shapes.
""",
    "10. Software development": """
SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)
A structured process for developing and maintaining software.
Common stages:
1. Planning / problem definition
2. Requirements analysis
3. Design (e.g. algorithms, pseudocode, flowcharts)
4. Implementation / coding
5. Testing and debugging
6. Deployment
7. Maintenance

REQUIREMENTS
• Functional requirements: what the system must do.
• Non-functional requirements: qualities/constraints (e.g. performance).
• SRS = Software Requirements Specification; records requirements.

WATERFALL VS AGILE
• Waterfall: phases are generally completed in sequence.
• Agile: iterative/incremental development; feedback and adaptation are frequent.

PROGRAMMING APPROACH
• Structured programming uses clear sequence, selection and iteration.
• Pseudocode describes an algorithm in plain, language-independent steps.
""",
    "11. Errors, testing and debugging": """
ERROR TYPES
• Syntax error: code breaks Python's grammar/rules.
• Runtime error: occurs while the program is running.
• Logic error: program runs but produces an incorrect result.

DEBUGGING
Finding and correcting errors. Read error messages and inspect the
relevant line, variable values, conditions and program flow.

TESTING
• Normal/typical data: ordinary valid input.
• Boundary data: values at the edges of allowed ranges.
• Invalid/abnormal data: values that should be rejected or handled.
• Verification: checking whether the product meets its specification.
• Test cases should include expected results so actual results can be compared.
"""
}

PYTHON_SNIPPETS = {
    "print() — output": 'print("Hello, world!")\nprint("Total:", 15)',
    "input() — get text": 'name = input("Enter your name: ")\nprint("Hello", name)',
    "int() — convert to whole number": 'age = int(input("Enter your age: "))\nprint(age + 1)',
    "float() — convert to decimal": 'price = float(input("Enter price: "))\nprint(price)',
    "str() — convert to text": 'score = 95\nmessage = "Score: " + str(score)\nprint(message)',
    "if / else": 'number = int(input("Number: "))\nif number % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")',
    "for loop": 'for count in range(1, 6):\n    print(count)',
    "while loop": 'count = 1\nwhile count <= 5:\n    print(count)\n    count += 1',
    "counter / total": 'total = 0\nfor i in range(3):\n    number = int(input("Number: "))\n    total += number\nprint("Total:", total)',
    "Boolean operators": 'if age >= 13 and age <= 17:\n    print("Teen range")',
    "f-string": 'name = "Alex"\nscore = 88\nprint(f"{name} scored {score}")',
    "comment": '# This is a comment\n# Python ignores this line'
}


# ----------------------------- Small UI helpers ------------------------------

class ScrollableFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.inner = ttk.Frame(self.canvas, padding=12)
        self.window = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.inner.bind("<Configure>", self._update_scroll)
        self.canvas.bind("<Configure>", self._resize_inner)

    def _update_scroll(self, _event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _resize_inner(self, event):
        self.canvas.itemconfigure(self.window, width=event.width)


class CheatSheetApp:
    def __init__(self, root):
        self.root = root
        root.title("PFP Digital Logic & Programming — Interactive Cheat Sheet")
        root.geometry("1120x760")
        root.minsize(850, 600)
        self.style = ttk.Style()
        try:
            self.style.theme_use("clam")
        except tk.TclError:
            pass
        self.style.configure("Title.TLabel", font=("Segoe UI", 19, "bold"))
        self.style.configure("Section.TLabel", font=("Segoe UI", 12, "bold"))
        self.style.configure("Hint.TLabel", foreground="#555555")
        self._build_header()
        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        self._build_home_tab()
        self._build_logic_tab()
        self._build_number_tab()
        self._build_reference_tab()
        self._build_notepad_tab()
        self._build_flowchart_tab()

    def _build_header(self):
        header = ttk.Frame(self.root, padding=(16, 12))
        header.pack(fill="x")
        ttk.Label(header, text="DIGITAL LOGIC & PROGRAMMING", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header, text="Interactive PFP workbook companion • Topics 1–4 • Labs 1–13",
                  style="Hint.TLabel").pack(anchor="w", pady=(2, 0))

    def _new_tab(self, title):
        frame = ttk.Frame(self.tabs)
        self.tabs.add(frame, text=title)
        return frame

    def _build_home_tab(self):
        tab = self._new_tab("Start here")
        body = ScrollableFrame(tab)
        body.pack(fill="both", expand=True)
        f = body.inner
        ttk.Label(f, text="Your all-in-one revision desk", style="Title.TLabel").pack(anchor="w", pady=(0, 8))
        ttk.Label(f, text=(
            "Use the tabs to revise concepts, test logic gates, convert numbers, "
            "look up Python syntax, draft code and sketch flowcharts."
        ), wraplength=950).pack(anchor="w", pady=(0, 14))
        cards = [
            ("DIGITAL LOGIC", "Binary and decimal • Boolean algebra • AND, OR, NOT, NAND, NOR, XOR"),
            ("PYTHON BASICS", "print() • input() • variables • int() • float() • str() • operators"),
            ("CONTROL STRUCTURES", "if / elif / else • for • while • range() • break • continue"),
            ("SOFTWARE DEVELOPMENT", "SDLC • Waterfall • Agile • requirements • testing • debugging"),
        ]
        for title, desc in cards:
            box = ttk.LabelFrame(f, text=title, padding=12)
            box.pack(fill="x", pady=5)
            ttk.Label(box, text=desc, wraplength=930).pack(anchor="w")
        ttk.Label(f, text="Quick study tip", style="Section.TLabel").pack(anchor="w", pady=(14, 4))
        ttk.Label(f, text=(
            "Try to explain each idea without looking, then use the calculators to check "
            "your understanding. For code, pay special attention to data types, conditions "
            "and indentation."
        ), wraplength=950).pack(anchor="w")
        ttk.Label(f, text=(
            "This is a revision companion, not a replacement for your teacher's instructions. "
            "If a question specifies a particular convention (especially memory units), follow it."
        ), style="Hint.TLabel", wraplength=950).pack(anchor="w", pady=(14, 0))

    # ------------------------------ Logic gates -------------------------------

    def _build_logic_tab(self):
        tab = self._new_tab("Logic gate calculator")
        outer = ttk.Frame(tab, padding=16)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="Logic gate calculator", style="Title.TLabel").pack(anchor="w")
        ttk.Label(outer, text="Change the inputs and gate to calculate the output and view its truth table.",
                  style="Hint.TLabel").pack(anchor="w", pady=(2, 12))

        controls = ttk.LabelFrame(outer, text="Try a gate", padding=12)
        controls.pack(fill="x")
        self.gate_var = tk.StringVar(value="AND")
        self.a_var = tk.IntVar(value=1)
        self.b_var = tk.IntVar(value=1)
        row = ttk.Frame(controls)
        row.pack(anchor="w")
        ttk.Label(row, text="Input A:").pack(side="left")
        ttk.Radiobutton(row, text="0", variable=self.a_var, value=0, command=self._update_gate).pack(side="left", padx=4)
        ttk.Radiobutton(row, text="1", variable=self.a_var, value=1, command=self._update_gate).pack(side="left", padx=4)
        ttk.Label(row, text="Input B:").pack(side="left", padx=(18, 0))
        ttk.Radiobutton(row, text="0", variable=self.b_var, value=0, command=self._update_gate).pack(side="left", padx=4)
        ttk.Radiobutton(row, text="1", variable=self.b_var, value=1, command=self._update_gate).pack(side="left", padx=4)
        ttk.Label(row, text="Gate:").pack(side="left", padx=(18, 5))
        gate_box = ttk.Combobox(row, textvariable=self.gate_var,
                                values=["AND", "OR", "NOT A", "NOT B", "NAND", "NOR", "XOR"],
                                state="readonly", width=12)
        gate_box.pack(side="left")
        gate_box.bind("<<ComboboxSelected>>", lambda _e: self._update_gate())

        self.gate_result = ttk.Label(controls, text="Output = 1", font=("Segoe UI", 16, "bold"))
        self.gate_result.pack(anchor="w", pady=(12, 0))
        self.gate_explain = ttk.Label(controls, text="", wraplength=900)
        self.gate_explain.pack(anchor="w", pady=(4, 0))

        tablebox = ttk.LabelFrame(outer, text="Truth table for selected gate", padding=10)
        tablebox.pack(fill="both", expand=True, pady=14)
        self.truth_tree = ttk.Treeview(tablebox, columns=("A", "B", "Output"), show="headings", height=5)
        for col in ("A", "B", "Output"):
            self.truth_tree.heading(col, text=col)
            self.truth_tree.column(col, width=120, anchor="center")
        self.truth_tree.pack(anchor="w")
        self._update_gate()

    def _gate_value(self, gate, a, b):
        return {
            "AND": a & b,
            "OR": a | b,
            "NOT A": 1 - a,
            "NOT B": 1 - b,
            "NAND": 1 - (a & b),
            "NOR": 1 - (a | b),
            "XOR": int(a != b),
        }[gate]

    def _update_gate(self):
        gate, a, b = self.gate_var.get(), self.a_var.get(), self.b_var.get()
        out = self._gate_value(gate, a, b)
        self.gate_result.config(text=f"Output = {out}")
        descriptions = {
            "AND": "AND is 1 only if both inputs are 1.",
            "OR": "OR is 1 if at least one input is 1.",
            "NOT A": "NOT reverses input A.",
            "NOT B": "NOT reverses input B.",
            "NAND": "NAND is the opposite of AND.",
            "NOR": "NOR is the opposite of OR.",
            "XOR": "XOR is 1 when the two inputs are different.",
        }
        self.gate_explain.config(text=descriptions[gate])
        for item in self.truth_tree.get_children():
            self.truth_tree.delete(item)
        combos = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for x, y in combos:
            result = self._gate_value(gate, x, y)
            self.truth_tree.insert("", "end", values=(x, y, result))

    # ---------------------------- Number converter ---------------------------

    def _build_number_tab(self):
        tab = self._new_tab("Binary / decimal / ASCII")
        outer = ttk.Frame(tab, padding=16)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="Number systems toolkit", style="Title.TLabel").pack(anchor="w")
        ttk.Label(outer, text="Convert binary and decimal, add binary values, and inspect ASCII codes.",
                  style="Hint.TLabel").pack(anchor="w", pady=(2, 12))

        conv = ttk.LabelFrame(outer, text="Binary ↔ decimal converter", padding=12)
        conv.pack(fill="x", pady=5)
        self.number_entry = tk.StringVar()
        self.number_mode = tk.StringVar(value="Decimal to binary")
        r = ttk.Frame(conv)
        r.pack(fill="x")
        ttk.Entry(r, textvariable=self.number_entry, width=24).pack(side="left")
        ttk.Combobox(r, textvariable=self.number_mode,
                     values=["Decimal to binary", "Binary to decimal"], state="readonly",
                     width=22).pack(side="left", padx=8)
        ttk.Button(r, text="Convert", command=self._convert_number).pack(side="left")
        self.number_output = ttk.Label(conv, text="Result will appear here.", font=("Segoe UI", 12, "bold"))
        self.number_output.pack(anchor="w", pady=(10, 0))

        addbox = ttk.LabelFrame(outer, text="Binary addition", padding=12)
        addbox.pack(fill="x", pady=8)
        self.bin_a = tk.StringVar(value="1011")
        self.bin_b = tk.StringVar(value="0110")
        rr = ttk.Frame(addbox)
        rr.pack(anchor="w")
        ttk.Label(rr, text="First:").pack(side="left")
        ttk.Entry(rr, textvariable=self.bin_a, width=16).pack(side="left", padx=5)
        ttk.Label(rr, text="Second:").pack(side="left", padx=(12, 0))
        ttk.Entry(rr, textvariable=self.bin_b, width=16).pack(side="left", padx=5)
        ttk.Button(rr, text="Add", command=self._add_binary).pack(side="left", padx=8)
        self.bin_output = ttk.Label(addbox, text="Result will appear here.", font=("Segoe UI", 12, "bold"))
        self.bin_output.pack(anchor="w", pady=(8, 0))

        ascii_box = ttk.LabelFrame(outer, text="ASCII lookup", padding=12)
        ascii_box.pack(fill="x", pady=8)
        self.ascii_entry = tk.StringVar(value="A")
        ar = ttk.Frame(ascii_box)
        ar.pack(anchor="w")
        ttk.Label(ar, text="Enter one character:").pack(side="left")
        ttk.Entry(ar, textvariable=self.ascii_entry, width=8).pack(side="left", padx=6)
        ttk.Button(ar, text="Look up", command=self._ascii_lookup).pack(side="left")
        self.ascii_output = ttk.Label(ascii_box, text="Character code will appear here.")
        self.ascii_output.pack(anchor="w", pady=(8, 0))

    def _convert_number(self):
        raw = self.number_entry.get().strip()
        try:
            if self.number_mode.get() == "Decimal to binary":
                n = int(raw, 10)
                if n < 0:
                    raise ValueError
                result = f"{n}₁₀ = {bin(n)[2:]}₂"
            else:
                if not raw or any(ch not in "01" for ch in raw):
                    raise ValueError
                n = int(raw, 2)
                result = f"{raw}₂ = {n}₁₀"
            self.number_output.config(text=result)
        except ValueError:
            messagebox.showerror("Invalid input", "Enter a non-negative decimal integer or a binary number containing only 0 and 1.")

    def _add_binary(self):
        a, b = self.bin_a.get().strip(), self.bin_b.get().strip()
        try:
            if not a or not b or any(c not in "01" for c in a + b):
                raise ValueError
            total = int(a, 2) + int(b, 2)
            width = max(len(a), len(b))
            self.bin_output.config(text=f"{a}₂ + {b}₂ = {total:0{width}b}₂  (decimal {total})")
        except ValueError:
            messagebox.showerror("Invalid input", "Both values must contain only 0 and 1.")

    def _ascii_lookup(self):
        value = self.ascii_entry.get()
        if len(value) != 1:
            messagebox.showerror("One character needed", "Enter exactly one character.")
            return
        code = ord(value)
        self.ascii_output.config(text=f"{value!r}  →  decimal {code}  →  binary {code:08b}  (Unicode code point; ASCII covers 0–127)")

    # ------------------------------ Reference tab ----------------------------

    def _build_reference_tab(self):
        tab = self._new_tab("Full cheat sheet")
        left = ttk.Frame(tab, padding=(10, 10, 5, 10))
        left.pack(side="left", fill="y")
        right = ttk.Frame(tab, padding=(5, 10, 10, 10))
        right.pack(side="left", fill="both", expand=True)
        ttk.Label(left, text="Find a topic", style="Section.TLabel").pack(anchor="w")
        self.search_var = tk.StringVar()
        search = ttk.Entry(left, textvariable=self.search_var, width=25)
        search.pack(fill="x", pady=6)
        search.bind("<KeyRelease>", lambda _e: self._filter_topics())
        self.topic_list = tk.Listbox(left, width=29, height=25, exportselection=False)
        self.topic_list.pack(fill="y", expand=True)
        self.topic_list.bind("<<ListboxSelect>>", self._show_topic)
        self.topic_names = list(CHEAT_SHEETS.keys())
        self._fill_topic_list(self.topic_names)
        self.reference_text = tk.Text(right, wrap="word", font=("Consolas", 10), padx=12, pady=12)
        self.reference_text.pack(fill="both", expand=True)
        self.reference_text.insert("1.0", "Choose a topic on the left to view its notes.")
        self.reference_text.config(state="disabled")
        self.topic_list.selection_set(0)
        self._show_topic()

    def _fill_topic_list(self, names):
        self.topic_list.delete(0, "end")
        for name in names:
            self.topic_list.insert("end", name)

    def _filter_topics(self):
        query = self.search_var.get().lower()
        matches = [name for name in self.topic_names
                   if query in name.lower() or query in CHEAT_SHEETS[name].lower()]
        self._fill_topic_list(matches)

    def _show_topic(self, _event=None):
        selection = self.topic_list.curselection()
        if not selection:
            return
        name = self.topic_list.get(selection[0])
        self.reference_text.config(state="normal")
        self.reference_text.delete("1.0", "end")
        self.reference_text.insert("1.0", name.upper() + "\n" + "=" * len(name) + "\n\n" + CHEAT_SHEETS[name].strip())
        self.reference_text.config(state="disabled")

    # ------------------------------- Code pad ---------------------------------

    def _build_notepad_tab(self):
        tab = self._new_tab("Python notepad")
        outer = ttk.Frame(tab, padding=12)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="Python programming notepad", style="Title.TLabel").pack(anchor="w")
        ttk.Label(outer, text="Choose a template to insert, then edit your own notes or code. Save it as a .py file.",
                  style="Hint.TLabel").pack(anchor="w", pady=(2, 8))
        toolbar = ttk.Frame(outer)
        toolbar.pack(fill="x", pady=(0, 8))
        self.snippet_var = tk.StringVar(value="print() — output")
        ttk.Combobox(toolbar, textvariable=self.snippet_var, values=list(PYTHON_SNIPPETS.keys()),
                     state="readonly", width=31).pack(side="left")
        ttk.Button(toolbar, text="Insert example", command=self._insert_snippet).pack(side="left", padx=5)
        ttk.Button(toolbar, text="Open .py / .txt", command=self._open_code).pack(side="left", padx=5)
        ttk.Button(toolbar, text="Save", command=self._save_code).pack(side="left", padx=5)
        ttk.Button(toolbar, text="Clear", command=self._clear_code).pack(side="left", padx=5)
        self.code_text = tk.Text(outer, wrap="none", undo=True, font=("Consolas", 11),
                                 padx=10, pady=10)
        yscroll = ttk.Scrollbar(outer, orient="vertical", command=self.code_text.yview)
        xscroll = ttk.Scrollbar(outer, orient="horizontal", command=self.code_text.xview)
        self.code_text.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        self.code_text.pack(fill="both", expand=True, side="top")
        xscroll.pack(fill="x")
        yscroll.pack(side="right", fill="y")
        self.code_text.insert("1.0", '# My Python notes / program\n# Choose an example above to insert a template.\n\n')

    def _insert_snippet(self):
        snippet = PYTHON_SNIPPETS[self.snippet_var.get()]
        self.code_text.insert("insert", snippet + "\n\n")
        self.code_text.focus_set()

    def _open_code(self):
        path = filedialog.askopenfilename(filetypes=[("Python/text files", "*.py *.txt"), ("All files", "*.*")])
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            self.code_text.delete("1.0", "end")
            self.code_text.insert("1.0", content)
        except OSError as exc:
            messagebox.showerror("Open failed", str(exc))

    def _save_code(self):
        path = filedialog.asksaveasfilename(defaultextension=".py",
                    filetypes=[("Python files", "*.py"), ("Text files", "*.txt"), ("All files", "*.*")])
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(self.code_text.get("1.0", "end-1c"))
            messagebox.showinfo("Saved", f"Saved to:\n{path}")
        except OSError as exc:
            messagebox.showerror("Save failed", str(exc))

    def _clear_code(self):
        if messagebox.askyesno("Clear notepad", "Clear everything in the notepad? Save your work first if needed."):
            self.code_text.delete("1.0", "end")

    # ------------------------------ Flowchart pad -----------------------------

    def _build_flowchart_tab(self):
        tab = self._new_tab("Flowchart shapes")
        outer = ttk.Frame(tab, padding=12)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="Flowchart shape workspace", style="Title.TLabel").pack(anchor="w")
        ttk.Label(outer, text="Add a symbol, give it a label, then drag it to arrange your flowchart.",
                  style="Hint.TLabel").pack(anchor="w", pady=(2, 8))
        tools = ttk.Frame(outer)
        tools.pack(fill="x", pady=(0, 8))
        self.shape_var = tk.StringVar(value="Process")
        ttk.Label(tools, text="Shape:").pack(side="left")
        ttk.Combobox(tools, textvariable=self.shape_var,
                     values=["Start / End", "Process", "Input / Output", "Decision"],
                     state="readonly", width=18).pack(side="left", padx=5)
        ttk.Button(tools, text="Add shape", command=self._add_flow_shape).pack(side="left", padx=4)
        ttk.Button(tools, text="Connect selected", command=self._connect_shapes).pack(side="left", padx=4)
        ttk.Button(tools, text="Delete selected", command=self._delete_shape).pack(side="left", padx=4)
        ttk.Button(tools, text="Clear board", command=self._clear_board).pack(side="left", padx=4)
        ttk.Button(tools, text="Export as PostScript", command=self._export_flowchart).pack(side="left", padx=4)
        self.flow_canvas = tk.Canvas(outer, bg="white", height=480, highlightthickness=1,
                                     highlightbackground="#aaaaaa")
        self.flow_canvas.pack(fill="both", expand=True)
        self.flow_canvas.bind("<ButtonPress-1>", self._flow_press)
        self.flow_canvas.bind("<B1-Motion>", self._flow_drag)
        self.flow_canvas.bind("<ButtonRelease-1>", self._flow_release)
        self.flow_shapes = {}
        self.flow_counter = 0
        self.selected_shape = None
        self.drag_offset = (0, 0)
        self._flow_hint()

    def _flow_hint(self):
        self.flow_canvas.create_text(18, 18, anchor="nw",
            text="Tip: select a shape and drag it. To connect two shapes, select the first, then the second, then click Connect selected.",
            fill="#666666", width=850, tags=("hint",))

    def _add_flow_shape(self):
        kind = self.shape_var.get()
        default = {"Start / End": "Start", "Process": "Process", "Input / Output": "Input / Output",
                   "Decision": "Condition?"}[kind]
        label = simpledialog.askstring("Shape label", "Text inside the shape:", initialvalue=default, parent=self.root)
        if label is None:
            return
        self.flow_counter += 1
        x = 260 + (self.flow_counter % 3) * 30
        y = 110 + (self.flow_counter - 1) * 95
        tag = f"shape_{self.flow_counter}"
        self._draw_shape(kind, label, x, y, tag)

    def _draw_shape(self, kind, label, x, y, tag):
        w, h = 170, 58
        if kind == "Start / End":
            ids = [self.flow_canvas.create_oval(x-w/2, y-h/2, x+w/2, y+h/2,
                    outline="#244a73", width=2, fill="#e5f1ff", tags=(tag,))]
        elif kind == "Process":
            ids = [self.flow_canvas.create_rectangle(x-w/2, y-h/2, x+w/2, y+h/2,
                    outline="#315b45", width=2, fill="#e8f5e9", tags=(tag,))]
        elif kind == "Input / Output":
            ids = [self.flow_canvas.create_polygon(x-w/2+18, y-h/2, x+w/2, y-h/2,
                    x+w/2-18, y+h/2, x-w/2, y+h/2, outline="#76531c",
                    width=2, fill="#fff3d6", tags=(tag,))]
        else:
            ids = [self.flow_canvas.create_polygon(x, y-h/2, x+w/2, y,
                    x, y+h/2, x-w/2, y, outline="#744078",
                    width=2, fill="#f7eafa", tags=(tag,))]
        text_id = self.flow_canvas.create_text(x, y, text=label, width=w-24,
                    font=("Segoe UI", 10), tags=(tag,))
        ids.append(text_id)
        self.flow_shapes[tag] = {"kind": kind, "label": label, "x": x, "y": y, "ids": ids}
        self._select_shape(tag)

    def _select_shape(self, tag):
        self.selected_shape = tag
        for key, item in self.flow_shapes.items():
            outline = "#d12b2b" if key == tag else None
            for item_id in item["ids"]:
                if self.flow_canvas.type(item_id) in ("oval", "rectangle", "polygon"):
                    self.flow_canvas.itemconfigure(item_id, outline=outline or self._original_outline(item["kind"]))
        self.flow_canvas.tag_raise(tag)

    @staticmethod
    def _original_outline(kind):
        return {"Start / End": "#244a73", "Process": "#315b45",
                "Input / Output": "#76531c", "Decision": "#744078"}[kind]

    def _flow_press(self, event):
        current = self.flow_canvas.find_withtag("current")
        tags = self.flow_canvas.gettags(current[-1]) if current else ()
        shape_tag = next((t for t in tags if t.startswith("shape_")), None)
        if shape_tag:
            self._select_shape(shape_tag)
            x, y = self.flow_shapes[shape_tag]["x"], self.flow_shapes[shape_tag]["y"]
            self.drag_offset = (x - event.x, y - event.y)
        else:
            self.selected_shape = None

    def _flow_drag(self, event):
        if not self.selected_shape:
            return
        tag = self.selected_shape
        item = self.flow_shapes[tag]
        new_x = event.x + self.drag_offset[0]
        new_y = event.y + self.drag_offset[1]
        dx, dy = new_x - item["x"], new_y - item["y"]
        self.flow_canvas.move(tag, dx, dy)
        item["x"], item["y"] = new_x, new_y

    def _flow_release(self, _event):
        pass

    def _connect_shapes(self):
        selected = self.flow_canvas.find_withtag("selected_shape")
        # Selection is tracked explicitly; ask for the second shape via a two-click sequence.
        if not self.selected_shape:
            messagebox.showinfo("Connect", "Select the first shape, then select the second shape and click Connect selected.")
            return
        if not hasattr(self, "_connect_first") or self._connect_first is None:
            self._connect_first = self.selected_shape
            messagebox.showinfo("Connect", "First shape selected. Now click the second shape, then click Connect selected again.")
            return
        second = self.selected_shape
        first = self._connect_first
        self._connect_first = None
        if first == second:
            messagebox.showinfo("Connect", "Choose two different shapes.")
            return
        a, b = self.flow_shapes[first], self.flow_shapes[second]
        line = self.flow_canvas.create_line(a["x"], a["y"] + 30, b["x"], b["y"] - 30,
                                            arrow=tk.LAST, width=2, fill="#555555")
        self.flow_canvas.tag_lower(line)
        self.flow_canvas.addtag_withtag("connector", line)

    def _delete_shape(self):
        if not self.selected_shape:
            return
        tag = self.selected_shape
        for item_id in self.flow_shapes[tag]["ids"]:
            self.flow_canvas.delete(item_id)
        del self.flow_shapes[tag]
        self.selected_shape = None

    def _clear_board(self):
        if messagebox.askyesno("Clear board", "Remove all shapes and connectors?"):
            self.flow_canvas.delete("all")
            self.flow_shapes.clear()
            self.selected_shape = None
            self._connect_first = None
            self._flow_hint()

    def _export_flowchart(self):
        path = filedialog.asksaveasfilename(defaultextension=".ps",
                    filetypes=[("PostScript file", "*.ps")])
        if not path:
            return
        try:
            self.flow_canvas.postscript(file=path, colormode="color")
            messagebox.showinfo("Exported", f"Flowchart exported to:\n{path}\nYou can open the .ps file with a compatible viewer.")
        except tk.TclError as exc:
            messagebox.showerror("Export failed", str(exc))


def main():
    root = tk.Tk()
    app = CheatSheetApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
