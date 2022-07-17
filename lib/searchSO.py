import sys


def searchStack(term):
     sys.stdout.flush()
     try:
        import stackexchange
     except ImportError:
        print("There was an error importing the stackoverflow api wrapper")
        sys.exit(0)
    #try:
     SO = stackexchange.StackOverflow()
     qs = SO.search(intitle=term, pagesize=10, page=1)
     print('\n\n')

     if len(qs)==0:
        print("No results came back on that error.")
     search_index = 0
     for q in qs:
        search_index = search_index+1
        if search_index > 2:
            break
        else:
        # q.tittle q.id
            print(q.title)
    #except:
    #   print("There was an error running that stackoverflow api wrapper")