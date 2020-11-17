from typing import Optional


class SchedulerJobData:
    """Scheduler job data."""
    """The custom data the user specified when creating the scheduler source."""
    custom_data: Optional[str]

    def __init__(self, custom_data: Optional[str]) -> None:
        self.custom_data = custom_data
