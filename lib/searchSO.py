import sys


def searchStack(term):
    try:
        import stackexchange
    except ImportError:
        print("There was an error importing the stackoverflow api wrapper")
        sys.exit(0)
    #try:
    term = ' '.join(sys.argv[1:])
    SO = stackexchange.StackOverflow()
    qs = SO.search(intitle=term)
    print('\r--- questions with "%s" in title ---' % (term))
    for q in qs:
        print('%8d %s' % (q.id, q.title))
    #except:
        #print("There was an error running that stackoverflow api wrapper")