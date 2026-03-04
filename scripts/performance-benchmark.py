import time
import psutil
import resource

class PerformanceBenchmark:
    def __init__(self):
        self.start_time = time.time()
        self.start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    def measure_performance(self):
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        execution_time = end_time - self.start_time
        memory_usage = end_memory - self.start_memory
        cpu_usage = psutil.cpu_percent(interval=None)
        return execution_time, memory_usage, cpu_usage

if __name__ == '__main__':
    benchmark = PerformanceBenchmark()
    # Add your code here to benchmark
    exec_time, mem_usage, cpu_usage = benchmark.measure_performance()
    print(f'Execution Time: {exec_time} seconds')
    print(f'Memory Usage: {mem_usage} KB')
    print(f'CPU Usage: {cpu_usage}%')