# Total for first-form pokemon = 100
# Total for second-form pokemon = 150
# Total for third-form pokemon = 200

# Standard Distributions for first forms:
# HP Balanced Defensive
#  health 30 (+25) (+25)
#  attack 15 (+5) (+5)
#  defense 25 (+10) (+10)
#  special_attack 5
#  special_defense 25 (+10) (+10)
#  speed   5
# A max_attack pokemon using a super-effective move that does 90 damaage (2X damage) against
# a max_hp defensive pokemon would do 91% health.
# Based on this damage calculation formula:
# ((attack * 0.7) * 2) - damage_resisted
# and damage_resisted is based on the following formula (replace defense with special defense for special attacks):
# damage_dealt - (damage_dealt / defense)

standard_stats = {
    "third_form": {
        "defensive": {
            "max_hp": {
                "hp": 100,
                "attack": 30,
                "defense": 30,
                "special_attack": 5,
                "special_defense": 30,
                "speed": 5,
            },
            "equalized_defense": {
                "hp": 54,
                "attack": 30,
                "defense": 53,
                "special_attack": 5,
                "special_defense": 53,
                "speed": 5,
            },
        },
        "offensive": {
            "max_attack": {
                "hp": 30,
                "attack": 100,
                "defense": 20,
                "special_attack": 5,
                "special_defense": 20,
                "speed": 25
            },
            "max_special": {
                "hp": 30,
                "attack": 5,
                "defense": 20,
                "special_attack": 100,
                "special_defense": 20,
                "speed": 25
            },
            "fast_physical": {
                "hp": 30,
                "attack": 80,
                "defense": 20,
                "special_attack": 5,
                "special_defense": 20,
                "speed": 45
            },
            "fast_special": {
                "hp": 30,
                "attack": 5,
                "defense": 20,
                "special_attack": 70,
                "special_defense": 20,
                "speed": 55
            },
            "fastest_physical": {
                "hp": 30,
                "attack": 70,
                "defense": 20,
                "special_attack": 5,
                "special_defense": 20,
                "speed": 55
            }
        },
        "balanced": {
            "hybrid_offense": {
                "hp": 25,
                "attack": 50,
                "defense": 20,
                "special_attack": 50,
                "special_defense": 20,
                "speed": 30
            },
        },
    }
}

pokedex = {
    "aegislash-shield": {
        "base_stats": standard_stats["third_form"]["defensive"]["equalized_defense"]
    },
    "aegislash-blade": {
        "base_stats": standard_stats["third_form"]["offensive"]["max_attack"]
    },
    "lycanroc-dusk": {
        "base_stats": standard_stats["third_form"]["offensive"]["fast_physical"]
    },
    "amoonguss": {
        "base_stats": standard_stats["third_form"]["defensive"]["equalized_defense"]
    },
    "charizard-mega-x": {
        "base_stats": standard_stats["third_form"]["offensive"]["fast_physical"]
    },
    "charizard-mega-y": {
        "base_stats": standard_stats["third_form"]["offensive"]["max_special"]
    }
}
