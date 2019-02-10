#!/usr/bin/env python


import math
import argparse
import numpy

#city: list[hospital,%Accurate Prenatal Care]
city_to_hospital_dict = {
    "Newburyport": [("Anna Jaques Hospital",84.4)],
    "Greenfield" : [("Baystate Franklin Medical Center", 85.3)],
    "Ware": [("Baystate Mary Lane Hospital",80.7)],
    "Springfield": [("Baystate Medical Center",78.1),("Mercy Medical Center", 79.8)],
    "Pittsfield":[("Berkshire Medical Center",66.0)],
    "Boston":[("Beth Israel Deaconess Medical Center",86.1),("Tufts Medical Center",89.0),("Massachusetts General Hospital",89.2),("Boston Medical Center", 69.6),("Brigham and Women's Hospital",95.1),("Caritas St. Elizabeth's Medical Center of Boston", 62.5)],
    "Beverly":[("Beverly Hospital",92.4),("North Shore Birth Center", 96.2)],
    "Brockton":[("Brockton Hospital",79.4),("Caritas Good Samaritan Medical Center",63.7)],
    "Cambridge":[("Cambridge Hospital",79.4),("Cambridge Birth Center",76.1), ("Mount Auburn Hospital", 88.7)],
    "Barnstable":[("Cape Cod Hospital",78.9)],
    "Methuen":[("Caritas Holy Family Hospital and Medical Center", 78.4)],
    "Norwood":[("Caritas Norwood Hospital", 58.3)],
    "Fall River":[("Charlton Memorial Hospital" ,88.1)],
    "Northampton":[("Cooley Dickinson Hospital", 93.3)],
    "Concord":[("Emerson Hospital",84.1)],
    "Great Barrington":[("Fairview Hospital", 87.9)],
    "Falmouth":[("Falmouth Hospital",87.9)],
    "Southbridge":[("Harrington Memorial Hospital",90.0)],
    "Garner":[("Heywood Memorial Hospital", 80.6)],
    "Holyoke":[("Holyoke Hospital",74.2)],
    "Plymouth":[("Jordan Hospital", 86.1)],
    "Lawrence":[("Lawrence General Hospital", 76.8)],
    "Leominister":[("Leominister Hospital", 85.0)],
    "Lowell":[("Lowell General Hospital", 82.2)],
    "Oak Bluffs":[("Martha's Vineyard Hospital", 95.3)],
    "Melrose":[("Melrose-Wakefield Hospital", 90.1)],
    "Framingham":[("Metrowest Medical Center-Framingham Union Campus",94.2)],
    "Milford":[("Milford Regional Medical Center",94.2)],
    "Taunton":[("Morton Hospital",71.1)],
    "Nantucket":[("Nantucket Cottage Hospital",71.9)],
    "Newton":[("Newton Wellesley Hospital",89.3)],
    "North Adams":[("North Adams Regional Hospital", 90.8)],
    "Salem":[("North Shore Medical Center - Salem Hospital", 84.6)],
    "Worcester":[("Saint Vincent Hospital",86.9),("UMass Memorial Center", 71.7)],
    "Weymouth":[("South Shore Hospital",93.8)],
    "New Bedford":[("St.Luke's Hospital",74.9)],
    "Attleboro":[("Sturdy Memorial Hospital",84.2)],
    "Wareham":[("Tobey Hospital",85.9)],
    "Winchester":[("Wincester Hospital",86.7)]
}

city_to_infant_mortality_rate = {
    "Attleboro":3.0,
    "Barnstable":6.7,
    "Boston":6.7,
    "Brockton":8.0,
    "Brookline":0.0,
    "Cambridge":3.5,
    "Chicopee":5.3,
    "Fall River":8.2,
    "Framingham":3.3,
    "Haverhill":4.4,
    "Lawrence":6.2,
    "Leominister":3.2,
    "Lowell":6.9,
    "Lynn":5.9,
    "Malden":3.9,
    "Medford":2.4,
    "Methuen":2.9,
    "New Bedford":7.7,
    "Newton":2.0,
    "Peabody":5.3,
    "Pittsfield":5.0,
    "Plymouth":0.0,
    "Quincy":4.8,
    "Revere":5.3,
    "Somerville":6.2,
    "Springfield":8.3,
    "Taunton":8.1,
    "Waltham":2.1,
    "Weymouth":2.5,
    "Worcester":8.8
}

#1991-2009
race_to_infant_mortality_rate = {
    "White":[5.5,5.5,5.3,5.3,4.4,4.7,4.8,4.6,4.7,3.8,4.1,4.1,4.1,3.8,4.3,4.2,3.9,3.7,4.1],
    "Black":[15.0,16.4,13.1,12.6,11.1,11.4,11.7,10.6,12.3,12.8,12.1,11.6,12.7,11.5,9.4,11.1,10.2,11.7,7.6],
    "Hispanic":[9.4,7.9,9.3,7.6,7.2,5.1,6.7,6.7,5.5,5.2,7.3,7.0,5.6,7.6,7.7,5.8,7.4,7.9,7.1],
    "Asian" : [4.2,4.9,3.9,2.4,5.5,2.2,2.6,2.7,1.9,4.1,3.1,3.0,2.7,2.7,3.4,1.8,3.1,2.7,3.2]
}

