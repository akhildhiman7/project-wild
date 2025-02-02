class Resource:
    def __init__(self, deployment_time, cost_per_operation, available_units):
        self.deployment_time = deployment_time
        self.cost_per_operation = cost_per_operation
        self.available_units = available_units

class SmokeJumpers(Resource):
    def __init__(self, deployment_time, cost_per_operation, available_units):
        super().__init__(deployment_time, cost_per_operation, available_units)
        self.name = "Smoke_Jumpers"

class FireEngines(Resource):
    def __init__(self, deployment_time, cost_per_operation, available_units):
        super().__init__(deployment_time, cost_per_operation, available_units)
        self.name = "Fire_Engines"

class Helicopters(Resource):
    def __init__(self, deployment_time, cost_per_operation, available_units):
        super().__init__(deployment_time, cost_per_operation, available_units)
        self.name = "Helicopters"

class TankerPlanes(Resource):
    def __init__(self, deployment_time, cost_per_operation, available_units):
        super().__init__(deployment_time, cost_per_operation, available_units)
        self.name = "Tanker_Planes"

class GroundCrews(Resource):
    def __init__(self, deployment_time, cost_per_operation, available_units):
        super().__init__(deployment_time, cost_per_operation, available_units)
        self.name = "Ground_Crews"