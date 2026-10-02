# PDF to Audiobook

A simple Python application that extracts text from PDF files and reads it aloud using text-to-speech.

## Features

- Select a PDF using a file picker
- Extract text from PDF pages
- Convert extracted text to speech
- Read multi-page PDFs automatically
- Works offline using `pyttsx3`

## Built With

- Python
- PyPDF2
- pyttsx3
- Tkinter

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd pdf-to-audiobook
```

Install the required packages:

```bash
pip install pyttsx3 PyPDF2
```

If `pip` isn't recognized on Windows, use:

```bash
py -m pip install pyttsx3 PyPDF2
```

## Usage

Run the program:

```bash
python main.py
```

Choose a PDF from the file picker and the program will extract its text and begin reading it aloud.

## Notes

The program works best with PDFs that contain selectable text. Scanned PDFs or PDFs containing only images cannot currently be read because they require OCR.

## Future Improvements

- Play, pause, and stop controls
- Reading speed controls
- Voice selection
- Page selection
- Audiobook file export
- GUI
- OCR support for scanned PDFs

## License

This project is open source and available for personal and educational use.
