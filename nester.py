import sys


def nestPrint(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            nestPrint(each_item)
        else:
            print(each_item)


def print_lol(the_list, indent=False , level=0, outfile=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, outfile)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='',file=outfile)
            print(each_item, file=outfile)