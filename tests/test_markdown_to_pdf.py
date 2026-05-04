import pytest

from markdown_to_pdf import markdown_to_pdf


def test_returns_bytes():
    assert isinstance(markdown_to_pdf("# Hello"), bytes)


def test_output_has_pdf_magic_header():
    assert markdown_to_pdf("# Hello").startswith(b"%PDF-")


@pytest.mark.parametrize(
    "source",
    [
        "",
        "# Heading",
        "- item 1\n- item 2",
        "**bold** and *italic*",
        "[link](https://example.com)",
        "```\ncode block\n```",
    ],
)
def test_renders_various_markdown_to_valid_pdf(source):
    assert markdown_to_pdf(source).startswith(b"%PDF-")


def test_longer_input_produces_larger_pdf():
    small = markdown_to_pdf("a")
    big = markdown_to_pdf("lorem ipsum " * 500)
    assert len(big) > len(small)
