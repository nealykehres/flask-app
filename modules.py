

import csv
def convert_to_dict(filename):
    # open a CSV file - note - must have column headings in top row
    datafile = open(filename)

    # create list of OrderedDicts as of Python 3.6
    my_reader = csv.DictReader(datafile)

    # write it all out to a new list
    list_of_dicts = []
    for row in my_reader:
        # we convert each row to a string and add a newline
        list_of_dicts.append( dict(row) )

    # close original csv file
    datafile.close()
    # return the list
    return list_of_dicts

def search_the_list(list):
    for item in list:
        if "Whig" in item['Party']:
            print(item['President'] + " was a Whig.")
    for k in list[0].keys():
        print(k)

# run tests
if __name__ == '__main__':
    test_make_ordinal()
    presidents_list = convert_to_dict("presidents.csv")
    search_the_list(presidents_list)
    print(make_ordinal(12))
    print(make_ordinal(32))
