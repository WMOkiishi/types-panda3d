from _typeshed import StrOrBytesPath
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d.core._dtoolutil import istream, ostream

_TiXmlEncoding: TypeAlias = Literal[0, 1, 2]

class TiXmlBase:
    """TiXmlBase is a base class for every class in TinyXml.
    It does little except to establish that TinyXml classes
    can be printed and provide some utility functions.

    In XML, the document and elements can contain
    other elements and other types of nodes.

    @verbatim
    A Document can contain: Element (container or leaf)
                            Comment (leaf)
                            Unknown (leaf)
                            Declaration( leaf )

    An Element can contain: Element (container or leaf)
                            Text    (leaf)
                            Attributes (not on tree)
                            Comment (leaf)
                            Unknown (leaf)

    A Decleration contains: Attributes (not on tree)
    @endverbatim
    """

    TIXML_NO_ERROR: Final = 0
    TIXML_ERROR: Final = 1
    TIXML_ERROR_OPENING_FILE: Final = 2
    TIXML_ERROR_PARSING_ELEMENT: Final = 3
    TIXML_ERROR_FAILED_TO_READ_ELEMENT_NAME: Final = 4
    TIXML_ERROR_READING_ELEMENT_VALUE: Final = 5
    TIXML_ERROR_READING_ATTRIBUTES: Final = 6
    TIXML_ERROR_PARSING_EMPTY: Final = 7
    TIXML_ERROR_READING_END_TAG: Final = 8
    TIXML_ERROR_PARSING_UNKNOWN: Final = 9
    TIXML_ERROR_PARSING_COMMENT: Final = 10
    TIXML_ERROR_PARSING_DECLARATION: Final = 11
    TIXML_ERROR_DOCUMENT_EMPTY: Final = 12
    TIXML_ERROR_EMBEDDED_NULL: Final = 13
    TIXML_ERROR_PARSING_CDATA: Final = 14
    TIXML_ERROR_DOCUMENT_TOP_ONLY: Final = 15
    TIXML_ERROR_STRING_COUNT: Final = 16
    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def SetCondenseWhiteSpace(condense: bool) -> None:
        """The world does not agree on whether white space should be kept or
        not. In order to make everyone happy, these global, static functions
        are provided to set whether or not TinyXml will condense all white space
        into a single space or not. The default is to condense. Note changing this
        value is not thread safe.
        """
    @staticmethod
    def IsWhiteSpaceCondensed() -> bool:
        """Return the current white space setting."""
    def Row(self) -> int:
        """Return the position, in the original source file, of this node or attribute.
        The row and column are 1-based. (That is the first row and first column is
        1,1). If the returns values are 0 or less, then the parser does not have
        a row and column value.

        Generally, the row and column value will be set when the TiXmlDocument::Load(),
        TiXmlDocument::LoadFile(), or any TiXmlNode::Parse() is called. It will NOT be set
        when the DOM was created from operator>>.

        The values reflect the initial load. Once the DOM is modified programmatically
        (by adding or changing nodes and attributes) the new values will NOT update to
        reflect changes in the document.

        There is a minor performance cost to computing the row and column. Computation
        can be disabled if TiXmlDocument::SetTabSize() is called with 0 as the value.

        @sa TiXmlDocument::SetTabSize()
        """
    def Column(self) -> int:
        """< See Row()"""

