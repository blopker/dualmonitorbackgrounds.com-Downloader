import urllib #URL library
import re #Regular Expression
import os #OS System library

#sections = ["anime","abstract","animals","astronomy","computers",
#            "crafted-nature","gaming","celebrities","industrial","macabre",
#            "microscopic","mobile-technology","music","nature",
#            "popular-culture","science-fiction","sports","vehicles"] #A list of all the site's sections.

sections = ["anime","abstract","animals","astronomy","computers", #An edited list for the sections I want.
            "crafted-nature","celebrities","industrial","macabre",
            "microscopic","music","nature"
            ,"science-fiction","sports","vehicles"] #A list of all the site's sections.

for section in sections: #Do this for each section in the list.
    print "Starting section " + section
    if not os.path.exists(section): #Makes a new folder for the section if one doesn't exist.
        print "Folder: " + section + " not found. Creating folder."
        os.makedirs(section)
    pagenumber = 1 #Keeps track of the page number for each section.
    while True: #Do this for as long as the page has wallpapers on it.
        url = "http://www.dualmonitorbackgrounds.com/" + section + "/" + "page" + "/" + str(pagenumber) + "/" #Formatted URL root (string)
        site = urllib.urlopen(url) #Create a site object.
        find = "/" + section + "/" + "(.+)\.jpg\.php" #Creates a regular expression 'search term' 
        imagenames = re.findall(find,site.read()) #Opens the URL and searches the source code for search terms matches. imagenames is a list of images found.
        if len(imagenames) == 0: #If no images were found, we are on the last page. Move on to the next section.
            print "Section done."
            break; #Pop out of the while loop.
        for name in imagenames: #Do this for each image name.
            if os.path.isfile(section+os.sep+name+".jpg"): #If the file is already there, skip it.
                print "File " + section+os.sep+name+".jpg" + " exists. Skipping."
                continue
            print "Getting picture " + name + ".jpg"
            imagelocation = "http://www.dualmonitorbackgrounds.com/albums/"+section+"/"+name+".jpg" #Create the final URL with the image name.
            urllib.urlretrieve(imagelocation,section+os.sep+name+".jpg") #Download and save the image in its section's folder.
        pagenumber += 1 #Add one to the page number counter.
print "All done. Enjoy!"
