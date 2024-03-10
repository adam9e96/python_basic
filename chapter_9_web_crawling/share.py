import csv
def save_csv(file_path: str, dict_list: list[dict]) -> None:
    with open(f'./output/{file_path}', 'wt', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=dict_list[0].keys())
        csv_writer.writeheader()
        for item in dict_list:
            csv_writer.writerow(item)
    print(f'{file_path}이 저장되었습니다.')