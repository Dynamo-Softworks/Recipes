# -*- coding: utf-8 -*-
import webbrowser, requests, bs4, string, sys, random

#sets the random seed to the current time
random.seed()
#init array for random inputs
rando = []

#this chooses a page and then steals the ingrediant list from it
def website_reacher():
    website_base = 'http://www.allrecipes.com/recipe/'
    for x in range(0, 1):
        webid = str(random.randint(10000,30000))
        try:
            website_numb = website_base + webid
            website_prin = website_numb
            res = requests.get(website_prin)
            res.raise_for_status()
            website = bs4.BeautifulSoup(res.text, "html.parser")
            ingr = website.select("li.checkList__line")
            for ingredient in ingr:
                lines = ingredient.getText()
                #removes a certain line from the list
                if lines.find("Add all ingre") == -1:
                    lines = lines.split()
                    lines = [line for line in lines if line.strip()]
                    if (random.randint(0,10) == 5):
                        rando.append(lines)
                    #uncommenting this will print the original recipe
                    #printer_func_two(lines)
        except:
            #uncommenting this will print the unavailable urls
            #print_the_invalids(webid)
            return

#generates weird recipes
def weird_recipper():
    website_reacher()
    if len(rando) > 5:
        printer_func(rando)
        del rando[:]
#print for the gen'd recipes
def printer_func(rando):
    print ">>>>>>>>>>>>>>>>"
    for lines in rando:
        if len(lines) < 2:
            del lines
        else:
            for line in lines:
                if (line.find("ADVERTISEMENT") == -1):
                    try:
                        sys.stdout.write(line)
                        sys.stdout.write(" ")
                        sys.stdout.flush()
                    except:
                        print "ERROR! AH!"
            print
    print "<<<<<<<<<<<<<<<<"
    print
#print for the normal recipes
def printer_func_two(lines):
    for line in lines:
        #Every line ends with "ADVERTISEMENT" for some html/css/web dev reason
        #this removes it
        if line.find("ADVERTISEMENT") == -1:
            sys.stdout.write(line)
            sys.stdout.write(" ")
            sys.stdout.flush()
        else:
            del line
    print
#prints the invalid urls
def print_the_invalids(webid):
    print
    print webid + " is not valid"
    print

#kicks off the party
def main():
    for x in range(0,100):
        weird_recipper()
        
main()
