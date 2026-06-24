import sys
import os
from pathlib import Path

try:
    from PyPDF2 import PdfReader
except ImportError:
    print('PyPDF2 not installed')
    sys.exit(1)

pdf_path = Path('ADB_BRAND_GUIDELINES_- BRAND BOOK AUDIBEL.pdf')
output_path = Path('extracted_brand.txt')

if not pdf_path.is_file():
    print(f'PDF file not found: {pdf_path}')
    sys.exit(1)

reader = PdfReader(str(pdf_path))
text_pages = []
for page_num, page in enumerate(reader.pages, start=1):
    try:
        text = page.extract_text()
        if text:
            text_pages.append(f'--- Page {page_num} ---\n' + text)
    except Exception as e:
        print(f'Error extracting page {page_num}: {e}')

full_text = '\n\n'.join(text_pages)
output_path.write_text(full_text, encoding='utf-8')
print(f'Extraction completed. Saved to {output_path}')
