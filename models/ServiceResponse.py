from models.constants import LOW, MEDIUM, HIGH
import json

class ServiceResponse:
    def __init__(self):
        self.firesAddressed = 0
        self.firesDelayed = 0
        self.operationalCosts = 0
        self.damageCosts = 0
        self.severityReport = {LOW: 0, MEDIUM: 0, HIGH: 0}
        self.severityCoordinates = {True:{LOW:[], MEDIUM:[], HIGH:[]},
                                    False:{LOW:[], MEDIUM:[], HIGH:[]}}

    def address_fire(self):
        self.firesAddressed += 1

    def delay_fire(self):
        self.firesDelayed += 1

    def add_operational_cost(self, cost):
        self.operationalCosts += cost

    def add_damage_cost(self, sev):
        if sev == HIGH:
            self.damageCosts += 200000
        elif sev == MEDIUM:
            self.damageCosts += 100000
        else:
            self.damageCosts += 50000

    def add_incident(self, resource_cost, sev, resolved,coordinates):
        self.severityReport[sev] += 1

        if not resolved:
            self.add_damage_cost(sev)
            self.delay_fire()
            self.severityCoordinates[False][sev].append(coordinates)
        else:
            self.address_fire()
            self.add_operational_cost(resource_cost)
            self.severityCoordinates[True][sev].append(coordinates)

    def get_report(self):
        """
            Print a detailed report containing:
            - Number of fires addressed
            - Number of fires delayed
            - Total operational costs
            - Estimated damage costs from delayed responses
            - Fire severity report
            """
        report_data = {
            "Number_of_fires_addressed": self.firesAddressed,
            "Number_of_fires_delayed": self.firesDelayed,
            "Total_operational_costs": self.operationalCosts,
            "Estimated_damage_costs_from_delayed_responses": self.damageCosts,
            "Fire_severity_report": self.severityReport,
            "Coordinates": self.severityCoordinates
        }

        # report_json = json.dumps(report_data)
        return report_data
