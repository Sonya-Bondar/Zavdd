import os
import json


def show_system_json():
    print("Поточна папка:", os.getcwd())

    student = {
        "name": "Sofia",
        "course": 2,
        "specialty": "IСT"
    }

    print(json.dumps(student, ensure_ascii=False, indent=4))