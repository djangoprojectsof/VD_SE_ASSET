from typing import List, Dict, Callable, Any


def aggregate_data(data: List[Dict[str, Any]], key: str, aggregator: Callable) -> Dict[str, Any]:
    grouped_data = {}

    for entry in data:
        key_value = entry.get(key)

        if key_value not in grouped_data:
            grouped_data[key_value] = []
        grouped_data[key_value].append(entry)

    aggregated_results = {}
    for k, group in grouped_data.items():
        aggregated_results[k] = aggregator(group)

    return aggregated_results

def sum_values(group: List[Dict[str, Any]], value_key: str) -> float:
    return sum(entry[value_key] for entry in group if value_key in entry)

data = [
    {'category': 'A', 'value': 10},
    {'category': 'B', 'value': 20},
    {'category': 'A', 'value': 15},
    {'category': 'B', 'value': 25}
]
result = aggregate_data(data, 'category', lambda group: sum_values(group, 'value'))
print(result)