class TiXmlNode(TiXmlBase):
    """The parent class for everything in the Document Object Model.
    (Except for attributes).
    Nodes have siblings, a parent, and children. A node can be
    in a document, or stand on its own. The type of a TiXmlNode
    can be queried, and it can be cast to its more defined type.
    """

    TINYXML_DOCUMENT: Final = 0
    TINYXMLDOCUMENT: Final = 0
    TINYXML_ELEMENT: Final = 1
    TINYXMLELEMENT: Final = 1
    TINYXML_COMMENT: Final = 2
    TINYXMLCOMMENT: Final = 2
    TINYXML_UNKNOWN: Final = 3
    TINYXMLUNKNOWN: Final = 3
    TINYXML_TEXT: Final = 4
    TINYXMLTEXT: Final = 4
    TINYXML_DECLARATION: Final = 5
    TINYXMLDECLARATION: Final = 5
    TINYXML_TYPECOUNT: Final = 6
    TINYXMLTYPECOUNT: Final = 6
    def Value(self) -> str:
        """The meaning of 'value' changes for the specific type of
        TiXmlNode.
        @verbatim
        Document:   filename of the xml file
        Element:    name of the element
        Comment:    the comment text
        Unknown:    the tag contents
        Text:       the text string
        @endverbatim

        The subclasses will wrap this function.
        """
    def ValueStr(self) -> str:
        """Return Value() as a std::string. If you only use STL,
        this is more efficient than calling Value().
        Only available in STL mode.
        """
    def ValueTStr(self) -> str: ...
    def SetValue(self, _value: str) -> None:
        """`(self, _value: str)`:
        Changes the value of the node. Defined as:
        @verbatim
        Document:   filename of the xml file
        Element:    name of the element
        Comment:    the comment text
        Unknown:    the tag contents
        Text:       the text string
        @endverbatim

        `(self, _value: str)`:
        STL std::string form.
        """
    def Clear(self) -> None:
        """Delete all the children of this node. Does not affect 'this'."""
    def Parent(self) -> TiXmlNode:
        """One step up the DOM."""
    @overload
    def FirstChild(self, _value: str = ...) -> TiXmlNode:
        """`(self)`; `(self)`:
        < The first child of this node. Will be null if there are no children.

        `(self, _value: str)`:
        < The first child of this node with the matching 'value'. Will be null if none found.
         The first child of this node with the matching 'value'. Will be null if none found.

        `(self, _value: str)`; `(self, _value: str)`:
        < STL std::string form.
        """
    @overload
    def FirstChild(self, value: str) -> TiXmlNode: ...
    @overload
    def LastChild(self, _value: str = ...) -> TiXmlNode:
        """`(self)`; `(self)`:
        The last child of this node. Will be null if there are no children.

        `(self, _value: str)`; `(self, value: str)`:
        The last child of this node matching 'value'. Will be null if there are no children.

        `(self, _value: str)`; `(self, _value: str)`:
        < STL std::string form.
        """
    @overload
    def LastChild(self, value: str) -> TiXmlNode: ...
    @overload
    def IterateChildren(self, previous: TiXmlNode) -> TiXmlNode:
        """`(self, previous: TiXmlNode)`:
        An alternate way to walk the children of a node.
        One way to iterate over nodes is:
        @verbatim
            for( child = parent->FirstChild(); child; child = child->NextSibling() )
        @endverbatim

        IterateChildren does the same thing with the syntax:
        @verbatim
            child = 0;
            while( child = parent->IterateChildren( child ) )
        @endverbatim

        IterateChildren takes the previous child as input and finds
        the next one. If the previous child is null, it returns the
        first. IterateChildren will return null when done.

        `(self, value: str, previous: TiXmlNode)`:
        This flavor of IterateChildren searches for children with a particular 'value'

        `(self, _value: str, previous: TiXmlNode)`; `(self, _value: str, previous: TiXmlNode)`:
        < STL std::string form.
        """
    @overload
    def IterateChildren(self, _value: str, previous: TiXmlNode) -> TiXmlNode: ...
    @overload
    def IterateChildren(self, value: str, previous: TiXmlNode) -> TiXmlNode: ...
    def InsertEndChild(self, addThis: TiXmlNode) -> TiXmlNode:
        """Add a new node related to this. Adds a child past the LastChild.
        Returns a pointer to the new object or NULL if an error occured.
        """
    def InsertBeforeChild(self, beforeThis: TiXmlNode, addThis: TiXmlNode) -> TiXmlNode:
        """Add a new node related to this. Adds a child before the specified child.
        Returns a pointer to the new object or NULL if an error occured.
        """
    def InsertAfterChild(self, afterThis: TiXmlNode, addThis: TiXmlNode) -> TiXmlNode:
        """Add a new node related to this. Adds a child after the specified child.
        Returns a pointer to the new object or NULL if an error occured.
        """
    def ReplaceChild(self, replaceThis: TiXmlNode, withThis: TiXmlNode) -> TiXmlNode:
        """Replace a child of this node.
        Returns a pointer to the new object or NULL if an error occured.
        """
    def RemoveChild(self, removeThis: TiXmlNode) -> bool:
        """Delete a child of this node."""
    @overload
    def PreviousSibling(self, _prev: str = ...) -> TiXmlNode:
        """`(self)`; `(self, __param0: str)`:
        Navigate to a sibling node.

        `(self, _value: str)`; `(self, _value: str)`:
        < STL std::string form.
        """
    @overload
    def PreviousSibling(self, _value: str) -> TiXmlNode: ...
    @overload
    def NextSibling(self, _next: str = ...) -> TiXmlNode:
        """`(self)`:
        Navigate to a sibling node.

        `(self, __param0: str)`:
        Navigate to a sibling node with the given 'value'.

        `(self, _value: str)`; `(self, _value: str)`:
        < STL std::string form.
        """
    @overload
    def NextSibling(self, _value: str) -> TiXmlNode: ...
    @overload
    def NextSiblingElement(self, _next: str = ...) -> TiXmlElement:
        """`(self)`; `(self, __param0: str)`:
        Convenience function to get through elements.
        Calls NextSibling and ToElement. Will skip all non-Element
        nodes. Returns 0 if there is not another element.

        `(self, _value: str)`; `(self, _value: str)`:
        < STL std::string form.
        """
    @overload
    def NextSiblingElement(self, _value: str) -> TiXmlElement: ...
    def FirstChildElement(self, _value: str = ...) -> TiXmlElement:
        """`(self)`; `(self, _value: str)`:
        Convenience function to get through elements.

        `(self, _value: str)`; `(self, _value: str)`:
        < STL std::string form.
        """
    def Type(self) -> int:
        """Query the type (as an enumerated value, above) of this node.
        The possible types are: DOCUMENT, ELEMENT, COMMENT,
                                UNKNOWN, TEXT, and DECLARATION.
        """
    def GetDocument(self) -> TiXmlDocument:
        """Return a pointer to the Document this node lives in.
        Returns null if not in a document.
        """
    def NoChildren(self) -> bool:
        """Returns true if this node has no children."""
    def ToDocument(self) -> TiXmlDocument:
        """< Cast to a more defined type. Will return null if not of the requested type."""
    def ToElement(self) -> TiXmlElement:
        """< Cast to a more defined type. Will return null if not of the requested type."""
    def ToComment(self) -> TiXmlComment:
        """< Cast to a more defined type. Will return null if not of the requested type."""
    def ToUnknown(self) -> TiXmlUnknown:
        """< Cast to a more defined type. Will return null if not of the requested type."""
    def ToText(self) -> TiXmlText:
        """< Cast to a more defined type. Will return null if not of the requested type."""
    def ToDeclaration(self) -> TiXmlDeclaration:
        """< Cast to a more defined type. Will return null if not of the requested type."""
    def Clone(self) -> TiXmlNode:
        """Create an exact duplicate of this node and return it. The memory must be deleted
        by the caller.
        """
    def Accept(self, visitor: TiXmlVisitor) -> bool:
        """Accept a hierchical visit the nodes in the TinyXML DOM. Every node in the
        XML tree will be conditionally visited and the host will be called back
        via the TiXmlVisitor interface.

        This is essentially a SAX interface for TinyXML. (Note however it doesn't re-parse
        the XML for the callbacks, so the performance of TinyXML is unchanged by using this
        interface versus any other.)

        The interface has been based on ideas from:

        - http://www.saxproject.org/
        - http://c2.com/cgi/wiki?HierarchicalVisitorPattern

        Which are both good references for "visiting".

        An example of using Accept():
        @verbatim
        TiXmlPrinter printer;
        tinyxmlDoc.Accept( &printer );
        const char* xmlcstr = printer.CStr();
        @endverbatim
        """

