from .settings import settings
from .landscape import Meadow


class PeriodicEventManager:
    """As the name states: It manages periodic events in the game loop
    ARGS:
        _map: The PlayMap the game is currently taking place on"""

    def __init__(self, _map):
        self.map = _map
        self.all_grass_objs = []
        self.all_water_objs = []

        for meadow in Meadow.all_grass:
            if meadow.map == _map:
                self.all_grass_objs += meadow.obs
        for water in Meadow.all_water:
            if water.map == _map:
                self.all_water_objs += water.obs

    def event(self):
        """Executes the events"""
        self.map.extra_actions()
        if settings("animations").val:
            Meadow.moving_grass(self.all_grass_objs)
            Meadow.moving_water(self.all_water_objs)
