import urllib
import re
import os
#sections = ["anime","abstract","animals","astronomy","computers",
#            "crafted-nature","gaming","celebrities","industrial","macabre",
#            "microscopic","music","nature",
#            "popular-culture","science-fiction","sports","vehicles"] #A list of all the site's sections.

sections = ["abstract", "animals", "astronomy", "computers",  # An edited list for the sections I want.
            "crafted-nature", "celebrities", "industrial", "macabre",
            "microscopic", "music", "nature", "science-fiction", "sports", "vehicles"]  # A list of all the site's sections.

index = "http://dualmonitorbackgrounds.com/"

size = ("3840", "1200")

WORKERS = 10

subfolders = False


# Makes a new folder if one doesn't exist.
def makeDir(section):
    if not subfolders:
        return
    if not os.path.exists(section):
        print "Folder: " + section + " not found. Creating folder."
        os.makedirs(section)


def getHTML(url):
    return urllib.urlopen(url).read()


def getImageNameList(section, page):
    url = index + section + "/page/" + str(page)
    html = getHTML(url)
    print url
    find = "/" + section + "/" + "(.+)\.jpg\.php"
    return list(set(re.findall(find, html)))


def getMaxPage(section):
    html = getHTML(index + section)
    find = "/{0}/page/(\d+)/".format(section)
    return max([int(x) for x in re.findall(find, html)])


def fileExists(section, name):
    return os.path.isfile(getImagePath(section, name))


def getImageFilename(name):
    return "{0}_w{1}_h{2}_cw{1}_ch{2}.jpg".format(name, size[0], size[1])


def getImagePath(section, name):
    if subfolders:
        return section + os.sep + getImageFilename(name)
    else:
        return getImageFilename(name)


def getImageURL(section, name):
    return "{0}cache/{1}/{2}".format(index, section, getImageFilename(name))


def saveImage(section, name):
    if fileExists(section, name):
        print name + " exists. Skipping."
        return
    print "Getting picture " + name
    urllib.urlretrieve(getImageURL(section, name), getImagePath(section, name))


def main():
    for section in sections:
        print "Starting section " + section
        makeDir(section)
        for page_number in xrange(1, getMaxPage(section)):
            imagenames = getImageNameList(section, page_number)
            for name in imagenames:
                saveImage(section, name)
        print "Section done."
    print "All done. Enjoy!"

if __name__ == '__main__':
    main()
