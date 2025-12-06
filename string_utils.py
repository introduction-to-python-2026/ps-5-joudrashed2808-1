


def split_before_uppercases(formula):
    if not formula:
        return []

    if not any(c.isupper() for c in formula):
        return [formula]

    results = []
    current_chunk = formula[0]

    for i in range (1, len(formula)):
        char = formula[i]

        if char.isupper():
            results.append(current_chunk)
            current_chunk = char
        else:
            current_chunk += char

    
    results.append(current_chunk)
        
    return results

def split_at_digit(formula):
    prefix = ""
    number_start_index = -1

    for i, char in enumerate(formula):
        if char.isdigit():
            number_start_index = i
            break
        prefix += char

    if number_start_index == -1:
        return formula, 1   
    
    number_part = formula[number_start_index:]
    return prefix, int(number_part)

def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    
    element_chunks = split_before_uppercases(molecular_formula)
    
    for chunk in element_chunks:
        element, count = split_at_digit(chunk)
        
        atom_counts[element] = atom_counts.get(element, 0) + count
        
    return atom_counts


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
