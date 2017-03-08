#!/usr/bin/env python
#usage: BuildGallery.py "gallery name"

import os, shutil

#have way to choose which gallery to build 
#galleryList names are dependant on "img_gallery" directory name
galleryList = ['necklace','bracelet','earring']
for gallery in galleryList:
    galleryHtml = '/home/honuts/www/' + gallery + '.html'
    galleryHtmlOld = '/home/honuts/www/.' + gallery + '.html.old'
    galleryImg = '/home/honuts/www/img_' + gallery + '/'

#BACKUP jewelry.html to jewelry.html.old, maybe with date?
    if os.path.isfile(galleryHtml):
        shutil.move(galleryHtml, galleryHtmlOld)

#open jewelry.html
    gfile = open(galleryHtml, 'w')

#add boilerplate to top of jewelry.html from text file
    header = open('/home/honuts/www/.header.html.template')
    gfile.write(header.read())
    header.close()

#iterate through files in directory and 
#... add section to jewelry.html for each image/descritpion
    fileList = os.listdir(galleryImg)
    gfile.write('<h2>%s Gallery</h2>\n' %(gallery.title()))
    gfile.write('<div id="Gallery">\n')
    for i in range(len(fileList)):
        if fileList[i].endswith(".jpg"):
            gfile.write('  <div class="display">\n')
            gfile.write('    <img src="./img_' + gallery \
                    + '/' +fileList[i] + '">\n')
            if os.path.isfile(galleryImg + \
                    os.path.splitext(fileList[i])[0]):
                desc = open(galleryImg + \
                        os.path.splitext(fileList[i])[0])
                gfile.write('    <p>' + desc.read() + '</p>\n')
                desc.close()
            else:
                gfile.write('    <p>' + \
                        os.path.splitext(fileList[i])[0] + '\n')
            gfile.write('  </div>\n')
    gfile.write('</div>\n')

#add boilerplate to bottom of jewelry.html from text file
    footer = open('/home/honuts/www/.footer.html.template')
    gfile.write(footer.read())
    footer.close()
#close jewelry.html
    gfile.close()
#Make page for each image? 
