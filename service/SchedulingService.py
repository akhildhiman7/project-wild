from datetime import datetime
from typing import List

# from main import sort_wildfire_data
from models.FireDepartment import FireDepartment
from models.ServiceResponse import ServiceResponse
from models.constants import severity_priority
from models.WildFireData import WildFireData
from datetime import datetime


class SchedulingService:
    def __init__(self, wildFireDataList):
        self.fire_department = FireDepartment()
        self.wildFireData = self.sort_wildfire_data(wildFireDataList)
        self.response = ServiceResponse()

    def orchestrate_wild_fires(self) -> ServiceResponse:
        wild_fire_index = 0

        while wild_fire_index < len(self.wildFireData):
            resource = self.fire_department.get_optimal_resource()
            if not resource:
                break

            sev = self.wildFireData[wild_fire_index].severity
            location = self.wildFireData[wild_fire_index].location.split(",")
            

            self.response.add_incident(resource.cost_per_operation, sev, True,location)

            wild_fire_index += 1

        while wild_fire_index < len(self.wildFireData):
            self.response.add_incident(0, self.wildFireData[wild_fire_index].severity, 
                                       False,self.wildFireData[wild_fire_index].location.split(","))
            wild_fire_index += 1

        self.response.get_resource_count(self.fire_department)
        return self.response

    def sort_wildfire_data(self, wildfire_list) -> List[WildFireData]:
        return sorted(
            wildfire_list,
            key=lambda wf: (
                -severity_priority[wf.severity],  # Sort by severity (descending order)
                datetime.strptime(wf.fire_start_time, '%Y-%m-%d %H:%M:%S'),  # Sort by fire_start_time (ascending order)
                datetime.strptime(wf.timestamp, '%Y-%m-%d %H:%M:%S')  # Sort by timestamp (ascending order)
            )
        )


