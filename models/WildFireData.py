class WildFireData:
    def __init__(self, timestamp, fire_start_time, location, severity):
        self.timestamp = timestamp
        self.fire_start_time = fire_start_time
        self.location = location
        self.severity = severity

    def __repr__(self):
        return (f"{self.__class__.__name__}(timestamp={self.timestamp}, "
                f"fire_start_time={self.fire_start_time}, location={self.location}, severity={self.severity})")