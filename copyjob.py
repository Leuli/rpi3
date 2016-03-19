import os
import shutil

class Copyjob:

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.copied_bytes = 0
        self.total_size = 0

    # create directory if not existing
    def make_dir(self,destination):
        if not os.path.exists(destination):
            os.makedirs(destination)

    # get the filesize in bytes for all files to be copied
    def get_overall_filesize(self):

        if os.path.isdir(self.src):
            for dirpath, dirnames, filenames in os.walk(self.src):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    self.total_size += os.path.getsize(fp)
        else:
            print("Copyjob: Error in count_all_files_size()")

        print("Copyjob: Total filesize: {}".format(self.total_size))

    # copy files and count copied bytes to measure progress
    def copy_files(self):

        # traverse directory
        for dirpath, dirnames, filenames in os.walk(self.src):

            # create necessary directories in dest folder
            for directory in dirnames:
                dest_dir = dirpath.replace(self.src, self.dest)
                self.make_dir(os.path.join(dest_dir, directory))

            # copy files and add size of copied files
            for sfile in filenames:
                src_file = os.path.join(dirpath, sfile)
                dest_file = os.path.join(dirpath.replace(self.src, self.dest), sfile)
                print(src_file)
                print(dest_file)
                shutil.copy(src_file, dest_file)
                self.copied_bytes += os.path.getsize(src_file)
                print(self.copied_bytes)



    # start the copy job
    def start_job(self):
        self.get_overall_filesize()
        self.copy_files()
