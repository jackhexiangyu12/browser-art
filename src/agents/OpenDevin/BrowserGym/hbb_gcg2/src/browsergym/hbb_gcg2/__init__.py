from browsergym.core.registration import register_task

# register the WebArena benchmark
from .task import HBBTask
from .config import TASK_IDS

ALL_WEBARENA_TASK_IDS = []

# register the WebArena benchmark
for task_id in TASK_IDS:
    gym_id = f"hbb_gcg2.{task_id}"
    register_task(
        gym_id,
        HBBTask,
        kwargs={"task_kwargs": {"task_id": task_id}},
    )
    ALL_WEBARENA_TASK_IDS.append(gym_id)
