import json
import requests
import pandas as pd
from datetime import datetime

URL = "https://data.sfgov.org/api/views/rqzj-sfat/rows.csv"

# data structure to add/update Trucks in the DB
# if this is something a user can do, we would want to validate their input
# i.e. Lat/Lon match address, enums are drop-down menu items
# Some of these don't need to be class items, since they are derived from other class items
# so the fields can be filled in as we add the Truck
class Truck:
    def __init__(self, applicant, facility, block, lot):
        self.locationid = 0
        self.Applicant = applicant
        self.FacilityType = facility  # can be Push Cart
        self.cnn = 0  # don't know what this stands for, so I'd want more data from customer to validate this field
        self.LocationDescription = ""
        self.Address = ""
        self.blocklot = block + lot  # block + lot
        self.block = block
        self.lot = lot
        self.permit = "00MFF-0000"
        self.Status = "REQUESTED"  # APPROVED, EXPIRED, REQUESTED
        self.FoodItems = ""
        self.X = 0
        self.Y = 0
        self.Latitude = 0
        self.Longitude = 0
        self.Schedule = ""  # link
        self.dayshours = ""  # opening times
        self.NOISent = ""
        self.Approved = datetime.now()  # timestamp
        self.Received = 0  # YYYYMMDD
        self.PriorPermit = 0  # count
        self.ExpirationDate = datetime.now()  #
        self.Location = (0, 0)  # lat, lon
        self.Fire_Prevention_Districts = 0
        self.Police_Districts = 0
        self.Supervisor_Districts = 0
        self.Zip_Codes = 0
        self.Neighborhoods = 0

    def convert_to_json(self):
        return {
            "locationid": self.locationid,
            "Applicant": self.Applicant,
            "FacilityType": self.FacilityType,
            "cnn": self.cnn,
            "LocationDescription": self.LocationDescription,
            "Address": self.Address,
            "blocklot": self.blocklot,
            "block": self.block,
            "lot": self.lot,
            "permit": self.permit,
            "Status": self.Status,
            "FoodItems": self.FoodItems,
            "X": self.X,
            "Y": self.Y,
            "Latitude": self.Latitude,
            "Longitude": self.Longitude,
            "Schedule": self.Schedule,
            "dayshours": self.dayshours,
            "NOISent": self.NOISent,
            "Approved": self.Approved,
            "Received": self.Received,
            "PriorPermit": self.PriorPermit,
            "ExpirationDate": self.ExpirationDate,
            "Location": "(" + str(self.Latitude) + ", " + str(self.Longitude) + ")",
            "Fire Prevention Districts": self.Fire_Prevention_Districts,
            "Police Districts": self.Police_Districts,
            "Supervisor Districts": self.Supervisor_Districts,
            "Zip Codes": self.Zip_Codes,
            "Neighborhoods (old)": self.Neighborhoods
    }


# Made this a class so that I don't have to keep passing "trucks" DF into functions
class FoodTruckAPI:
    def __init__(self):
        # using Pandas allows for reading from local csv or URL -> can update to take in 'file' as input
        self.trucks = pd.read_csv(URL)  # could use requests.get(url) to get the JSON

        """
        can convert to JSON if that is easier for REST
        trucks_json = trucks.to_json(orient="index")
        parsed = json.loads(trucks_json)
        print(json.dumps(parsed, indent=4))
        """

    # Add a new food truck.
    def add_truck(self, truck):
        # turn truck object into JSON

        response = requests.post(URL, truck.convert_to_json())
        return response.status_code  # to check that it worked

    # Retrieve a food truck based on the locationid field.
    # need to know what to return if the locationID is invalid
    # for now should check that returned truck object is not null before doing anything with it
    def retrieve_truck(self, locationID):
        new_truck = None
        for t in self.trucks.iterrows():
            if t[1]["locationid"] == locationID:
                # fill in new Truck object here
                new_truck = Truck(t[1]["Applicant"], t[1]["FacilityType"], t[1]["block"], t[1]["lot"])
        return new_truck

    # Get all food trucks for a given block.
    # should clarify what this should return
    # for now making it a list Truck data objects
    def get_all_trucks(self, block):
        trucks_list = []
        for t in self.trucks.iterrows():
            if t[1]["block"] == block:
                # no need to repeat the code of turning the dataframe element into a Truck object
                trucks_list.append(self.retrieve_truck(t[1]["locationid"]))
        return trucks_list  # can check if empty after


# main func for testing purposes --> not sure how something like this looks when actually interfacing with Internet
if __name__ == "__main__":
    api = FoodTruckAPI()

    t1 = Truck("Heather's Habanero Hut", "Truck", "0029", "007")
    api.add_truck(t1)

    # uses the retrieve truck function, but I assume the API should make retrieve truck public for use
    trucks_list = api.get_all_trucks("0029")
