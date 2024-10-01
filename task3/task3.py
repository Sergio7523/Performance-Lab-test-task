import json


def get_value(item_id, values_dict):
    return values_dict.get(item_id, None)


def fill_values(tests, values_dict):
    for test in tests:
        test_id = test['id']
        test['value'] = get_value(test_id, values_dict)
        if 'values' in test:
            fill_values(test['values'], values_dict)


def create_report(values_file, tests_file, report_file):
    with open(values_file, mode='r', encoding='utf-8') as vf:
        values = json.load(vf)
    values_dict = {item['id']: item['value'] for item in values['values']}

    with open(tests_file, mode='r', encoding='utf-8') as tf:
        tests = json.load(tf)
    fill_values(tests['tests'], values_dict)
    report_data = {'tests': tests['tests']}

    with open(report_file, mode='w', encoding='utf-8') as rf:
        json.dump(report_data, rf, indent=2)


if __name__ == '__main__':
    values_path, tests_path, report_path = [input() for _ in range(3)]
    create_report(values_path, tests_path, report_path)
