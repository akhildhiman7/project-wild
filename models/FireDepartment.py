from models.Resource import SmokeJumpers, FireEngines, Helicopters, TankerPlanes, GroundCrews, Resource
from heapq import heapify, heappush, heappop

class FireDepartment:
    def __init__(self):
        self.SmokeJumpers = SmokeJumpers(30, 5000, 5)
        self.FireEngines = FireEngines(60, 2000, 10)
        self.Helicopters = Helicopters(45, 8000, 3)
        self.TankerPlanes = TankerPlanes(120, 15000, 2)
        self.GroundCrews = GroundCrews(90, 3000, 8)
        self.resources = [self.SmokeJumpers, self.FireEngines, self.Helicopters, self.TankerPlanes, self.GroundCrews]
        self.costSoFar = 0
        self.resourcesAvailable = True
        self.resource_heap = self.create_resource_heap()

    def get_costs_accumulated(self):
        return self.costSoFar

    def resources_available(self):
        return self.resourcesAvailable

    def get_optimal_resource(self) -> Resource:
        """
                Fetches the optimal resource based on the following rules:
                - Select resource with the lowest cost_per_operation.
                - Reduce the available_units of the selected resource.
                - If the units for a resource become 0, remove it from consideration.
                - Update cost and resources available status.
                """
        while self.resource_heap:  # While the priority queue is not empty
            _, _, resource = heappop(self.resource_heap)  # Pop the resource with the lowest cost_per_operation
            if resource.available_units > 0:
                # Deduct one unit
                resource.available_units -= 1

                # Add the cost of operation
                self.costSoFar += resource.cost_per_operation

                # If units are still remaining, re-add the resource to the heap
                if resource.available_units > 0:
                    heappush(self.resource_heap, (resource.cost_per_operation, resource.deployment_time, resource))

                return resource  # Return the allocated resource

        # If all resources are exhausted, update the status
        self.resourcesAvailable = False
        return None  # No resources available

    def create_resource_heap(self):
        heap = []
        for resource in self.resources:
            heappush(heap,
                     (resource.cost_per_operation, resource.deployment_time, resource))  # Push tuple with cost priority
        return heap

