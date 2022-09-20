import json


def how_many_points_i_need():
    with open("points.json", "r") as read_file:
        data = json.load(read_file)
        max_points = data["socketPont"]["max"] + data["zhPont"]["max"] + data["mininetPont"]["max"]
        current_points = data["socketPont"]["elert"] + data["zhPont"]["elert"]
        grading = {
            5: round(max_points * 0.85),
            4: round(max_points * 0.75),
            3: round(max_points * 0.6),
            2: round(max_points * 0.5)
        }
        if max_points > current_points >= grading[5]:
            current_grade = 5
        elif grading[5] - 1 > current_points >= grading[4]:
            current_grade = 4
        elif grading[4] - 1 > current_points >= grading[3]:
            current_grade = 3
        elif grading[3]-1 > current_points >= grading[2]:
            current_grade = 2
        else:
            current_grade = 1