class TiXmlDeclaration(TiXmlNode):
    """In correct XML the declaration is the first entry in the file.
    @verbatim
        <?xml version="1.0" standalone="yes"?>
    @endverbatim

    TinyXml will happily read or write files without a declaration,
    however. There are 3 possible attributes to the declaration:
    version, encoding, and standalone.

    Note: In this version of the code, the attributes are
    handled as special cases, not generic attributes, simply
    because there can only be at most 3 and they are always the same.
    """

    @overload
    def __init__(self, copy: TiXmlDeclaration = ...) -> None:
        """`(self)`:
        Construct an empty declaration.

        `(self, _version: str, _encoding: str, _standalone: str)`:
        Construct.

        `(self, _version: str, _encoding: str, _standalone: str)`:
        Constructor.
        """
    @overload
    def __init__(self, _version: str, _encoding: str, _standalone: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def Version(self) -> str:
        """Version. Will return an empty string if none was found."""
    def Encoding(self) -> str:
        """Encoding. Will return an empty string if none was found."""
    def Standalone(self) -> str:
        """Is this a standalone document?"""

class TiXmlDocument(TiXmlNode):
    """Always the top level node. A document binds together all the
    XML pieces. It can be saved, loaded, and printed to the screen.
    The 'value' of a document node is the xml file name.
    """

    @overload
    def __init__(self, copy: TiXmlDocument = ...) -> None:
        """`(self)`:
        Create an empty document, that has no name.

        `(self, documentName: str)`:
        Create a document with a name. The name of the document is also the filename of the xml.

        `(self, documentName: str)`:
        Constructor.
        """
    @overload
    def __init__(self, documentName: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: TiXmlDocument | str) -> Self: ...
    @overload
    def LoadFile(self, encoding: _TiXmlEncoding = ...) -> bool:
        """`(self, encoding: _TiXmlEncoding = ...)`:
        Load a file using the current document value.
        Returns true if successful. Will delete any existing
        document data before loading.

        `(self, filename: str, encoding: _TiXmlEncoding = ...)`:
        Load a file using the given filename. Returns true if successful.

        `(self, filename: str, encoding: _TiXmlEncoding = ...)`:
        < STL std::string version.
        """
    @overload
    def LoadFile(self, filename: str, encoding: _TiXmlEncoding = ...) -> bool: ...
    def SaveFile(self, filename: str = ...) -> bool:
        """`(self)`:
        Save a file using the current document value. Returns true if successful.

        `(self, filename: str)`:
        Save a file using the given filename. Returns true if successful.

        `(self, filename: str)`:
        < STL std::string version.
        """
    def RootElement(self) -> TiXmlElement:
        """Get the root element -- the only top level element -- of the document.
        In well formed XML, there should only be one. TinyXml is tolerant of
        multiple elements at the document level.
        """
    def Error(self) -> bool:
        """If an error occurs, Error will be set to true. Also,
        - The ErrorId() will contain the integer identifier of the error (not generally useful)
        - The ErrorDesc() method will return the name of the error. (very useful)
        - The ErrorRow() and ErrorCol() will return the location of the error (if known)
        """
    def ErrorDesc(self) -> str:
        """Contains a textual (english) description of the error if one occurs."""
    def ErrorId(self) -> int:
        """Generally, you probably want the error string ( ErrorDesc() ). But if you
        prefer the ErrorId, this function will fetch it.
        """
    def ErrorRow(self) -> int:
        """Returns the location (if known) of the error. The first column is column 1,
        and the first row is row 1. A value of 0 means the row and column wasn't applicable
        (memory errors, for example, have no row/column) or the parser lost the error. (An
        error in the error reporting, in that case.)

        @sa SetTabSize, Row, Column
        """
    def ErrorCol(self) -> int:
        """< The column where the error occured. See ErrorRow()"""
    def SetTabSize(self, _tabsize: int) -> None:
        """SetTabSize() allows the error reporting functions (ErrorRow() and ErrorCol())
        to report the correct values for row and column. It does not change the output
        or input in any way.

        By calling this method, with a tab size
        greater than 0, the row and column of each node and attribute is stored
        when the file is loaded. Very useful for tracking the DOM back in to
        the source file.

        The tab size is required for calculating the location of nodes. If not
        set, the default of 4 is used. The tabsize is set per document. Setting
        the tabsize to 0 disables row/column tracking.

        Note that row and column tracking is not supported when using operator>>.

        The tab size needs to be enabled before the parse or load. Correct usage:
        @verbatim
        TiXmlDocument doc;
        doc.SetTabSize( 8 );
        doc.Load( "myfile.xml" );
        @endverbatim

        @sa Row, Column
        """
    def TabSize(self) -> int: ...
    def ClearError(self) -> None:
        """If you have handled the error, it can be reset with this call. The error
        state is automatically cleared if you Parse a new XML block.
        """
    def Print(self) -> None:
        """Write the document to standard out using formatted printing ("pretty print")."""

class TiXmlElement(TiXmlNode):
    """The element is a container class. It has a value, the element name,
    and can contain other elements, text, comments, and unknowns.
    Elements also contain an arbitrary number of attributes.
    """

    @overload
    def __init__(self, __param0: TiXmlElement) -> None:
        """`(self, in_value: str)`:
        Construct an element.

        `(self, _value: str)`:
        std::string constructor.
        """
    @overload
    def __init__(self, in_value: str) -> None: ...
    @overload
    def __init__(self, _value: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, base: TiXmlElement | str) -> Self: ...
    def Attribute(self, name: str) -> str:
        """Given an attribute name, Attribute() returns the value
        for the attribute of that name, or null if none exists.
        """
    @overload
    def SetAttribute(self, name: str, _value: int | str) -> None:
        """`(self, name: str, _value: str)`; `(self, name: str, value: int)`:
        Sets an attribute of name to a given value. The attribute
        will be created if it does not exist, or changed if it does.

        `(self, name: str, _value: int)`:
        < STL std::string form.

        `(self, name: str, _value: str)`:
        STL std::string form.
        """
    @overload
    def SetAttribute(self, name: str, value: int) -> None: ...
    def SetDoubleAttribute(self, name: str, value: float) -> None:
        """`(self, name: str, value: float)`:
        Sets an attribute of name to a given value. The attribute
        will be created if it does not exist, or changed if it does.

        `(self, name: str, value: float)`:
        < STL std::string form.
        """
    def RemoveAttribute(self, name: str) -> None:
        """`(self, name: str)`:
        Deletes an attribute with the given name.

        `(self, name: str)`:
        < STL std::string form.
        """
    def FirstAttribute(self) -> TiXmlAttribute:
        """< Access the first attribute in this element."""
    def LastAttribute(self) -> TiXmlAttribute:
        """< Access the last attribute in this element."""
    def GetText(self) -> str:
        """Convenience function for easy access to the text inside an element. Although easy
        and concise, GetText() is limited compared to getting the TiXmlText child
        and accessing it directly.

        If the first child of 'this' is a TiXmlText, the GetText()
        returns the character string of the Text node, else null is returned.

        This is a convenient method for getting the text of simple contained text:
        @verbatim
        <foo>This is text</foo>
        const char* str = fooElement->GetText();
        @endverbatim

        'str' will be a pointer to "This is text".

        Note that this function can be misleading. If the element foo was created from
        this XML:
        @verbatim
        <foo><b>This is text</b></foo>
        @endverbatim

        then the value of str would be null. The first child node isn't a text node, it is
        another element. From this XML:
        @verbatim
        <foo>This is <b>text</b></foo>
        @endverbatim
        GetText() will return "This is ".

        WARNING: GetText() accesses a child node - don't become confused with the
                 similarly named TiXmlHandle::Text() and TiXmlNode::ToText() which are
                 safe type casts on the referenced node.
        """

class TiXmlCursor:
    """Internal structure for tracking location of items
    in the XML file.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: TiXmlCursor) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...

class TiXmlVisitor:
    """Implements the interface to the "Visitor pattern" (see the Accept() method.)
    If you call the Accept() method, it requires being passed a TiXmlVisitor
    class to handle callbacks. For nodes that contain other nodes (Document, Element)
    you will get called with a VisitEnter/VisitExit pair. Nodes that are always leaves
    are simply called with Visit().

    If you return 'true' from a Visit method, recursive parsing will continue. If you return
    false, <b>no children of this node or its sibilings</b> will be Visited.

    All flavors of Visit methods have a default implementation that returns 'true' (continue
    visiting). You need to only override methods that are interesting to you.

    Generally Accept() is called on the TiXmlDocument, although all nodes suppert Visiting.

    You should never change the document from a callback.

    @sa TiXmlNode::Accept()
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: TiXmlVisitor = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @overload
    def VisitEnter(self, __param0: TiXmlDocument | str) -> bool:
        """`(self, __param0: TiXmlDocument)`:
        doc

        `(self, __param0: TiXmlElement, __param1: TiXmlAttribute)`:
        firstAttribute
        """
    @overload
    def VisitEnter(self, __param0: TiXmlElement | str, __param1: TiXmlAttribute) -> bool: ...
    def VisitExit(self, __param0: TiXmlDocument | TiXmlElement | str) -> bool:
        """`(self, __param0: TiXmlDocument)`:
        doc

        `(self, __param0: TiXmlElement)`:
        element
        """
    def Visit(self, __param0: TiXmlComment | TiXmlDeclaration | TiXmlText | TiXmlUnknown | str) -> bool:
        """`(self, __param0: TiXmlComment)`:
        comment

        `(self, __param0: TiXmlDeclaration)`:
        declaration

        `(self, __param0: TiXmlText)`:
        text

        `(self, __param0: TiXmlUnknown)`:
        unknown
        """

class TiXmlAttribute(TiXmlBase):
    """An attribute is a name-value pair. Elements have an arbitrary
    number of attributes, each with a unique name.

    @note The attributes are not TiXmlNodes, since they are not
          part of the tinyXML document object model. There are other
          suggested ways to look at this problem.
    """

    @overload
    def __init__(self) -> None:
        """`(self)`:
        Construct an empty attribute.

        `(self, _name: str, _value: str)`:
        Construct an attribute with a name and value.

        `(self, _name: str, _value: str)`:
        std::string constructor.
        """
    @overload
    def __init__(self, _name: str, _value: str) -> None: ...
    def __eq__(self, __rhs: object) -> bool: ...
    def __lt__(self, rhs: TiXmlAttribute) -> bool: ...
    def __gt__(self, rhs: TiXmlAttribute) -> bool: ...
    def Name(self) -> str:
        """< Return the name of this attribute."""
    def Value(self) -> str:
        """< Return the value of this attribute."""
    def ValueStr(self) -> str:
        """< Return the value of this attribute."""
    def IntValue(self) -> int:
        """< Return the value of this attribute, converted to an integer."""
    def DoubleValue(self) -> float:
        """< Return the value of this attribute, converted to a double."""
    def NameTStr(self) -> str:
        """Get the tinyxml string representation"""
    def SetName(self, _name: str) -> None:
        """`(self, _name: str)`:
        < Set the name of this attribute.

        `(self, _name: str)`:
        STL std::string form.
        """
    def SetValue(self, _value: str) -> None:
        """`(self, _value: str)`:
        < Set the value.

        `(self, _value: str)`:
        STL std::string form.
        """
    def SetIntValue(self, _value: int) -> None:
        """< Set the value from an integer."""
    def SetDoubleValue(self, _value: float) -> None:
        """< Set the value from a double."""
    def Next(self) -> TiXmlAttribute:
        """Get the next sibling attribute in the DOM. Returns null at end."""
    def Previous(self) -> TiXmlAttribute:
        """Get the previous sibling attribute in the DOM. Returns null at beginning."""
    def SetDocument(self, doc: TiXmlDocument | str) -> None:
        """[internal use]
        Set the document pointer so the attribute can report errors.
        """

class TiXmlAttributeSet:
    """A class used to manage a group of attributes.
    It is only used internally, both by the ELEMENT and the DECLARATION.

    The set can be changed transparent to the Element and Declaration
    classes that use it, but NOT transparent to the Attribute
    which has to implement a next() and previous() method. Which makes
    it a bit problematic and prevents the use of STL.

    This version is implemented with circular lists because:
        - I like circular lists
        - it demonstrates some independence from the (typical) doubly linked list.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    def Add(self, attribute: TiXmlAttribute) -> None: ...
    def Remove(self, attribute: TiXmlAttribute) -> None: ...
    def First(self) -> TiXmlAttribute: ...
    def Last(self) -> TiXmlAttribute: ...
    def Find(self, _name: str) -> TiXmlAttribute: ...
    def FindOrCreate(self, _name: str) -> TiXmlAttribute: ...

class TiXmlComment(TiXmlNode):
    """An XML comment."""

    @overload
    def __init__(self, __param0: TiXmlComment = ...) -> None:
        """`(self)`:
        Constructs an empty comment.

        `(self, _value: str)`:
        Construct a comment from text.
        """
    @overload
    def __init__(self, _value: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, base: TiXmlComment | str) -> Self: ...

class TiXmlText(TiXmlNode):
    """XML text. A text node can have 2 ways to output the next. "normal" output
    and CDATA. It will default to the mode it was parsed from the XML file and
    you generally want to leave it alone, but you can change the output mode with
    SetCDATA() and query it with CDATA().
    """

    @overload
    def __init__(self, copy: TiXmlText) -> None:
        """`(self, initValue: str)`:
        Constructor for text element. By default, it is treated as
        normal, encoded text. If you want it be output as a CDATA text
        element, set the parameter _cdata to 'true'

        `(self, initValue: str)`:
        Constructor.
        """
    @overload
    def __init__(self, initValue: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, base: TiXmlText | str) -> Self: ...
    def CDATA(self) -> bool:
        """Queries whether this represents text using a CDATA section."""
    def SetCDATA(self, _cdata: bool) -> None:
        """Turns on or off a CDATA representation of text."""

class TiXmlUnknown(TiXmlNode):
    """Any tag that tinyXml doesn't recognize is saved as an
    unknown. It is a tag of text, but should not be modified.
    It will be written back to the XML, unchanged, when the file
    is saved.

    DTD tags get thrown into TiXmlUnknowns.
    """

    def __init__(self, copy: TiXmlUnknown = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...

class TiXmlHandle:
    """A TiXmlHandle is a class that wraps a node pointer with null checks; this is
    an incredibly useful thing. Note that TiXmlHandle is not part of the TinyXml
    DOM structure. It is a separate utility class.

    Take an example:
    @verbatim
    <Document>
        <Element attributeA = "valueA">
            <Child attributeB = "value1" />
            <Child attributeB = "value2" />
        </Element>
    <Document>
    @endverbatim

    Assuming you want the value of "attributeB" in the 2nd "Child" element, it's very
    easy to write a *lot* of code that looks like:

    @verbatim
    TiXmlElement* root = document.FirstChildElement( "Document" );
    if ( root )
    {
        TiXmlElement* element = root->FirstChildElement( "Element" );
        if ( element )
        {
            TiXmlElement* child = element->FirstChildElement( "Child" );
            if ( child )
            {
                TiXmlElement* child2 = child->NextSiblingElement( "Child" );
                if ( child2 )
                {
                    // Finally do something useful.
    @endverbatim

    And that doesn't even cover "else" cases. TiXmlHandle addresses the verbosity
    of such code. A TiXmlHandle checks for null pointers so it is perfectly safe
    and correct to use:

    @verbatim
    TiXmlHandle docHandle( &document );
    TiXmlElement* child2 = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).Child( "Child", 1 ).ToElement();
    if ( child2 )
    {
        // do something useful
    @endverbatim

    Which is MUCH more concise and useful.

    It is also safe to copy handles - internally they are nothing more than node pointers.
    @verbatim
    TiXmlHandle handleCopy = handle;
    @endverbatim

    What they should not be used for is iteration:

    @verbatim
    int i=0;
    while ( true )
    {
        TiXmlElement* child = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).Child( "Child", i ).ToElement();
        if ( !child )
            break;
        // do something
        ++i;
    }
    @endverbatim

    It seems reasonable, but it is in fact two embedded while loops. The Child method is
    a linear walk to find the element, so this code would iterate much more than it needs
    to. Instead, prefer:

    @verbatim
    TiXmlElement* child = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).FirstChild( "Child" ).ToElement();

    for( child; child; child=child->NextSiblingElement() )
    {
        // do something
    }
    @endverbatim
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, ref: TiXmlHandle) -> None:
        """`(self, ref: TiXmlHandle)`:
        Copy constructor

        `(self, _node: TiXmlNode)`:
        Create a handle from any node (at any depth of the tree.) This can be a null pointer.
        """
    @overload
    def __init__(self, _node: TiXmlNode) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, ref: TiXmlHandle | TiXmlNode) -> Self: ...
    @overload
    def FirstChild(self, value: str = ...) -> TiXmlHandle:
        """`(self)`:
        Return a handle to the first child node.

        `(self, value: str)`:
        Return a handle to the first child node with the given name.
        """
    @overload
    def FirstChild(self, _value: str) -> TiXmlHandle: ...
    @overload
    def FirstChildElement(self, value: str = ...) -> TiXmlHandle:
        """`(self)`:
        Return a handle to the first child element.

        `(self, value: str)`:
        Return a handle to the first child element with the given name.
        """
    @overload
    def FirstChildElement(self, _value: str) -> TiXmlHandle: ...
    @overload
    def Child(self, index: int) -> TiXmlHandle:
        """`(self, value: str, index: int)`:
        Return a handle to the "index" child with the given name.
        The first child is 0, the second 1, etc.

        `(self, index: int)`:
        Return a handle to the "index" child.
        The first child is 0, the second 1, etc.
        """
    @overload
    def Child(self, value: str, index: int) -> TiXmlHandle: ...
    @overload
    def Child(self, _value: str, index: int) -> TiXmlHandle: ...
    @overload
    def ChildElement(self, index: int) -> TiXmlHandle:
        """`(self, value: str, index: int)`:
        Return a handle to the "index" child element with the given name.
        The first child element is 0, the second 1, etc. Note that only TiXmlElements
        are indexed: other types are not counted.

        `(self, index: int)`:
        Return a handle to the "index" child element.
        The first child element is 0, the second 1, etc. Note that only TiXmlElements
        are indexed: other types are not counted.
        """
    @overload
    def ChildElement(self, value: str, index: int) -> TiXmlHandle: ...
    @overload
    def ChildElement(self, _value: str, index: int) -> TiXmlHandle: ...
    def ToNode(self) -> TiXmlNode:
        """Return the handle as a TiXmlNode. This may return null."""
    def ToElement(self) -> TiXmlElement:
        """Return the handle as a TiXmlElement. This may return null."""
    def ToText(self) -> TiXmlText:
        """Return the handle as a TiXmlText. This may return null."""
    def ToUnknown(self) -> TiXmlUnknown:
        """Return the handle as a TiXmlUnknown. This may return null."""
    def Node(self) -> TiXmlNode:
        """@deprecated use ToNode.
        Return the handle as a TiXmlNode. This may return null.
        """
    def Element(self) -> TiXmlElement:
        """@deprecated use ToElement.
        Return the handle as a TiXmlElement. This may return null.
        """
    def Text(self) -> TiXmlText:
        """@deprecated use ToText()
        Return the handle as a TiXmlText. This may return null.
        """
    def Unknown(self) -> TiXmlUnknown:
        """@deprecated use ToUnknown()
        Return the handle as a TiXmlUnknown. This may return null.
        """

class TiXmlPrinter(TiXmlVisitor):
    """Print to memory functionality. The TiXmlPrinter is useful when you need to:

    -# Print to memory (especially in non-STL mode)
    -# Control formatting (line endings, etc.)

    When constructed, the TiXmlPrinter is in its default "pretty printing" mode.
    Before calling Accept() you can call methods to control the printing
    of the XML document. After TiXmlNode::Accept() is called, the printed document can
    be accessed via the CStr(), Str(), and Size() methods.

    TiXmlPrinter uses the Visitor API.
    @verbatim
    TiXmlPrinter printer;
    printer.SetIndent( "\\t" );

    doc.Accept( &printer );
    fprintf( stdout, "%s", printer.CStr() );
    @endverbatim
    """

    def __init__(self, __param0: TiXmlPrinter = ...) -> None: ...
    def SetIndent(self, _indent: str) -> None:
        """Set the indent characters for printing. By default 4 spaces
        but tab (\\t) is also useful, or null/empty string for no indentation.
        """
    def Indent(self) -> str:
        """Query the indention string."""
    def SetLineBreak(self, _lineBreak: str) -> None:
        """Set the line breaking string. By default set to newline (\\n).
        Some operating systems prefer other characters, or can be
        set to the null/empty string for no indenation.
        """
    def LineBreak(self) -> str:
        """Query the current line breaking string."""
    def SetStreamPrinting(self) -> None:
        """Switch over to "stream printing" which is the most dense formatting without
        linebreaks. Common when the XML is needed for network transmission.
        """
    def CStr(self) -> str:
        """Return the result."""
    def Size(self) -> int:
        """Return the length of the result string."""
    def Str(self) -> str:
        """Return the result."""

TIXML_ENCODING_UNKNOWN: Final = 0
TIXMLENCODINGUNKNOWN: Final = 0
TIXML_ENCODING_UTF8: Final = 1
TIXMLENCODINGUTF8: Final = 1
TIXML_ENCODING_LEGACY: Final = 2
TIXMLENCODINGLEGACY: Final = 2

def read_xml_stream(_in: istream) -> TiXmlDocument:
    """Reads an XML document from the indicated stream.
    @returns the document, or NULL on error.
    """

def write_xml_stream(out: ostream, doc: TiXmlDocument | str) -> None: ...
def print_xml(xnode: TiXmlNode) -> None: ...
def print_xml_to_file(filename: StrOrBytesPath, xnode: TiXmlNode) -> None: ...
def get_TIXML_MAJOR_VERSION() -> int: ...
def get_TIXML_MINOR_VERSION() -> int: ...
def get_TIXML_PATCH_VERSION() -> int: ...
def get_TIXML_DEFAULT_ENCODING() -> _TiXmlEncoding: ...

readXmlStream = read_xml_stream
writeXmlStream = write_xml_stream
printXml = print_xml
printXmlToFile = print_xml_to_file
getTIXMLMAJORVERSION = get_TIXML_MAJOR_VERSION
getTIXMLMINORVERSION = get_TIXML_MINOR_VERSION
getTIXMLPATCHVERSION = get_TIXML_PATCH_VERSION
getTIXMLDEFAULTENCODING = get_TIXML_DEFAULT_ENCODING
