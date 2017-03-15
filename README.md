# BuildGallery
Python script used to populate HTML files for rustybearstudio.com based on contents of image gallery directories.

Html files are in the same directory as:
  .header.html.template
  .footer.html.template
  .about.html.template
  .index.html.template
BuildGallery.py builds each gallery starting with .header..., then iterates through img_ gallery directories to add necessary <div> and other such HTML for the gallery page, and ends the file with .footer...
index.html and about.html are built by processing the appropirate html.template files in order and saving to file.
