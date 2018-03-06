from CS312Graph import *
import math


class ArrayQueue:

    def __init__(self):
        self.list = list()

    def make_queue(self, nodes):
        for node in nodes:
            self.list.append(node)

    def delete_min(self):
        min_idx = 0
        min_value = math.inf
        for i in range(len(self.list)):
            if self.list[i].dist < min_value:
                min_idx = i
                min_value = self.list[i].dist
        return self.list.pop(min_idx)

    def decrease_key(self, to_adjust):
        pass

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False


class HeapQueue:
    def __init__(self):
        self.heap_array = list()
        self.heap_array.append(None)

    def decrease_key(self, node):
        if not (node.idx > self.get_size()):
            self.bubble_up(node.idx)

    def make_queue(self, nodes):
        for node in nodes:
            self.insert(node)

    def insert(self, to_insert):
        self.heap_array.append(to_insert)
        to_insert.idx = self.get_size()
        self.bubble_up(self.get_size())

    def bubble_up(self, idx):
        while idx // 2 > 0:
            if self.heap_array[idx].dist < self.heap_array[idx // 2].dist:
                temp = self.heap_array[idx // 2]
                self.heap_array[idx // 2] = self.heap_array[idx]
                self.heap_array[idx // 2].idx = idx // 2
                self.heap_array[idx] = temp
                temp.idx = idx
            idx = idx // 2

    def delete_min(self):
        to_return = self.heap_array[1]
        self.heap_array[1] = self.heap_array[self.get_size()]
        self.heap_array.pop()
        self.bubble_down(1)
        return to_return

    def bubble_down(self,idx):
        while (idx * 2 ) <= self.get_size():
            min_idx = self.get_min_child(idx)
            if min_idx == None:
                return
            else:
                if self.heap_array[idx].dist > self.heap_array[min_idx].dist:
                    temp = self.heap_array[idx]
                    self.heap_array[min_idx].idx = idx
                    self.heap_array[idx] = self.heap_array[min_idx]
                    temp.idx = min_idx
                    self.heap_array[min_idx] = temp
            idx = min_idx

    def get_min_child(self, idx):
        if idx * 2 > self.get_size():
            return None
        elif (idx * 2) + 1 > self.get_size():
            return idx * 2
        else:
            left_child = self.heap_array[idx * 2]
            right_child = self.heap_array[(idx *2 ) + 1]
            if left_child.dist < right_child.dist:
                return idx * 2
            else:
                return (idx * 2) + 1

    def get_size(self):
        return len(self.heap_array) - 1

    def is_empty(self):
        if len(self.heap_array) == 1:
            return True
        else:
            return False