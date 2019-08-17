# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    # Initialize the trie with an root node and a handler, this is the root path or home page node
    def __init__(self):
        self.root = RouteTrieNode()

    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest) node of this path
    def insert(self, path_list, endOfWord):
        current_node = self.root

        for item in path_list:
            current_node.insert(item)
            current_node = current_node.next[item]

        current_node.endOfWord = endOfWord

    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or None for no match
    def find(self, path_list):
        current_node = self.root

        for item in path_list:
            if item in current_node.next.keys():
                current_node = current_node.next[item]
            else:
                return None
        return current_node.endOfWord


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    # Initialize the node with children as before, plus a handler
    def __init__(self):
        self.endOfWord = None
        self.next = {}

    # Insert the node as before
    def insert(self, word):
        if word not in self.next.keys():
            self.next[word] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
    def __init__(self, root_handler, not_found_handler):
        self.routeTrie = RouteTrie()
        self.rootHandler = root_handler
        self.notFound = not_found_handler

    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie
    def add_handler(self, path, handler):
        path_list = self.split_path(path)
        self.routeTrie.insert(path_list, handler)

    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
    def lookup(self, path):
        path_list = self.split_path(path)
        if len(path_list) == 0:
            return self.rootHandler
        ret = self.routeTrie.find(path_list)
        if ret is None:
            return self.notFound
        else:
            return ret

    # you need to split the path into parts for
    # both the add_handler and loopup functions,
    # so it should be placed in a function here
    def split_path(self, path):
        if path[-1] == "/":
            path = path[:-1]
        return path.split("/")[1:]


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one

