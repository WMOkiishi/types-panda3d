import keyword
from typing import Final

# from `AtomicToken` in interrogate_interface.h
ATOMIC_TYPES: Final = {
    1: 'int',  2: 'float', 3: 'float',
    4: 'bool', 5: 'str',   6: 'None',
    7: 'str',  8: 'int',   9: 'None'
}

DISALLOWED_CHARS: Final = frozenset('!@#$%^&*()<>,.-=+~{}? ')
COMMENT_INDENTS: Final = frozenset('/* ')


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
    indentation: str | None = None
    for line in comment.splitlines():
        if frozenset(line) <= COMMENT_INDENTS:
            line = ''
        elif line.startswith('/*'):
            line = line[2:].removeprefix('* ')
        elif indentation is None:
            for i, char in enumerate(line):
                if char not in COMMENT_INDENTS:
                    indentation, line = line[:i], line[i:]
                    break
        elif indentation:
            line = line.removeprefix(indentation)
        line = line.removesuffix('*/')
        docstring_lines.append(line.rstrip())
    return '\n'.join(docstring_lines).strip().replace('\\', '\\\\')
