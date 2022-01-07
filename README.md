# PDF Imposition Tool

* This tool imposes a PDF such that 4 pages will appear on 1 page :))

## Background
* In some of my courses, I learn best when take notes on my lecture slides. However, scrolling through 50+ slides per lecture can get messy, so I like to format my notes so that 4 slides are on one page.
* I can perform manually impose my PDFs with a PDF editor, but that requires a decent amount of 'clicks' and the time adds up. I made this program to save some time :))
* Given the file path, this tool automatically formats a new PDF with 4 slides on each page.

## Dependencies
* [PyPDF2](https://pypi.org/project/PyPDF2/) (`pip install PyPDF2`)

## Usage
Run the following command from the command line.
```
python imposition.py <input_file_path.pdf> <output_file_path.pdf>
```
If an ouput file path is not provided (i.e., `python imposition.py <input_file_path.pdf>`), the new PDF will overwrite the original PDF and will be saved there.

## Example
This is a sample of what an imposed PDF would look like.
![image](https://user-images.githubusercontent.com/68765813/148579172-58147f7e-b570-4a0d-87cd-dbe9745d3017.png)
