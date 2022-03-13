# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
utils/initialization
"""

from .augmentations import letterbox
from .downloads import attempt_download
from .general import non_max_suppression, intersect_dicts, scale_coords, set_logging
from .torch_utils import select_device

__all__ = [
    "attempt_download",
    "intersect_dicts",
    "letterbox",
    "non_max_suppression",
    "notebook_init",
    "scale_coords",
    "select_device",
    "set_logging",
]


def notebook_init(verbose=True):
    # Check system software and hardware
    print("Checking setup...")

    import os
    import shutil

    from yolort.v5.utils.general import check_requirements, emojis, is_colab
    from yolort.v5.utils.torch_utils import select_device  # imports

    check_requirements(("psutil", "IPython"))
    import psutil
    from IPython import display  # to display images and clear console output

    if is_colab():
        shutil.rmtree("/content/sample_data", ignore_errors=True)  # remove colab /sample_data directory

    if verbose:
        # System info
        # gb = 1 / 1000 ** 3  # bytes to GB
        gib = 1 / 1024 ** 3  # bytes to GiB
        ram = psutil.virtual_memory().total
        total, used, free = shutil.disk_usage("/")
        display.clear_output()
        s = (
            f"({os.cpu_count()} CPUs, {ram * gib:.1f} GB RAM, "
            f"{(total - free) * gib:.1f}/{total * gib:.1f} GB disk)"
        )
    else:
        s = ""

    select_device(newline=False)
    print(emojis(f"Setup complete ✅ {s}"))
    return display
