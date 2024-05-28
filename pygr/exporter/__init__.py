import threading as th
from .exporter_functions import check_exporter_queue


class ExporterQ(Queue):
    def __init__(self, q):
        self.export_queue = []
        self.initialize_export_queue_handler()

    def add_to_q(self, element):
        self.export_queue.append(element)

    def remove_first_from_q(self):
        if len(self.export_queue) > 0:
            self.export_queue.pop(0)

    def is_there_elements_in_q(self):
        return len(self.export_queue) > 0

    def get_first_in_q(self):
        return self.export_queue[0]

    def initialize_q(self, fn):
        thread = th.Thread(target=fn, args=[self])
        thread.start()
