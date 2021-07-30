# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2021, James R. Barlow (https://github.com/jbarlow83/)

# pybind11 does not generate type annotations yet, and mypy doesn't understand
# the way we're augmenting C++ classes with Python methods as in
# pikepdf/_methods.py. Thus, we need to manually spell out the resulting types
# after augmenting.

from abc import abstractmethod
from enum import Enum
from typing import (
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    Iterator,
    KeysView,
    List,
    Optional,
    Set,
    Tuple,
    TypeVar,
    Union,
    overload,
)

from pikepdf.models.encryption import EncryptionInfo, Permissions
from pikepdf.models.image import PdfInlineImage

T = TypeVar('T', bound='Object')

class Buffer: ...

# Exceptions

class PasswordError(Exception): ...
class PdfError(Exception): ...
class ForeignObjectError(Exception): ...

# Enums
class AccessMode(Enum):
    default: int = ...
    mmap: int = ...
    mmap_only: int = ...
    stream: int = ...

class EncryptionMethod(Enum):
    none: int = ...
    unknown: int = ...
    rc4: int = ...
    aes: int = ...
    aesv3: int = ...

class ObjectStreamMode(Enum):
    disable: int = ...
    generate: int = ...
    preserve: int = ...

class ObjectType(Enum):
    array: int = ...
    boolean: int = ...
    dictionary: int = ...
    inlineimage: int = ...
    integer: int = ...
    name: int = ...
    null: int = ...
    operator: int = ...
    real: int = ...
    reserved: int = ...
    stream: int = ...
    string: int = ...
    uninitialized: int = ...

class StreamDecodeLevel(Enum):
    all: int = ...
    generalized: int = ...
    none: int = ...
    specialized: int = ...

class TokenType(Enum):
    array_close: int = ...
    array_open: int = ...
    bad: int = ...
    bool: int = ...
    brace_close: int = ...
    brace_open: int = ...
    comment: int = ...
    dict_close: int = ...
    dict_open: int = ...
    eof: int = ...
    inline_image: int = ...
    integer: int = ...
    name: int = ...
    null: int = ...
    real: int = ...
    space: int = ...
    string: int = ...
    word: int = ...

# Object
class Object:
    def _ipython_key_completions_(self) -> Optional[KeysView]: ...
    def _inline_image_raw_bytes(self) -> bytes: ...
    def _parse_page_contents(self, callbacks: Callable) -> None: ...
    def _parse_page_contents_grouped(
        self, whitelist: str
    ) -> List[Tuple[Collection[Union[Object, PdfInlineImage]], 'Operator']]: ...
    def _parse_stream(self, *args, **kwargs) -> Any: ...
    def _parse_stream_grouped(self, *args, **kwargs) -> Any: ...
    def _repr_mimebundle_(self, include=None, exclude=None) -> Optional[Dict]: ...
    def _write(self, data: bytes, filter: Object, decode_parms: Object) -> None: ...
    def append(self, pyitem: Object) -> None: ...
    def as_dict(self) -> '_ObjectMapping': ...
    def as_list(self) -> '_ObjectList': ...
    def emplace(self, other: Object, retain: Iterable['Name'] = ...) -> None: ...
    def extend(self, arg0: Iterable[Object]) -> None: ...
    @overload
    def get(self, key: str, default: Object = ...) -> Object: ...
    @overload
    def get(self, key: Object, default: Object = ...) -> Object: ...
    def get_raw_stream_buffer(self) -> Buffer: ...
    def get_stream_buffer(self, decode_level: StreamDecodeLevel = ...) -> Buffer: ...
    def is_owned_by(self, possible_owner: 'Pdf') -> bool: ...
    def items(self) -> Iterable[Tuple[str, Object]]: ...
    def keys(self) -> Set[str]: ...
    def page_contents_add(self, contents: Object, prepend: bool = ...) -> None: ...
    def page_contents_coalesce(self) -> None: ...
    @staticmethod
    def parse(stream: bytes, description: str = ...) -> Object: ...
    def read_bytes(self, decode_level: StreamDecodeLevel = ...) -> bytes: ...
    def read_raw_bytes(self) -> bytes: ...
    def same_owner_as(self, other: Object) -> bool: ...
    def to_json(self, dereference: bool = ...) -> bytes: ...
    def unparse(self, resolved: bool = ...) -> bytes: ...
    def wrap_in_array(self) -> Object: ...
    def write(
        self,
        data: bytes,
        *,
        filter: Union['Name', 'Array', None] = ...,
        decode_parms: Union['Dictionary', 'Array', None] = ...,
        type_check: bool = ...,
    ) -> None: ...
    def __bytes__(self) -> bytes: ...
    @overload
    def __contains__(self, arg0: Object) -> bool: ...
    @overload
    def __contains__(self, arg0: str) -> bool: ...
    def __copy__(self) -> Object: ...
    def __delattr__(self, arg0: str) -> None: ...
    @overload
    def __delitem__(self, arg0: str) -> None: ...
    @overload
    def __delitem__(self, arg0: Object) -> None: ...
    @overload
    def __delitem__(self, arg0: int) -> None: ...
    def __dir__(self) -> list: ...
    def __eq__(self, other: Any) -> bool: ...
    def __getattr__(self, arg0: str) -> Object: ...
    @overload
    def __getitem__(self, arg0: str) -> Object: ...
    @overload
    def __getitem__(self, arg0: Object) -> Object: ...
    @overload
    def __getitem__(self, arg0: int) -> Object: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterable[Object]: ...
    def __len__(self) -> int: ...
    def __setattr__(self, arg0: str, arg1: object) -> None: ...
    @overload
    def __setitem__(self, arg0: str, arg1: Object) -> None: ...
    @overload
    def __setitem__(self, arg0: Object, arg1: Object) -> None: ...
    @overload
    def __setitem__(self, arg0: str, arg1: object) -> None: ...
    @overload
    def __setitem__(self, arg0: Object, arg1: object) -> None: ...
    @overload
    def __setitem__(self, arg0: int, arg1: Object) -> None: ...
    @overload
    def __setitem__(self, arg0: int, arg1: object) -> None: ...
    @property
    def _objgen(self) -> Tuple[int, int]: ...
    @property
    def _type_code(self) -> ObjectType: ...
    @property
    def _type_name(self) -> str: ...
    @property
    def images(self) -> '_ObjectMapping': ...
    @property
    def is_indirect(self) -> bool: ...
    @property
    def is_rectangle(self) -> bool: ...
    @property
    def objgen(self) -> Tuple[int, int]: ...
    @property
    def stream_dict(self) -> Object: ...
    @stream_dict.setter
    def stream_dict(self, val: Object) -> None: ...

