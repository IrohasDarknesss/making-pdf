import img2pdf
import glob
from natsort import natsorted 

# Get Image Lists
lists = list(glob.glob("your_path/*.jpg"))

# Making PDF file
pdfpath = "default.pdf"
with open(pdfpath,"wb") as f:
    f.write(img2pdf.convert([str(i) for i in natsorted(lists) if ".jpg" in i]))
