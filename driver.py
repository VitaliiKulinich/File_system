from file_system import FileSystem


class Driver:
    FS = FileSystem(100)

    def __init__(self):
        self._file_system = None

    def mkfs(self, n):
        self._file_system = FileSystem(n)

    def mount(self):
        self._file_system = self.FS

    def unmount(self):
        self._file_system = None

    def fstat(self, name):
        if self._file_system:
            return self._file_system.find_file_descriptor_by_name(name)

    def ls(self):
        if self._file_system:
            return self._file_system.dir.dir_links

    def create(self, name):
        if self._file_system:
            self._file_system.create_file(name)

    def open(self, name):
        if self._file_system:
            file = self._file_system.find_file_descriptor_by_name(name)
            return self._file_system.open(file)

    def close(self, fd):
        if self._file_system:
            self._file_system.close(fd)

    def read(self, fd, offset, size):
        data = ''
        if self._file_system:
            file = self._file_system.find_file_by_number_of_fd(fd)
            if file:
                for block in self._file_system.read_file(offset, size, file):
                    data += block.data[0:size]
            else:
                return None

        return data

    def write(self, fd, offset, size, data):
        if self._file_system:
            file = self._file_system.find_file_by_number_of_fd(fd)
            self._file_system.write_file(offset, size, data, file)

    def link(self, name1, name2):
        if self._file_system:
            fd = self._file_system.find_file_descriptor_by_name(name1)
            if fd:
                self._file_system.create_link(name2, fd)

    def unlink(self, name):
        if self._file_system:
            link = self._file_system.find_link_by_name(name)
            self._file_system.remove_link(link)

    def truncate(self, name, size):
        if self._file_system:
            file = self._file_system.find_file_descriptor_by_name(name)
            self._file_system.truncate_file(file, size)