class Name(Object): ...

class _ObjectList:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: _ObjectList) -> None: ...
    @overload
    def __init__(self, arg0: Iterable) -> None: ...
    @overload
    def __init__(*args, **kwargs) -> None: ...
    def append(self, x: Object) -> None: ...
    def clear(self) -> None: ...
    def count(self, x: Object) -> int: ...
    @overload
    def extend(self, L: _ObjectList) -> None: ...
    @overload
    def extend(self, L: Iterable[Object]) -> None: ...
    def insert(self, i: int, x: Object) -> None: ...
    @overload
    def pop(self) -> Object: ...
    @overload
    def pop(self, i: int) -> Object: ...
    @overload
    def pop(*args, **kwargs) -> Any: ...
    def remove(self, x: Object) -> None: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, x: Object) -> bool: ...
    @overload
    def __delitem__(self, arg0: int) -> None: ...
    @overload
    def __delitem__(self, arg0: slice) -> None: ...
    @overload
    def __delitem__(*args, **kwargs) -> Any: ...
    def __eq__(self, other: Any) -> bool: ...
    @overload
    def __getitem__(self, s: slice) -> _ObjectList: ...
    @overload
    def __getitem__(self, arg0: int) -> Object: ...
    @overload
    def __getitem__(*args, **kwargs) -> Any: ...
    def __iter__(self) -> Iterator[Object]: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: Any) -> bool: ...
    @overload
    def __setitem__(self, arg0: int, arg1: Object) -> None: ...
    @overload
    def __setitem__(self, arg0: slice, arg1: _ObjectList) -> None: ...
    @overload
    def __setitem__(*args, **kwargs) -> Any: ...

class _ObjectMapping:
    get: Any = ...
    keys: Any = ...
    values: Any = ...
    __contains__: Any = ...
    def __init__(self) -> None: ...
    def items(self) -> Iterator: ...
    def __bool__(self) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> Object: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: str, arg1: Object) -> None: ...

class Operator(Object): ...

class Annotation:
    def __init__(self, arg0: Object) -> None: ...
    def get_appearance_stream(self, which: Object, state: str = ...) -> Object: ...
    def get_page_content_for_appearance(
        self,
        name: Object,
        rotate: int,
        required_flags: int = ...,
        forbidden_flags: int = ...,
    ) -> str: ...
    @property
    def appearance_dict(self) -> Object: ...
    @property
    def appearance_state(self) -> str: ...
    @property
    def flags(self) -> int: ...
    @property
    def subtype(self) -> str: ...

