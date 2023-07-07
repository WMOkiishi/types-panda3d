from collections.abc import Container, Iterable, MutableSequence, Sequence
from re import Pattern
from typing import overload
from typing_extensions import Final, Never

SECHEADER: Final[Pattern[str]]
JUNKHEADER: Final[Pattern[str]]
IMPORTSTAR: Final[Pattern[str]]
IDENTIFIER: Final[Pattern[str]]
FILEHEADER: Final[Pattern[str]]

def readFile(fn: str) -> str: ...
def writeFile(wfile: str, data: bytes) -> None: ...
def writeFileLines(wfile: str, lines: Iterable[bytes]) -> None: ...
def findFiles(dirlist: str | Iterable[str], ext: str, ign: Container[str], list: MutableSequence[str]) -> None: ...
def pathToModule(result: str) -> str: ...
def textToHTML(comment: str, sep: str, delsection: Pattern[str] | None = None) -> str: ...
def linkTo(link: str, text: str) -> str: ...
def convertToPythonFn(fn: str) -> str: ...
def removeFileLicense(content: str) -> str: ...

class InterrogateTokenizer:
    fn: str
    pos: int
    data: str
    def __init__(self, fn: str) -> None: ...
    def readint(self) -> int: ...
    def readstring(self) -> str: ...

def parseInterrogateIntVec(tokzr: InterrogateTokenizer) -> list[int]: ...

class InterrogateFunction:
    db: InterrogateDatabase
    index: int
    componentname: str
    flags: int
    classindex: int
    scopedname: str
    cwrappers: list[int]
    pythonwrappers: list[int]
    comment: str
    prototype: str
    def __init__(self, tokzr: InterrogateTokenizer, db: InterrogateDatabase) -> None: ...

class InterrogateEnumValue:
    name: str
    scopedname: str
    value: int
    def __init__(self, tokzr: InterrogateTokenizer) -> None: ...

class InterrogateDerivation:
    flags: int
    base: int
    upcast: int
    downcast: int
    def __init__(self, tokzr: InterrogateTokenizer) -> None: ...

class InterrogateType:
    db: InterrogateDatabase
    index: int
    componentname: str
    flags: int
    scopedname: str
    truename: str
    outerclass: int
    atomictype: int
    wrappedtype: int
    constructors: list[int]
    destructor: int
    elements: list[int]
    methods: list[int]
    casts: list[int]
    derivations: list[InterrogateDerivation]
    enumvalues: list[InterrogateEnumValue]
    nested: list[int]
    comment: str
    def __init__(self, tokzr: InterrogateTokenizer, db: InterrogateDatabase) -> None: ...

class InterrogateParameter:
    name: str
    parameterflags: int
    type: int
    def __init__(self, tokzr: InterrogateTokenizer) -> None: ...

class InterrogateWrapper:
    db: InterrogateDatabase
    index: int
    componentname: str
    flags: int
    function: int
    returntype: int
    returnvaluedestructor: int
    uniquename: str
    parameters: list[InterrogateParameter]
    def __init__(self, tokzr: InterrogateTokenizer, db: InterrogateDatabase) -> None: ...

class InterrogateDatabase:
    fn: str
    magic: int
    library: str
    libhash: str
    module: str
    functions: dict[int, InterrogateFunction]
    wrappers: dict[int, InterrogateWrapper]
    types: dict[int, InterrogateType]
    namedtypes: dict[str, InterrogateType]
    def __init__(self, tokzr: InterrogateTokenizer) -> None: ...

def printTree(tree, indent: int) -> None: ...

COMPOUND_STMT_PATTERN: Final[tuple]
DOCSTRING_STMT_PATTERN: Final[tuple]
DERIVATION_PATTERN: Final[tuple]
ASSIGNMENT_STMT_PATTERN: Final[tuple]

class ParseTreeInfo:
    docstring: str
    name: str
    file: str
    class_info: dict[str, ParseTreeInfo]
    function_info: dict[str, ParseTreeInfo]
    assign_info: dict
    derivs: dict
    prototype: str
    def __init__(self, tree, name: str, file) -> None: ...
    @overload
    def match(self, pattern: str | list[str], data: str, vars: dict | None = None) -> tuple[bool, dict]: ...
    @overload
    def match(self, pattern: tuple[str, ...], data: Sequence[str], vars: dict | None = None) -> tuple[bool, dict]: ...
    def extract_info(self, tree: Sequence[str]) -> None: ...
    def extract_derivs(self, classinfo: ParseTreeInfo, tree) -> None: ...
    def extract_tokens(self, str: str, tree) -> str: ...

class CodeDatabase:
    types: dict[str, InterrogateType | ParseTreeInfo]
    funcs: dict[str, InterrogateFunction | ParseTreeInfo]
    goodtypes: dict[str, InterrogateType]
    funcExports: dict[str, list[str]]
    typeExports: dict[str, list[str]]
    varExports: dict[str, list[str]]
    globalfn: list[str]
    formattedprotos: dict[str, str]
    def __init__(self, cxxlist: Iterable[str], pylist: Iterable[str]) -> None: ...
    def getClassList(self) -> list: ...
    def getGlobalFunctionList(self) -> list: ...
    def getClassComment(self, cn: str) -> str: ...
    def getClassParents(self, cn: str) -> list: ...
    def getClassConstants(self, cn: str) -> list: ...
    def buildInheritance(self, inheritance: MutableSequence[str], cn: str) -> None: ...
    def getInheritance(self, cn: str) -> list: ...
    def getClassImport(self, cn: str) -> str: ...
    def getClassConstructors(self, cn: str) -> list: ...
    def getClassMethods(self, cn: str) -> list: ...
    def getFunctionName(self, fn: str) -> str: ...
    def getFunctionImport(self, fn: str) -> str: ...
    def getFunctionPrototype(self, fn: str, urlprefix: str, urlsuffix: str) -> str: ...
    def getFunctionComment(self, fn: str) -> str: ...
    def isFunctionPython(self, fn: str) -> bool: ...
    def getFuncExports(self, mod: str) -> list[str]: ...
    def getTypeExports(self, mod: str) -> list[str]: ...
    def getVarExports(self, mod: str) -> list[str]: ...

CLASS_RENAME_DICT: dict[Never, Never]

def makeCodeDatabase(indirlist: str | Iterable[str], directdirlist: str | Iterable[str]) -> CodeDatabase: ...
def generateFunctionDocs(code: CodeDatabase, method: str, urlprefix: str, urlsuffix: str) -> str: ...
def generateLinkTable(link: Sequence[str], text, cols: int, urlprefix: str, urlsuffix: str) -> str: ...
def generate(
    pversion: str,
    indirlist: str | Iterable[str],
    directdirlist: str | Iterable[str],
    docdir: str,
    header: str,
    footer: str,
    urlprefix: str,
    urlsuffix: str,
) -> None: ...
def expandImports(
    indirlist: str | Iterable[str], directdirlist: str | Iterable[str], fixdirlist: str | Iterable[str]
) -> None: ...
