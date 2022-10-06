import sys
import json


def get_points_of_circuit(circuit):
    ret_link_list = []
    i = 0
    while i < len(circuit) - 1:
        pair = [circuit[i], circuit[i + 1]]
        ret_link_list.append(pair)
        i += 1
    return ret_link_list


def is_route_available(circuit, available_links, demand):
    point_pairs_of_circuit = get_points_of_circuit(circuit)
    all_elements_available = len(point_pairs_of_circuit)
    available = 0
    for link in available_links:
        for point in point_pairs_of_circuit:
            if link["points"] == point and (link['capacity'] - demand) >= 0:
                available += 1
    return available == all_elements_available


def find_route(demand, possible_circuits, available_links):
    start_point = demand["end-points"][0]
    finish_point = demand["end-points"][1]
    ret = []
    for circuit in possible_circuits:
        if circuit[0] == start_point and circuit[len(circuit) - 1] == finish_point:
            if is_route_available(circuit, available_links, demand["demand"]):
                return circuit
    return ret


def update_available_links(demand, available_links, unavailable_links):
    point_pairs_of_circuit = get_points_of_circuit(demand["route_found"])
    rem_at_the_end = []
    for link in available_links:
        for point in point_pairs_of_circuit:
            if point == link["points"]:
                rem_at_the_end.append(link)
                link['capacity'] -= demand["demand"]
                unavailable_links.append(link)
    for link in rem_at_the_end:
        available_links.remove(link)


def update_unavailable_links(demand, available_links, unavailable_links):
    point_pairs_of_circuit = get_points_of_circuit(demand['route_found'])
    rem_at_the_end = []
    for link in unavailable_links:
        for point in point_pairs_of_circuit:
            if point == link["points"]:
                rem_at_the_end.append(link)
                link['capacity'] += demand["demand"]
                available_links.append(link)
    for link in rem_at_the_end:
        unavailable_links.remove(link)


with open(sys.argv[1], "r") as read_file:
    data = json.load(read_file)

endpoints = data["end-points"]
switches = data["switches"]
links = data["links"]
possible_circuits = data["possible-circuits"]
duration = data["simulation"]["duration"]
demands = data["simulation"]["demands"]

available_links = []
for link in links:
    available_links.append(link)
unavailable_links = []
live_demands = []
demands_to_remove = []

time = 1
log_line_number = 1

# Define constants
demand_reservation = "igény foglalás"
demand_release = "igény felszabadítás"
fail = "sikertelen"
success = "sikeres"
event = ""
outcome = ""

# Start simulation:
while time != duration:
    if live_demands:
        rem_at_the_end = []
        for demand in live_demands:
            if demand['end-time'] == time:
                outcome = success
                event = demand_release
                print(
                    str(log_line_number) + ". " + event + ": " + demand["end-points"][0] + "<->" + demand["end-points"][
                        1] + " st:" + str(time) + " - " + outcome)
                update_unavailable_links(demand, available_links, unavailable_links)
                log_line_number += 1
                rem_at_the_end.append(demand)
        for demand in rem_at_the_end:
            live_demands.remove(demand)
    for demand in demands:
        if demand["start-time"] == time:
            route_found = find_route(demand, possible_circuits, available_links)
            if not route_found:
                outcome = fail
                event = demand_reservation
            else:
                outcome = success
                event = demand_reservation
                demand['route_found'] = route_found
                update_available_links(demand, available_links, unavailable_links)
                live_demands.append(demand)
            print(str(log_line_number) + ". " + event + ": " + demand["end-points"][0] + "<->" + demand["end-points"][
                1] + " st:" + str(time) + " - " + outcome)
            log_line_number += 1
    time += 1
