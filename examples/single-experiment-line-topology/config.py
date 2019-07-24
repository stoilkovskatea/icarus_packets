"""Configuration file for running a single simple simulation."""
from multiprocessing import cpu_count
from collections import deque
import copy
from icarus.util import Tree

# GENERAL SETTINGS

# Level of logging output
# Available options: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = 'INFO'

# If True, executes simulations in parallel using multiple processes
# to take advantage of multicore CPUs
PARALLEL_EXECUTION = False

# Number of processes used to run simulations in parallel.
# This option is ignored if PARALLEL_EXECUTION = False
N_PROCESSES = cpu_count()

# Number of times each experiment is replicated
N_REPLICATIONS = 1

# Granularity of caching.
# Currently, only OBJECT is supported
CACHING_GRANULARITY = 'OBJECT'

# Format in which results are saved.
# Result readers and writers are located in module ./icarus/results/readwrite.py
# Currently only PICKLE is supported
RESULTS_FORMAT = 'PICKLE'

# List of metrics to be measured in the experiments
# The implementation of data collectors are located in ./icarus/execution/collectors.py
DATA_COLLECTORS = ['CACHE_HIT_RATIO_SESSIONS', 'LATENCY_SESSIONS']

# Queue of experiments
EXPERIMENT_QUEUE = deque()

# Create experiment
experiment = Tree()

# Set topology
experiment['topology']['name'] = 'TREE'
experiment['topology']['k'] = 2
experiment['topology']['h'] = 3
experiment['topology']['delay'] = 5

# Set workload
experiment['workload'] = {
         'name':       'STATIONARY_UPDATED',
         'n_contents': 10 ** 2,
         'n_warmup':   9**2,
         'n_measured': 4*10 **4,
         'alpha':      0.8,
         'chunks_per_content': [(25,1), (25,1) , (50,1)]
                           }

# Set cache placement
experiment['cache_placement']['name'] = 'UNIFORM_NEW'
experiment['cache_placement']['network_cache'] = 0.05
experiment['cache_placement']['receiver_option'] = False

# Set content placement
experiment['content_placement']['name'] = 'UNIFORM'

# Set cache replacement policy
experiment['cache_policy']['name'] = 'LRU'

# Set caching meta-policy
experiment['strategy']['name'] = 'LCE_UPDATED'

# Description of the experiment

experiment['desc'] = "Tree topology"
# Append experiment to queue
EXPERIMENT_QUEUE.append(experiment)
