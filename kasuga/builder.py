# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Masahiko Hashimoto <hashimom@geeko.jp>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import csv
from kasuga.reader import Reader


class Builder:
    def __init__(self):
        self.infos = []

    def read(self, in_file):
        reader = Reader(in_file)
        infos = reader()

        f = open('input.csv', 'w')
        writer = csv.writer(f, lineterminator='\n')

        for info in infos:
            for chunk in info["Chunks"]:
                ind_surface = ""
                anc_surface = ""
                lnk_surface = ""

                # Independent
                if len(chunk["Independent"]) != 0 and not chunk["Link"] is None:
                    for independent in chunk["Independent"]:
                        ind_surface += independent["surface"]

                    # Ancillary
                    for ancillary in chunk["Ancillary"]:
                        if ancillary["position"][0] != "特殊":
                            anc_surface += ancillary["surface"]

                    # Link
                    for link in chunk["Link"]:
                        lnk_surface += link["surface"]

                    writer.writerow([ind_surface, anc_surface, lnk_surface])

        f.close()

    def __call__(self):
        pass


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-f', nargs='?', help='input text file', required=True)
    args = arg_parser.parse_args()

    builder = Builder()
    builder.read(args.f)


if __name__ == "__main__":
    main()
