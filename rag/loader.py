"""Utilities for loading external documents for retrieval augmented generation."""

from pathlib import Path
import json

from pdfminer.high_level import extract_text
from docx import Document


def load_documents(path: str) -> list[str]:
    """Return a list of text documents contained in *path*.

    The loader supports plain text files, PDF documents and DOCX files. Unknown
    file types are ignored silently.
    """
    docs: list[str] = []
    if not path:
        return docs
    p = Path(path)
    if p.is_file():
        paths = [p]
    else:
        paths = list(p.rglob("*"))

    for file in paths:
        suffix = file.suffix.lower()
        try:
            if suffix == ".txt":
                docs.append(file.read_text(encoding="utf-8"))
            elif suffix == ".pdf":
                docs.append(extract_text(str(file)))
            elif suffix in {".docx", ".doc"}:
                doc = Document(str(file))
                docs.append("\n".join(p.text for p in doc.paragraphs))
            elif suffix == ".json":
                docs.append(json.loads(file.read_text(encoding="utf-8")).get("text", ""))
        except Exception:
            # Skip unreadable files
            continue
    return docs
