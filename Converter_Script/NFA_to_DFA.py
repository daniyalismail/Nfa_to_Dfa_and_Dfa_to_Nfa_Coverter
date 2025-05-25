import pandas as pd
from tabulate import tabulate
import pydot
import os
import platform
from termcolor import colored

def print_centered(text, color=None):
    width = os.get_terminal_size().columns
    if color:
        text = colored(text, color)
    lines = text.splitlines()
    for line in lines:
        print(line.center(width))

def print_boxed(text, color='yellow'):
    width = os.get_terminal_size().columns
    box_width = width - 4
    print(colored('+' + '-' * box_width + '+', color))
    print(colored('|' + text.center(box_width) + '|', color))
    print(colored('+' + '-' * box_width + '+', color))

def open_image(filename):
    if platform.system() == "Windows":
        os.startfile(filename)
    elif platform.system() == "Darwin":
        os.system(f"open {filename}")
    else:
        os.system(f"xdg-open {filename}")

def draw_graph_dot(automaton, final_states, symbols, title="DFA Graph"):
    graph = pydot.Dot(graph_type='digraph', rankdir='LR', label=title, labelloc='t', fontsize="24", size="12,12")

    for state in automaton:
        shape = 'doublecircle' if state in final_states else 'circle'
        color = 'green' if state in final_states else 'lightblue'
        graph_node = pydot.Node(f'"{state}"', style="filled", fillcolor=color, shape=shape)
        graph.add_node(graph_node)

    start_state = list(automaton.keys())[0]
    graph.add_node(pydot.Node("START", shape="point"))
    graph.add_edge(pydot.Edge("START", f'"{start_state}"'))

    transition_map = {}
    dead_state_needed = False  # Flag to track missing transitions

    for from_state, transitions in automaton.items():
        for symbol in symbols:
            to_state = transitions.get(symbol, None)
            if not to_state:  # If no valid transition exists, route to dead state
                to_state = "DEAD"
                dead_state_needed = True
            elif isinstance(to_state, list):
                to_state = '"' + ",".join(sorted(to_state)) + '"'  # Fix DOT format
            else:
                to_state = f'"{to_state}"'  # Ensure valid DOT label

            key = (from_state, to_state)
            if key in transition_map:
                transition_map[key] += f", {symbol}"
            else:
                transition_map[key] = symbol

    for (from_state, to_state), label in transition_map.items():
        graph.add_edge(pydot.Edge(f'"{from_state}"', to_state, label=label))

    if dead_state_needed:  # If the DFA requires a dead state, add it
        graph.add_node(pydot.Node("DEAD", style="filled", fillcolor="gray", shape="circle"))
        for symbol in symbols:
            graph.add_edge(pydot.Edge("DEAD", "DEAD", label=symbol))

    try:
        graph.write_png('dfa_graph.png')
        print(f"\n{colored('Graph saved as dfa_graph.png', 'green')}")
        open_image('dfa_graph.png')
    except Exception as e:
        print(colored(f"Error generating graph: {str(e)}", 'red'))

def display_fancy_table(data, title):
    df = pd.DataFrame(data).fillna('∅')
    table = tabulate(df, headers='keys', tablefmt='grid', showindex=True, stralign='center', numalign='center')

    width = os.get_terminal_size().columns
    print("\n" + "=" * width)
    print_centered(title, 'cyan')
    print("=" * width)

    lines = table.splitlines()
    for line in lines:
        print(line.center(width))
    print("=" * width)

def nfa_to_dfa():
    nfa = {}
    n = int(input(colored("No. of states: ", 'yellow')))
    t = int(input(colored("No. of transitions per state: ", 'yellow')))
    symbols = input(colored("Enter all symbols separated by space: ", 'yellow')).split()

    for i in range(n):
        state = input(colored(f"Enter name of state {i + 1}: ", 'yellow'))
        nfa[state] = {}
        for symbol in symbols:
            next_states = input(colored(f"From state {state}, on input '{symbol}', go to: ", 'yellow')).split()
            nfa[state][symbol] = next_states

    display_fancy_table(nfa, "NFA Transition Table")

    nfa_final_states = input(colored("Enter final states of NFA separated by space: ", 'yellow')).split()

    dfa = {}
    keys_list = [list(nfa.keys())[0]]
    path_list = symbols
    new_states_list = []

    dfa[keys_list[0]] = {}
    for symbol in path_list:
        var = "".join(sorted(set(nfa[keys_list[0]].get(symbol, []))))
        dfa[keys_list[0]][symbol] = var
        if var and var not in keys_list:
            new_states_list.append(var)
            keys_list.append(var)

    while new_states_list:
        state = new_states_list.pop(0)
        dfa[state] = {}
        for symbol in path_list:
            temp = []
            for s in state:
                temp += nfa.get(s, {}).get(symbol, [])
            new_state = "".join(sorted(set(temp)))
            dfa[state][symbol] = new_state
            if new_state and new_state not in keys_list:
                new_states_list.append(new_state)
                keys_list.append(new_state)

    display_fancy_table(dfa, "DFA Transition Table")

    dfa_final_states = [state for state in dfa if any(fs in state for fs in nfa_final_states)]
    print(colored(f"\nFinal states of DFA: {', '.join(dfa_final_states)}", 'magenta'))

    draw_graph_dot(dfa, dfa_final_states, symbols, "DFA Graph")

def main():
    os.system('cls' if platform.system() == "Windows" else 'clear')

    print_boxed("NFA To DFA Converter", 'yellow')
    print_centered("By M.Daniyal Ismail (Roll No: 39) & Mazin Imran (Roll No: 23)", 'yellow')

    print("\n" * 2)
    print_centered("Welcome To Our Program", 'green')
    print("\n" * 2)

    while True:
        print_centered(colored("Choose Conversion Option:", 'blue'))
        print_centered(colored("1: NFA to DFA", 'cyan'))
        choice = input(colored("Enter your choice (1): ", 'yellow')).strip()

        print("\n")
        print_centered(colored("Thanks For The Selection! Let's Begin!", 'magenta'))
        print("\n")

        if choice == '1':
            nfa_to_dfa()
        else:
            print_centered(colored("Invalid choice. Please enter 1.", 'red'))
            continue

        cont = input(colored("\nDo you want to perform another conversion? (y/n): ", 'yellow')).lower()
        if cont != 'y':
            print("\n")
            print_boxed("Thanks! Hope You Enjoyed!!", 'green')
            print_boxed("Please Come Again!!", 'green')
            print_boxed("Program Terminated by the user", 'red')
            print("\n")
            break

if __name__ == "__main__":
    main()