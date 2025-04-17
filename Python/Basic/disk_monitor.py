import subprocess
import re
import sys


class DiskMonitorError(Exception):
    pass


class DiskMonitor:
    def __init__(self, partition, threshold):
        self.partition = partition
        self.threshold = threshold

    @staticmethod
    def convert_bytes(size):
        """Converts the input size (in KB) into a more readable format"""
        for x in ["K", "M", "G", "T"]:
            if size < 1024.0:
                return f"{size:3.1f} {x}B"
            size /= 1024.0

        # use , as the thousand separater; f'{value:,}'
        # convert_bytes(int(2251799813685248)), 2,048.0
        return f"{size:,}"

    def get_disk_space(self):
        """Returns the available disk space (in KB) and percentage utilization"""
        if sys.platform == "linux":
            try:
                out = subprocess.run(["df"], check=True, capture_output=True, text=True)
            except subprocess.SubprocessError as e:
                raise DiskMonitorError(f"Failed to measure disk space: {e}")

            # Parse the output to get the available space and the percentage
            # of disk utilization of the specified disk partition.
            pattern = f".* (\\d+) .* (\\d+)%.*{self.partition}\n"

            try:
                parsed = re.search(pattern, out.stdout)
                if parsed is None:
                    raise DiskMonitorError('Failed to parse "df" output')
            except Exception as e:
                print(e)
                sys.exit(1)
        else:
            print(f"OS ({sys.platform}) not supported!")
            sys.exit(1)

        return int(parsed.group(1)), int(parsed.group(2))

    def monitor(self):
        """Returns an alert if the disk is almost full"""
        _, use = self.get_disk_space()
        if use >= self.threshold:
            return f"{self.partition} utilization over {use}%."


test = DiskMonitor("/", 10)
available, use = test.get_disk_space()
print(available, use)
print(test.monitor())
print(DiskMonitor.convert_bytes(available))
print(DiskMonitor.convert_bytes(2251799813685248))

# .* to get all the chars
# grouping with parentheses

# When a method is defined using the @classmethod decorator, the method is
# bound to the class and not to an instance of the class. As a result, the
# method receives the class (cls) as its first argument, rather than an
# instance (self).

# use the assert keyword to check whether a condition is met and let
# Python raise the AssertionError if the condition isn't met.
# number = 10
# assert number < 5, f"The number should not exceed 5. ({number=})"
# print(number)
