from typing import List, Optional, Tuple

from now8_api.data.database import SqlEngine
from now8_api.domain import Line, Stop, TransportType, VehicleEstimation
from now8_api.service.city_data import CityData
from overrides import overrides
from pydantic.dataclasses import dataclass


class FakeCityData(CityData):
    @overrides
    async def get_estimations(
        self,
        stop: Stop,
    ) -> List[VehicleEstimation]:
        return []

    @overrides
    async def get_stops_city(
        self,
        transport_types: List[TransportType] = None,
    ) -> List[Stop]:
        return []

    @overrides
    async def get_stops_line(
        self,
        line: Line,
    ) -> Tuple[List[Stop], List[Stop]]:
        return ([], [])

    @overrides
    async def get_lines_stop(
        self,
        stop: Stop,
    ) -> List[Line]:
        return []


@dataclass
class FakeSqlEngine(SqlEngine):
    env_prefix: str = "FAKE_DB_"
    name: Optional[str] = "fake_name"
    user: Optional[str] = "fake_user"
    password: Optional[str] = "fake_password"
    host: Optional[str] = "fake_host"
    port: Optional[str] = "fake_port"

    @overrides
    async def execute_query(self, query: str, *_) -> List[tuple]:
        if query.startswith("SELECT"):
            return [
                ("42", "Stop 42", 0.0, 0.0, "A"),
                ("43", "Stop 43", 1.0, 1.0, "B"),
            ]
        else:
            raise NotImplementedError
