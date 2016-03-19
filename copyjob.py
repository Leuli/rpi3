import os
import shutil
import threading


class Copyjob(threading.Thread):

    def __init__(self, src, dest):
        threading.Thread.__init__(self)
        self.src = src
        self.dest = dest
        self.copied_bytes = 0
        self.total_bytes = 0

    def get_progress(self):
        return self.copied_bytes / self.total_bytes

    # get the filesize in bytes for all files to be copied
    def __get_overall_filesize(self):

        if os.path.isdir(self.src):
            for dirpath, dirnames, filenames in os.walk(self.src):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    self.total_bytes += os.path.getsize(fp)
        else:
            print("Copyjob: Error in count_all_files_size()")

        print("Copyjob: Total filesize: {}".format(self.total_bytes))

    # copy files and count copied bytes to measure progress
    def __copy_files(self):

        # traverse directory
        for dirpath, dirnames, filenames in os.walk(self.src):

            # copy files and add size of copied files
            for sfile in filenames:
                src_file = os.path.join(dirpath, sfile)
                dest_file = os.path.join(dirpath.replace(self.src, self.dest), sfile)

                # create destination directory
                if not os.path.exists(os.path.dirname(dest_file)):
                    os.makedirs(os.path.dirname(dest_file))

                shutil.copy(src_file, dest_file)
                self.copied_bytes += os.path.getsize(src_file)
                print("progress: {}".format(self.get_progress()))

    # this functions runs the job as thread
    def run(self):
        self.__get_overall_filesize()
        self.__copy_files()
