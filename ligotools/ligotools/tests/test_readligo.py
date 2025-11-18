import os
import numpy as np
import pytest
from ligotools import readligo as rl

DATA_DIR = "data"
H1 = os.path.join(DATA_DIR, "H-H1_LOSC_4_V2-1126259446-32.hdf5")
L1 = os.path.join(DATA_DIR, "L-L1_LOSC_4_V2-1126259446-32.hdf5")

@pytest.mark.parametrize("fn", [H1, L1])
def test_loaddata(fn):
    strain, time, chan_dict = rl.loaddata(fn)
    assert isinstance(strain, np.ndarray)
    assert isinstance(time, np.ndarray)
    assert len(strain) == len(time) > 0
    assert isinstance(chan_dict, dict)

def test_read_hdf5():
    strain, gpsStart, ts, qmask, dqnames, injmask, injnames = rl.read_hdf5(H1, readstrain=True)
    assert isinstance(strain, np.ndarray)
    assert strain.ndim == 1
    assert isinstance(gpsStart, (int, np.integer, np.floating))
    assert isinstance(ts, (float, np.floating))
    assert isinstance(qmask, np.ndarray)
    assert isinstance(dqnames, list)
    assert isinstance(injmask, np.ndarray)
    assert isinstance(injnames, list)