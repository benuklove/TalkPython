"""

  Created on 8/6/2017 by Ben

  benuklove@gmail.com
  
  

"""

from movie_client import MovieClient
import requests.exceptions

def main():
    print_header()
    search_event_loop()


def print_header():
    print("---------------------------------")
    print("       MOVIE SEARCH APP")
    print("---------------------------------")
    print()


def search_event_loop():
    search = "ONCE_THROUGH_LOOP"

    while search != 'x':
        try:
            search = input('Title search text (x to exit): ')
            if search != 'x':
                client = MovieClient(search)

                results = client.perform_search()
                print("Found {} results.".format(len(results)))
                for r in results:
                    print("{} - - {}".format(r.Year, r.Title))

                # print(client.perform_search())
                print(client.perform_search())
        except requests.exceptions.ConnectionError:
            print("Cannot search, network is down.")
        except ValueError as ve:
            print("ERROR, your search entry is invalid: {}".format(ve))
        except Exception as x:
            print("ERROR: {}".format(x))

    print('exiting...')


if __name__ == '__main__':
    main()