class Token:
    def __init__(self, arg0: TokenType, arg1: bytes) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    @property
    def error_msg(self) -> str: ...
    @property
    def raw_value(self) -> bytes: ...
    @property
    def type_(self) -> TokenType: ...
    @property
    def value(self) -> str: ...

class _QPDFTokenFilter: ...

class TokenFilter(_QPDFTokenFilter):
    def __init__(self) -> None: ...
    def handle_token(self, token: Token = ...) -> Union[None, List, Token]: ...

class StreamParser:
    def __init__(self) -> None: ...
    @abstractmethod
    def handle_eof(self) -> None: ...
    @abstractmethod
    def handle_object(self, obj: Object) -> None: ...

class Page:
    _repr_mimebundle_: Any = ...
    def __init__(self, arg0: Object) -> None: ...
    def _get_cropbox(self, arg0: bool) -> Object: ...
    def _get_mediabox(self, arg0: bool) -> Object: ...
    def _get_trimbox(self, arg0: bool) -> Object: ...
    def add_content_token_filter(self, tf) -> None: ...
    def as_form_xobject(self, handle_transformations: bool = ...) -> Object: ...
    def contents_coalesce(self) -> None: ...
    def externalize_inline_images(self, min_size: int = ...) -> None: ...
    def get_filtered_contents(self, tf: TokenFilter) -> bytes: ...
    def parse_contents(self, arg0: StreamParser) -> None: ...
    def remove_unreferenced_resources(self) -> None: ...
    def rotate(self, angle: int, relative: bool) -> None: ...
    @property
    def _images(self) -> _ObjectMapping: ...
    @property
    def cropbox(self) -> 'Array': ...
    @cropbox.setter
    def cropbox(self, val: 'Array') -> None: ...
    @property
    def mediabox(self) -> 'Array': ...
    @mediabox.setter
    def mediabox(self, val: 'Array') -> None: ...
    @property
    def obj(self) -> Object: ...
    @property
    def trimbox(self) -> 'Array': ...
    @trimbox.setter
    def trimbox(self, val: 'Array') -> None: ...
    @property
    def resources(self) -> Object: ...
    def add_resource(
        res: Object,
        res_type: Name,
        name: Optional[Name] = None,
        *,
        prefix: str = '',
        replace_existing: bool = True,
    ) -> Name: ...

class PageList:
    def __init__(self, *args, **kwargs) -> None: ...
    def append(self, page: Object) -> None: ...
    @overload
    def extend(self, other: PageList) -> None: ...
    @overload
    def extend(self, iterable: Iterable[Object]) -> None: ...
    def insert(self, index: int, obj: Object) -> None: ...
    def p(self, pnum: int) -> Object: ...
    def remove(self, **kwargs) -> None: ...
    def reverse(self) -> None: ...
    @overload
    def __delitem__(self, arg0: int) -> None: ...
    @overload
    def __delitem__(self, arg0: slice) -> None: ...
    @overload
    def __getitem__(self, arg0: int) -> Object: ...
    @overload
    def __getitem__(self, arg0: slice) -> list: ...
    def __iter__(self) -> PageList: ...
    def __len__(self) -> int: ...
    def __next__(self) -> Object: ...
    @overload
    def __setitem__(self, arg0: int, arg1: Object) -> None: ...
    @overload
    def __setitem__(self, arg0: slice, arg1: Iterable[Object]) -> None: ...

