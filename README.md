# tik-amuta
Scripts for processing the NPO-File ("tik amuta") distributed by the
Israeli Registrar of NPOs (רשם העמותות)

This is very initial for now, just something I needed and whipped up
and then made very slightly more generally usable.

The NPO registrar lets you buy a digital zip-file containing all the public
records of any NPO. But in the zipfile, what you get is a set of PDF files
with numbers instead of descriptive names, and next to them a folder containing
a Windows app for browsing the contents.

Luckily, that Windows app takes its data from a XML file that sits openly
in the same folder. This little Python script takes that XML file and builds
from it an HTML index file that people on non-Windows machines can use.

To use, extract all files from the Registrar's zip-file, and run make_index.py
from the root of the extracted folder. It runs interactively and asks you
where to put the index file. I'm not very proud of it, but I'm also not
going to invest much in it now.

