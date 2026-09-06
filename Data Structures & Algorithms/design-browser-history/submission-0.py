class BrowserHistory:

    def __init__(self, homepage: str):
        headSite = Site(homepage)
        self.head = headSite
        self.tail = headSite

    def visit(self, url: str) -> None:
        newSite = Site(url)
        currTail = self.tail
        self.tail.next = newSite
        self.tail = newSite
        newSite.prev = currTail


    def back(self, steps: int) -> str:
        curr = self.tail
        count = 0
        while curr.prev != None:
            if count == steps:
                self.tail = curr
                return curr.url
            count += 1
            curr = curr.prev

        self.tail = curr
        return curr.url    

    def forward(self, steps: int) -> str:
        curr = self.tail
        count = 0
        while curr.next != None:
            if count == steps:
                self.tail = curr
                return curr.url
            count += 1
            curr = curr.next
        
        self.tail = curr
        return curr.url


class Site:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)