def atomic_sentences(sentence):
    atoms = []
    for i in range(len(sentence)):
        if sentence[i].isalpha():
            atoms.append(sentence[i])
    return atoms

def is_atomic(sentence):
    if len(sentence) == 1 and sentence.isalpha():
        return True
    else:
        return False
        
def is_negation(sentence):
    if len(sentence) == 2 and sentence[0] == '~':
        return True
    else:
        return False
    
def is_conjunction(sentence): 
    if len(sentence) >= 3 and sentence[0] == '(' and sentence[-1] == ')':
        count = 0
        for i in range(len(sentence)):
            if sentence[i] == '(':
                count += 1
            elif sentence[i] == ')':
                count -= 1
            elif sentence[i] == '^' and count == 1:
                return True
        return False
    else:
        return False   
    
def is_disjunction(sentence):
    if len(sentence) >= 3 and sentence[0] == '(' and sentence[-1] == ')':
        count = 0
        for i in range(len(sentence)):
            if sentence[i] == '(':
                count += 1
            elif sentence[i] == ')':
                count -= 1
            elif sentence[i] == 'v' and count == 1:
                return True
        return False
    else:
        return False
    
def is_implication(sentence):
    if len(sentence) >= 3 and sentence[0] == '(' and sentence[-1] == ')':
        count = 0
        for i in range(len(sentence)):
            if sentence[i] == '(':
                count += 1
            elif sentence[i] == ')':
                count -= 1
            elif sentence[i] == '>' and count == 1:
                return True
        return False
    else:
        return False

def is_biconditional(sentence): 
    if len(sentence) >= 3 and sentence[0] == '(' and sentence[-1] == ')':
        count = 0
        for i in range(len(sentence)):
            if sentence[i] == '(':
                count += 1
            elif sentence[i] == ')':
                count -= 1
            elif sentence[i] == '<' and count == 1:
                return True
        return False
    else:
        return False
    
def is_wff(sentence):
    if is_atomic(sentence):
        return True
    elif is_negation(sentence):
        return is_wff(sentence[1:])
    elif is_conjunction(sentence):
        return is_wff(sentence[1:-1])
    elif is_disjunction(sentence):
        return is_wff(sentence[1:-1])
    elif is_implication(sentence):
        return is_wff(sentence[1:-1])
    elif is_biconditional(sentence):
        return is_wff(sentence[1:-1])
    else:
        return False
    
def truth_value_replacer(sentence,values):
    atoms = atomic_sentences(sentence)
    for i in range(len(atoms)):
        sentence = sentence.replace(atoms[i],str(values[i]))
    return sentence

def double_negation_eliminator(sentence):
    if is_negation(sentence):
        return double_negation_eliminator(sentence[1:])
    elif is_conjunction(sentence):
        return '(' + double_negation_eliminator(sentence[1:-1]) + ')'
    elif is_disjunction(sentence):
        return '(' + double_negation_eliminator(sentence[1:-1]) + ')'
    elif is_implication(sentence):
        return '(' + double_negation_eliminator(sentence[1:-1]) + ')'
    elif is_biconditional(sentence):
        return '(' + double_negation_eliminator(sentence[1:-1]) + ')'
    else:
        return sentence
    
def truth_value_flipper(sentence):
    if is_negation(sentence):
        if sentence[1] == '1':
            return '0'
        elif sentence[1] == '0':
            return '1'
    elif is_conjunction(sentence):
        return '(' + truth_value_flipper(sentence[1:-1]) + ')'
    elif is_disjunction(sentence):
        return '(' + truth_value_flipper(sentence[1:-1]) + ')'
    elif is_implication(sentence):
        return '(' + truth_value_flipper(sentence[1:-1]) + ')'
    elif is_biconditional(sentence):
        return '(' + truth_value_flipper(sentence[1:-1]) + ')'
    else:
        return sentence
    