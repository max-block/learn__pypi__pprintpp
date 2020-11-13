from dataclasses import dataclass
from datetime import datetime

import pprintpp


@dataclass
class Data:
    name: str
    value: int
    tags: list[str]
    created_at: datetime


d = Data("v1", 3342, ["a", "b", "c", "d"], datetime.now())

pprintpp.pprint(d)
