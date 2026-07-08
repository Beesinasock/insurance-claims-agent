import pdfplumber
from pathlib import Path


class DocumentParser:
    """
    Reads FNOL documents and returns plain text.
    Supports PDF and TXT files.
    """

    def read_document(self, file_path):
        """
        Reads a PDF or TXT document and returns its content as a string.
        """

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if file_path.suffix.lower() == ".txt":
            return self._read_txt(file_path)

        elif file_path.suffix.lower() == ".pdf":
            return self._read_pdf(file_path)

        else:
            raise ValueError(
                f"Unsupported file type: {file_path.suffix}"
            )

    def _read_txt(self, file_path):
        """
        Reads text files.
        """

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def _read_pdf(self, file_path):
        """
        Reads PDF files.
        """

        text = ""

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text.strip()