#white,black,hispanic,asian
city_to_races = {
    "Attleboro":[78.1,3.2,7.1,11.1],
    "Barnstable":[82.0,4.3,7.0,11.1],
    "Boston":[40.5,27.6,22.0,9.9],
    "Brockton":[32.8,53.0,9.7,4.3],
    "Brookline":[70.0,2.1,4.6,23.1],
    "Cambridge":[54.7,14.6,7.0,23.4],
    "Chicopee":[68.9,4.2,23.8,3.0],
    "Fall River":[77.6,6.0,11.1,5.3],
    "Framingham":[64.7,8.0,17.2,10.0],
    "Haverhill":[71.7,3.2,20.3,4.2],
    "Lawrence":[13.2,2.7,81.3,2.7],
    "Leominister":[68.0,5.3,20.1,6.6],
    "Lowell":[43.0,7.6,19.8,29.4],
    "Lynn":[32.2,14.8,42.7,9.9],
    "Malden":[45.8,18.3,8.2,27.6],
    "Medford":[69.6,12.7,5.1,12.4],
    "Methuen":[63.1,2.3,27.0,7.3],
    "New Bedford":[59.2,12.0,25.0,3.7],
    "Newton":[73.4,2.9,4.7,18.9],
    "Peabody":[81.1,2.9,4.7,18.9],
    "Pittsfield":[79.7,6.8,7.1,6.0],
    "Plymouth":[92.8,2.1,2.2,2.9],
    "Quincy":[55.0,7.2,5.5,32.1],
    "Revere":[50.0,5.1,34.0, 11.0],
    "Somerville":[58.8,8.8,16.9,15.0],
    "Springfield":[23.2,20.2,51.7,4.8],
    "Taunton":[79.6,9.0,6.9,4.2],
    "Waltham":[51.9,8.3,20.4,19.1],
    "Weymouth":[82.5,5.9,2.9,8.7],
    "Worcester":[59.0,14.4,18.9,7.7]
}


city_lat_long = {
    "Attleboro":[41.944538,-71.284088],
    "Barnstable":[41.677690,-70.359280],
    "Boston":[42.360081,-71.058884],
    "Brockton":[42.083431,-71.018379],
    "Brookline":[42.333672,-71.120880],
    "Cambridge":[42.373615,-71.109734],
    "Chicopee":[42.148331,-72.606956],
    "Fall River":[41.701031,-71.155388],
    "Framingham":[42.281559,-71.418831],
    "Haverhill":[42.777431,-71.077332],
    "Lawrence":[42.707035,-71.163116],
    "Leominister":[42.525860,-71.760130],
    "Lowell":[42.633427,-71.316170],
    "Lynn":[42.464409,-70.948509],
    "Malden":[42.426498,-71.073547],
    "Medford":[42.418560,-71.106453],
    "Methuen":[42.729851,-71.183983],
    "New Bedford":[41.634048,-70.927658],
    "Newton":[42.338032,-71.211578],
    "Peabody":[42.534599,-70.928757],
    "Pittsfield":[42.445030,-73.252800],
    "Plymouth":[41.955750,-70.664391],
    "Quincy":[42.252876,-71.002274],
    "Revere":[42.409969,-71.012398],
    "Somerville":[42.389118,-71.097153],
    "Springfield":[42.102051,-72.585762],
    "Taunton":[41.901680,-71.092651],
    "Waltham":[42.376171,-71.238991],
    "Weymouth":[42.217529,-70.936897],
    "Worcester":[42.262119,-71.802238]
}


def distance(origin, destination):
    lat1 = origin[0]
    lon1 = origin[1]
    lat2 = destination[0]
    lon2 = destination[1]
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type=str)
    parser.add_argument('--race', type=str)
    args = parser.parse_args()


    if city_to_infant_mortality_rate.get(args.city) > numpy.mean(race_to_infant_mortality_rate.get(args.race)):

        orig_city = city_lat_long.get(args.city)
        city_list = []
        distance_list = []
        for city in city_lat_long.keys():
            if city is not args.city:

                dest_city = city_lat_long.get(city)
                city_list.append(city)

                distance_list.append(distance(orig_city,dest_city))
        delete = city_list.index(args.city)
        city_list.remove(args.city)
        del distance_list[delete]
        best_city = city_list[distance_list.index(min(distance_list))]
        print("1")
        list_of_hospitals = city_to_hospital_dict.get(best_city)
        hospital_list = []
        score_list = []
        if len(list_of_hospitals) > 1:
            for hospital in list_of_hospitals:
                hospital_list.append(hospital[0])
                score_list.append(hospital[1])
            best_hospital = hospital_list[score_list.index(max(score_list))]
            print(1.2)
            print(best_hospital)
        else:
            print(1.3)
            print(list_of_hospitals[0])
    else:
        list_of_hospitals = city_to_hospital_dict.get(args.city)
        hospital_list = []
        score_list = []
        if len(list_of_hospitals) > 1:
            for hospital in list_of_hospitals:
                hospital_list.append(hospital[0])
                score_list.append(hospital[1])
            best_hospital = hospital_list[score_list.index(max(score_list))]
            print(2)
            print(best_hospital)
        else:
            print(3)
            print(list_of_hospitals[0])

if __name__ == '__main__':
     main()
