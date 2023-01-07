import keyword
import string
from typing import Final

# from `AtomicToken` in interrogate_interface.h
ATOMIC_TYPES: Final = {
    1: 'int',  2: 'float', 3: 'float',
    4: 'bool', 5: 'str',   6: 'None',
    7: 'str',  8: 'int',   9: 'None'
}

ID_CHARS: Final = frozenset({'_', *string.ascii_letters, *string.digits})
COMMENT_INDENTS: Final = frozenset('/* ')


def make_alias_name(name: str, /, *, capitalize: bool = False) -> str:
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


def make_class_name(cpp_name: str) -> str:
    """Convert a C++ class name to a Python class name
    according to the default Interrogate rules.
    """
    # Based on classNameFromCppName from interfaceMakerPythonNative.cxx
    py_name_parts: list[str] = []
    underscore = False
    for char in cpp_name:
        if char not in ID_CHARS:
            underscore = True
            continue
        if underscore:
            py_name_parts.append('_')
            underscore = False
        py_name_parts.append(char)
    return check_keyword(''.join(py_name_parts))


def make_method_name(cpp_name: str) -> str:
    """Convert a C++ function/method name to a Python function/method name
    according to the default Interrogate rules.
    """
    # Based on methodNameFromCppName from interfaceMakerPythonNative.cxx
    py_name = ''.join(c if c in ID_CHARS else '_' for c in cpp_name)
    return check_keyword(py_name)


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