class Pdf:
    _attach: Any = ...
    _repr_mimebundle_: Any = ...
    add_blank_page: Any = ...
    check: Any = ...
    close: Any = ...
    make_stream: Any = ...
    open: Any = ...
    open_metadata: Any = ...
    open_outline: Any = ...
    save: Any = ...
    __enter__: Any = ...
    __exit__: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _add_page(self, page: Object, first: bool = ...) -> None: ...
    def _add_page_at(self, arg0: Object, arg1: bool, arg2: Object) -> None: ...
    def _decode_all_streams_and_discard(self) -> None: ...
    def _get_object_id(self, arg0: int, arg1: int) -> Object: ...
    def _open(self, *args, **kwargs) -> Any: ...
    def _process(self, arg0: str, arg1: bytes) -> None: ...
    def _remove_page(self, arg0: Object) -> None: ...
    def _replace_object(self, arg0: Tuple[int, int], arg1: Object) -> None: ...
    def _save(
        self,
        filename: object,
        static_id: bool = ...,
        preserve_pdfa: bool = ...,
        min_version: object = ...,
        force_version: object = ...,
        fix_metadata_version: bool = ...,
        compress_streams: bool = ...,
        stream_decode_level: object = ...,
        object_stream_mode: ObjectStreamMode = ...,
        normalize_content: bool = ...,
        linearize: bool = ...,
        qdf: bool = ...,
        progress: object = ...,
        encryption: object = ...,
        samefile_check: bool = ...,
    ) -> None: ...
    def _swap_objects(self, arg0: Tuple[int, int], arg1: Tuple[int, int]) -> None: ...
    def check_linearization(self, stream: object = ...) -> bool: ...
    def copy_foreign(self, h: Object) -> Object: ...
    @overload
    def get_object(self, objgen: Tuple[int, int]) -> Object: ...
    @overload
    def get_object(self, objid: int, gen: int) -> Object: ...
    def get_warnings(self) -> list: ...
    @overload
    def make_indirect(self, h: T) -> T: ...
    @overload
    def make_indirect(self, obj: object) -> Object: ...
    @classmethod
    def new(cls) -> Pdf: ...
    def remove_unreferenced_resources(self) -> None: ...
    def show_xref_table(self) -> None: ...
    @property
    def Root(self) -> Object: ...
    @property
    def _allow_accessibility(self) -> bool: ...
    @property
    def _allow_extract(self) -> bool: ...
    @property
    def _allow_modify_all(self) -> bool: ...
    @property
    def _allow_modify_annotation(self) -> bool: ...
    @property
    def _allow_modify_assembly(self) -> bool: ...
    @property
    def _allow_modify_form(self) -> bool: ...
    @property
    def _allow_modify_other(self) -> bool: ...
    @property
    def _allow_print_highres(self) -> bool: ...
    @property
    def _allow_print_lowres(self) -> bool: ...
    @property
    def _encryption_data(self) -> dict: ...
    @property
    def _pages(self) -> Any: ...
    @property
    def allow(self) -> Permissions: ...
    @property
    def docinfo(self) -> Object: ...
    @docinfo.setter
    def docinfo(self, val: Object) -> None: ...
    @property
    def encryption(self) -> EncryptionInfo: ...
    @property
    def extension_level(self) -> int: ...
    @property
    def filename(self) -> str: ...
    @property
    def is_encrypted(self) -> bool: ...
    @property
    def is_linearized(self) -> bool: ...
    @property
    def objects(self) -> Any: ...
    @property
    def pages(self) -> PageList: ...
    @property
    def pdf_version(self) -> str: ...
    @property
    def root(self) -> Object: ...
    @property
    def trailer(self) -> Object: ...

class Rectangle:
    def __init__(self, llx: float, lly: float, urx: float, ury: float) -> None: ...
    @overload
    def __init__(self, Array) -> None: ...
    @property
    def llx(self) -> float: ...
    @llx.setter
    def llx(self, val: float): ...
    @property
    def lly(self) -> float: ...
    @lly.setter
    def lly(self, val: float): ...
    @property
    def urx(self) -> float: ...
    @urx.setter
    def urx(self, val: float): ...
    @property
    def ury(self) -> float: ...
    @ury.setter
    def ury(self, val: float): ...
    @property
    def width(self) -> float: ...
    @property
    def height(self) -> float: ...
    @property
    def lower_left(self) -> Tuple[float, float]: ...
    @property
    def lower_right(self) -> Tuple[float, float]: ...
    @property
    def upper_left(self) -> Tuple[float, float]: ...
    @property
    def upper_right(self) -> Tuple[float, float]: ...
    def as_array(self) -> 'Array': ...

def _new_operator(op: str) -> Object: ...
def _Null() -> Any: ...
def _encode(handle: Any) -> Object: ...
def _new_array(arg0: Iterable) -> Object: ...
def _new_boolean(arg0: bool) -> Object: ...
def _new_dictionary(arg0: dict) -> Object: ...
def _new_integer(arg0: int) -> Object: ...
def _new_name(arg0: str) -> Object: ...
@overload
def _new_real(arg0: str) -> Object: ...
@overload
def _new_real(value: float, places: int = ...) -> Object: ...
@overload
def _new_real(*args, **kwargs) -> Any: ...
def _new_stream(arg0: Pdf, arg1: bytes) -> Object: ...
def _new_string(s: Union[str, bytes]) -> Object: ...
def _new_string_utf8(s: str) -> Object: ...
def _test_file_not_found(*args, **kwargs) -> Any: ...
def get_decimal_precision() -> int: ...
def pdf_doc_to_utf8(pdfdoc: bytes) -> str: ...
def qpdf_version() -> str: ...
def set_access_default_mmap(mmap: bool) -> bool: ...
def set_decimal_precision(prec: int) -> int: ...
def unparse(obj: Any) -> bytes: ...
def utf8_to_pdf_doc(utf8: str, unknown: bytes) -> Tuple[bool, bytes]: ...
