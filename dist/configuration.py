import yaml
from collections import namedtuple

MasterConfig = namedtuple('Server', ('addr', 'push', 'pull', 'ctrl', 'store'))
WorkerConfig = namedtuple('Worker', ('addr', 'push', 'pull', 'ctrl', 'store'))
StoreConfig  = namedtuple('Store', ('addr', 'port'))
DistConfig   = namedtuple('Dist', ('master', 'workers', 'stores'))

def load(fname):
    """ Load and validate configuration """

    config = yaml.load(open(fname))

    stores = []
    workers = []
    master = None

    master = MasterConfig(
        config['master'],
        config['push'],
        config['pull'],
        config['ctrl'],
        config['store'],
    )

    for addr in config['workers'].values():
        worker = MasterConfig(
            addr,
            config['push'],
            config['pull'],
            config['ctrl'],
            config['store'],
        )
        workers.append(worker)

    for addr, port in config['stores'].values():
        store = StoreConfig(
            addr,
            port
        )
        stores.append(store)

    return DistConfig(master, workers, stores)
