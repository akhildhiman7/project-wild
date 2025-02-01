from service.SchedulingService import SchedulingService
from models.WildFireData import WildFireData

wildFireList = []

def read_csv(file_path):
    import csv
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            wildFireList.append(WildFireData(row['timestamp'], row['fire_start_time'], row['location'], row['severity']))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_csv('./resource/current_wildfiredata.csv')

    service_response = SchedulingService(wildFireList).orchestrate_wild_fires()
    print(service_response.get_report())
