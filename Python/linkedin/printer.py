import numpy as np

class PrintQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds an item to the back of the queue (= front of the list!)
                    --> insert to the 0th index in the list.
        Runtime: O(n) linear time: the bigger the queue, the longer it takes to add another item.
        """
        self.items.insert(0, item)


    def dequeue(self):
        """Returns and removes the front item of the queue (= last item of the list).

        Runtime: O(1) constant: does not depend on the size of the queue."""

        if self.items:
            return self.items.pop()
        return None


    def peek(self):
        """Returns the first item of the queue.
        Returns None if empty

        Runtime: O(1)"""

        if self.items:
            return self.items[-1]
        return None


    def size(self):
        return len(self.items)


    def is_empty(self):
        return self.items == []

#------------------------------------------------------------------------------

class Job:

    def __init__(self):
        self.pages = np.random.randint(1,11)


    def check_complete(self):
        return self.pages == 0


    def print_page(self):
        if not self.check_complete():
            self.pages -= 1

#------------------------------------------------------------------------------

class Printer:

    def __init__(self):
        self.queue = PrintQueue()

    def get_job(self, job):
        self.queue.enqueue(job)


    def print_job(self):

        if not self.queue.is_empty():
            job = self.queue.dequeue()
            total_pages = job.pages
            i = 1
            while not job.check_complete():
                print(f"\tPrinting... page {i}/{total_pages}")
                job.print_page()
                i+=1
            print("\n\tDone printing this document!")
        else:
            print("There is nothing to print...")

    def print_all(self):

        number_of_jobs = self.queue.size()
        i=1
        while not self.queue.is_empty():
            print(f"\n\nDocument {i}/{number_of_jobs}")
            print("-------------------------\n")
            self.print_job()
            i+=1
        print("\nAll documents have been printed!")
