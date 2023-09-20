settings = {

    # General Settings:
    "bandwidth": 180e3,
    "frequency": 2600e6,
    "slot_duration_in_seconds": 0.5e-3,
    "number_of_slots": 10,
    "resource_blocks_per_slot": 3,
    "tx_power": 40,

    # Proportional Fair:
    "ewma_time_constant": 20,
    "starvation_threshold": 5,

    # Scenarios:
    "scenarios": {
        "scenario_1": {
            "base_stations": [
                {"mode": "FIXED", "x": 31, "y": 9}
            ],
            "user_equipments": [
                {"mode": "FIXED", "x": 0, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 20, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 40, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 60, "y": 0, "number_of_ues": 1}
            ],
            "capacity_calculator": "RoundRobinCapacityCalculator"
        },
        "scenario_2": {
            "base_stations": [
                {"mode": "FIXED", "x": 31, "y": 9}
            ],
            "user_equipments": [
                {"mode": "FIXED", "x": 0, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 20, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 40, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 60, "y": 0, "number_of_ues": 1}
            ],
            "capacity_calculator": "ProportionalFairCapacityCalculator"
        },
        "scenario_3": {
            "base_stations": [
                {"mode": "FIXED", "x": 10, "y": 20},
                {"mode": "FIXED", "x": 50, "y": 20}
            ],
            "user_equipments": [
                {"mode": "FIXED", "x": 0, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 20, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 40, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 60, "y": 0, "number_of_ues": 1}
            ],
            "capacity_calculator": "RoundRobinCapacityCalculator"
        },
        "scenario_4": {
            "base_stations": [
                {"mode": "FIXED", "x": 10, "y": 20},
                {"mode": "FIXED", "x": 50, "y": 20}
            ],
            "user_equipments": [
                {"mode": "FIXED", "x": 0, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 20, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 40, "y": 0, "number_of_ues": 1},
                {"mode": "FIXED", "x": 60, "y": 0, "number_of_ues": 1}
            ],
            "capacity_calculator": "ProportionalFairCapacityCalculator"
        },
        "scenario_5": {
            "base_stations": [
                {"mode": "FIXED", "x": 10, "y": 20},
                {"mode": "FIXED", "x": 50, "y": 20}
            ],
            "user_equipments": {
                "mode": "RANDOM",
                "upper_x_bound": 90,
                "upper_y_bound": 50,
                "number_of_ues": 100
            },
            "capacity_calculator": "RoundRobinCapacityCalculator"
        },
        "scenario_6": {
            "base_stations": [
                {"mode": "FIXED", "x": 10, "y": 20},
                {"mode": "FIXED", "x": 50, "y": 20}
            ],
            "user_equipments": {
                "mode": "RANDOM",
                "upper_x_bound": 90,
                "upper_y_bound": 50,
                "number_of_ues": 100
            },
            "capacity_calculator": "ProportionalFairCapacityCalculator"
        }
    }
}
