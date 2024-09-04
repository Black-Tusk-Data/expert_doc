"""
img = PdfImage(list(page.images.values())[0])
img.extract_to(fileprefix='image001')
"""
from pathlib import Path
from typing import Iterable, NamedTuple

import pikepdf
from pikepdf import Pdf, PdfImage, Name
import pypdfium2 as pdfium


class Image(NamedTuple):
    raw_img: PdfImage

    def dump_to_file(self, name_no_extension: str) -> str:
        return self.raw_img.extract_to(fileprefix=name_no_extension)

    pass


class ParsedPage(NamedTuple):
    images: list[Image]
    text: str
    pass


class PdfParser:
    def __init__(self, path: Path):
        self.path = path
        self.img_pdf = pikepdf.Pdf.open(path)
        self.text_pdf = pdfium.PdfDocument(str(path))
        assert len(self.img_pdf.pages) == len(self.text_pdf)
        return

    def iter_page_contents(self) -> Iterable[ParsedPage]:
        for text_page, img_page in zip(
                self.text_pdf,
                self.img_pdf.pages,
        ):
            yield ParsedPage(
                images=[
                    Image(raw_img=PdfImage(img))
                    for img in img_page.images.values()
                ],
                text=text_page.get_textpage().get_text_range(),
            )
            pass
        return
    pass
