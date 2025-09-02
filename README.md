# TextTools (v0.1)
This is a small software that converts text in an image into plain text.

### Why?
Websites/Apps/Programs that do not allow you to copy/paste are annoying. >:(

### What does it do?
It uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) to identify text in image files and convert it into plain text.

### But there are tools online that do that easily!!!!
True, but, this one is _100% free!_ no annoying ads involved, no pop-ups, no image limit, and no trying to sell you a subscription!

### Alright, how do I install-

Nope! No installation required, fire up the .exe file (Linux support is intended soon) and you're good to go!

### Can I build from source?
That's... A bit complicated, the Tesseract OCR files are heavy after it's installation, which don't play well with Git, so, for now, you may need to stick with the Release files, sadly.

### That's one hefty release isn't it?
Tesseract's language recognition files are quite hefty, so for each language supported it gets slightly heavier, unfortunately, there isn't much I can do about this...

## Main functions:

- Choose an image file to convert to text
- Paste an image from the clipboard to convert to text
- Open image from a link to convert it to text
- More soon(?)

## To-do
- Language selector to optimize Tesseract's usage.
- Language selector for the interface (Currently the program is in Brazilian Portuguese only.)
- ... Make the interface look better.
- Linux support.
