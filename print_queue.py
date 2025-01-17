import time
import threading
from queue import Queue

class PrintJob:
    def __init__(self, document_name, pages):
        self.document_name = document_name
        self.pages = pages

    def __str__(self):
        return f"{self.document_name} ({self.pages} pages)"

class PrintQueue:
    def __init__(self):
        self.queue = Queue()
        self.lock = threading.Lock()
        self.current_job = None

    def add_job(self, print_job):
        with self.lock:
            self.queue.put(print_job)
            print(f"Added to queue: {print_job}")

    def process_jobs(self):
        while True:
            with self.lock:
                if not self.queue.empty():
                    self.current_job = self.queue.get()
                    print(f"Processing: {self.current_job}")
                    time.sleep(self.current_job.pages * 0.5)  # Simulate time taken to print
                    print(f"Completed: {self.current_job}")
                    self.current_job = None
                else:
                    print("Queue is empty, waiting for jobs...")
            time.sleep(3)  # Wait before checking the queue again

    def start_processing(self):
        thread = threading.Thread(target=self.process_jobs)
        thread.daemon = True
        thread.start()

def main():
    print_queue = PrintQueue()
    print_queue.start_processing()

    # Example jobs
    print_queue.add_job(PrintJob("Document1", 5))
    print_queue.add_job(PrintJob("Document2", 3))
    print_queue.add_job(PrintJob("Document3", 10))

    # Simulate adding more jobs over time
    time.sleep(10)
    print_queue.add_job(PrintJob("Document4", 2))
    print_queue.add_job(PrintJob("Document5", 6))

    # Keep the main thread alive
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()