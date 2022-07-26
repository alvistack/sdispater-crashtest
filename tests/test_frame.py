from __future__ import annotations

import inspect

from types import FrameType

from crashtest.frame import Frame
from tests.helpers import nested_exception
from tests.helpers import simple_exception


def test_frame() -> None:
    try:
        simple_exception()
    except ValueError as e:
        assert e.__traceback__ is not None
        frame_info = inspect.getinnerframes(e.__traceback__)[0]
        frame = Frame(frame_info)
        same_frame = Frame(frame_info)
        assert frame_info.frame == frame.frame

    assert frame.lineno == 11
    assert frame.filename == __file__
    assert frame.function == "test_frame"
    assert frame.line == "        simple_exception()\n"

    with open(__file__) as f:
        assert f.read() == frame.file_content

    assert repr(frame) == f"<Frame {__file__}, test_frame, 11>"

    try:
        nested_exception()
    except Exception as e:
        assert e.__traceback__ is not None
        frame_info = inspect.getinnerframes(e.__traceback__)[0]
        other_frame = Frame(frame_info)

    assert same_frame == frame
    assert other_frame != frame
    assert hash(same_frame) == hash(frame)
    assert hash(other_frame) != hash(frame)


def test_frame_with_no_context_should_return_empty_line() -> None:
    frame = Frame(
        inspect.FrameInfo(FrameType(), "filename.py", 123, "function", None, 3)
    )

    assert frame.line == ""
