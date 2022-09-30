import keyword
from typing import Final

# (mostly) from `methodRenameDictionary` in interfaceMakerPythonNative.cxx
METHOD_RENAMES: Final = {
    'operator ==': '__eq__',
    'operator !=': '__ne__',
    'operator <<': '__lshift__',
    'operator >>': '__rshift__',
    'operator <': '__lt__',
    'operator >': '__gt__',
    'operator <=': '__le__',
    'operator >=': '__ge__',
    'operator <=>': '__cmp__',
    'operator =': 'assign',
    'operator ()': '__call__',
    'operator []': '__getitem__',
    'operator [] =': '__setitem__',
    'operator ++unary': 'increment',
    'operator ++': 'increment',
    'operator --unary': 'decrement',
    'operator --': 'decrement',
    'operator ^': '__xor__',
    'operator %': '__mod__',
    'operator !': 'logicalNot',
    'operator ~unary': '__invert__',
    'operator &': '__and__',
    'operator &&': 'logicalAnd',
    'operator |': '__or__',
    'operator ||': 'logicalOr',
    'operator +': '__add__',
    'operator -': '__sub__',
    'operator -unary': '__neg__',
    'operator *': '__mul__',
    'operator /': '__truediv__',
    'operator +=': '__iadd__',
    'operator -=': '__isub__',
    'operator *=': '__imul__',
    'operator /=': '__itruediv__',
    'operator ,': 'concatenate',
    'operator |=': '__ior__',
    'operator &=': '__iand__',
    'operator ^=': '__ixor__',
    'operator ~=': 'bitwiseNotEqual',
    'operator ->': 'deference',
    'operator <<=': '__ilshift__',
    'operator >>=': '__irshift__',
    # 'operator typecast bool': '__bool__',
    # 'print': 'Cprint',
    'size': '__len__',
    '__nonzero__': '__bool__',
}

# from `AtomicToken` in interrogate_interface.h
ATOMIC_TYPES: Final = {
    1: 'int',  2: 'float', 3: 'float',
    4: 'bool', 5: 'str',   6: 'None',
    7: 'str',  8: 'int',   9: 'None'
}

DISALLOWED_CHARS: Final = frozenset('!@#$%^&*()<>,.-=+~{}? ')


def snake_to_camel(name: str, /, capitalize: bool = False) -> str:
    """Convert a string from snake to camel case."""
    return ''.join(
        s[:1].upper() + s[1:] if capitalize or i != 0 else s
        for i, s in enumerate(name.split('_'))
    )


def check_keyword(name: str, /) -> str:
    """Append an underscore to a string if it is a Python keyword.
    Otherwise, return it unchanged.
    """
    # Mimics checkKeyword from interfaceMakerPythonNative.cxx
    if keyword.iskeyword(name):
        name = '_' + name
    return name


def class_name_from_cpp_name(cpp_name: str, mangle: bool = False) -> str:
    """Convert a C++ class name to a Python class name
    according to the default Interrogate rules.
    """
    # Mimics classNameFromCppName from interfaceMakerPythonNative.cxx
    py_name_parts: list[str] = []
    next_cap = mangle
    underscore = False
    for char in cpp_name:
        if mangle and (char == '_' or char == ' '):
            next_cap = True
        elif char in DISALLOWED_CHARS:
            underscore = not mangle
        elif next_cap:
            py_name_parts.append(char.upper())
            next_cap = False
        elif underscore:
            py_name_parts.append('_' + char)
            underscore = False
        else:
            py_name_parts.append(char)
    return check_keyword(''.join(py_name_parts))


def method_name_from_cpp_name(cpp_name: str, mangle: bool = False) -> str:
    """Convert a C++ function/method name to a Python function/method name
    according to the default Interrogate rules.
    """
    # Mimics methodNameFromCppName from interfaceMakerPythonNative.cxx
    # cpp_name = cpp_name.removeprefix('__py__')  # This isn't actually necessary
    if py_name := METHOD_RENAMES.get(cpp_name):
        return py_name
    py_name_parts: list[str] = []
    next_cap = False
    for char in cpp_name:
        if mangle and (char == '_' or char == ' '):
            next_cap = True
        elif char in DISALLOWED_CHARS:
            if not mangle:
                py_name_parts.append('_')
        elif next_cap:
            py_name_parts.append(char.upper())
            next_cap = False
        else:
            py_name_parts.append(char)
    return check_keyword(''.join(py_name_parts))


def comment_to_docstring(comment: str) -> str:
    docstring_lines: list[str] = []
    comment = comment.strip('\n /*')
    if not comment:
        return ''
    for line in comment.splitlines():
        if line == ' *':
            docstring_lines.append('')
        else:
            docstring_lines.append(
                line.removeprefix(' * ').removeprefix('// ').rstrip())
    return '\n'.join(docstring_lines)
