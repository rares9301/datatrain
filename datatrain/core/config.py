# config.py
import os

# Routing workflows
# get project root
PROJECT_ROOT = os.getenv('PROJECT_ROOT')
if PROJECT_ROOT is None:
    raise EnvironmentError('Variabila de mediu PROJECT_ROOT nu este setată.')

# create work directory
WORKLOAD_DIR = os.path.join(PROJECT_ROOT, 'workload')
if not os.path.exists(WORKLOAD_DIR):
    os.makedirs(WORKLOAD_DIR)

# create script paths
outliers_script_path = os.path.join(PROJECT_ROOT, 'datatrain', 'core', 'codebase', 'outliers.py')


