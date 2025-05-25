
# NFA to DFA Converter

This Python-based tool converts a **Non-deterministic Finite Automaton (NFA)** into a **Deterministic Finite Automaton (DFA)**. It features interactive user input, colorful and structured transition tables, and graphical visualization of the resulting DFA using DOT and `pydot`.

---

## 🔧 Features

- Interactive CLI-based NFA input system
- Dynamic construction of corresponding DFA
- Beautifully formatted transition tables using `pandas` and `tabulate`
- Automatic generation and display of DFA state diagrams (`dfa_graph.png`)
- Highlights final DFA states
- Graceful user experience with colors and prompts

---

## 📁 Repository

**GitHub:** [NFA to DFA and DFA to NFA Converter](https://github.com/daniyalismail/Nfa_to_Dfa_and_Dfa_to_Nfa_Coverter)

---

## 🖥️ Installation

Clone the repository and navigate to the `Theory of Computation` folder:

```bash
git clone https://github.com/daniyalismail/Nfa_to_Dfa_and_Dfa_to_Nfa_Coverter.git
cd Nfa_to_Dfa_and_Dfa_to_Nfa_Coverter/Converter_Script
```

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main script to launch the tool:

```bash
python NFA_to_DFA.py
```

Follow the prompts to:

- Input number of states and transitions
- Enter each state's transitions
- Define final NFA states

The program will output:

- NFA transition table
- DFA transition table
- Final states of the DFA
- A visual DFA graph saved as `dfa_graph.png` and automatically opened

---

## 💡 Example

### 🔢 Input

```text
No. of states: 2
No. of transitions per state: 2
Enter all symbols separated by space: a b

Enter name of state 1: A
From state A, on input 'a', go to: B
From state A, on input 'b', go to: A

Enter name of state 2: B
From state B, on input 'a', go to: A B
From state B, on input 'b', go to: B

Enter final states of NFA separated by space: B
```

### 📊 Output

```text
Final states of DFA: B, AB
Graph saved as dfa_graph.png
```

Transition tables are printed in a stylized format, and a DFA graph image is generated.

---

## 📁 File Structure

```
.
├── NFA_to_DFA.py        # Main script
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```

---

## 📷 DFA Visualization

A `.png` graph of the DFA is generated using `pydot` and DOT language. The graph highlights:
- Final states with double circles
- Dead states (if any) in gray
- Transitions with labeled arrows

---

## 🧠 Authors

- **M. Daniyal Ismail** (Roll No: 39)
- **Mazin Imran** (Roll No: 23)

Project developed as part of a Theory of Computation course.

---

## 🤝 Contributions

Pull requests and contributions are welcome! Please ensure your changes are well-documented and tested.

---

## 📝 License

This project is open-source and free to use for academic and learning purposes.
