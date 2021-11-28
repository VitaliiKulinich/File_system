class FileDescriptor:
    def __init__(self, type):
        self.type = type
        self.number_of_links = 0
        self.blocks = {}
        self.dir_links = []

    def size(self):
        size_of_blocks = 0
        for block in self.blocks.values():
            size_of_blocks += len(block.data)
        return size_of_blocks if self.type == "File" else None
