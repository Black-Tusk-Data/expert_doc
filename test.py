#!/usr/bin/env python3

import subprocess
import time
from pathlib import Path

from expert_doc import PdfParser


path = Path("./Measurement_and_Instrumentation.pdf")


def main():
    print("downloading textbook...")
    subprocess.check_call([
        "wget", "https://shareok.org/bitstream/handle/11244/325397.3/Measurement_and_Instrumentation.pdf?sequence=6&isAllowed=y",
        "-O", str(path),
    ])
    t0 = time.time()
    pages = list(PdfParser(path).iter_pages())
    t1 = time.time()
    print("parsed", len(pages), "pages in", round(t1 - t0, 2), "seconds")
    return


if __name__ == '__main__':
    main()
