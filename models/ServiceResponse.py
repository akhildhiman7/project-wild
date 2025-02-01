from models.constants import LOW, MEDIUM, HIGH

class ServiceResponse:
    def __init__(self):
        self.firesAddressed = 0
        self.firesDelayed = 0
        self.operationalCosts = 0
        self.damageCosts = 0
        self.severityReport = {LOW: 0, MEDIUM: 0, HIGH: 0}

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

    def add_incident(self, resource_cost, sev, resolved):
        self.severityReport[sev] += 1

        if not resolved:
            self.add_damage_cost(sev)
            self.delay_fire()
        else:
            self.address_fire()
            self.add_operational_cost(resource_cost)

    def get_report(self):
        """
            Print a detailed report containing:
            - Number of fires addressed
            - Number of fires delayed
            - Total operational costs
            - Estimated damage costs from delayed responses
            - Fire severity report
            """
        report = (
            f"Number of fires addressed: {self.firesAddressed}\n"
            f"Number of fires delayed: {self.firesDelayed}\n"
            f"Total operational costs: ${self.operationalCosts}\n"
            f"Estimated damage costs from delayed responses: ${self.damageCosts}\n"
            f"Fire severity report: {self.severityReport}"
        )
        return report
