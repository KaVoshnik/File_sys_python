import argparse

class DataAnalyzer:
    def __init__(self, input_file, output_path='./', file_prefix='', append_mode=False, stats_type='s'):
        self.input_file = input_file
        self.output_path = output_path
        self.file_prefix = file_prefix
        self.append_mode = append_mode
        self.stats_type = stats_type
        self.integers_data = []
        self.floats_data = []
        self.strings_data = []

    def parse_data(self):
        with open(self.input_file, 'r') as file:
            for line in file:
                line = line.strip()
                try:
                    number = int(line)
                    self.integers_data.append(number)
                except ValueError:
                    try:
                        number = float(line)
                        self.floats_data.append(number)
                    except ValueError:
                        self.strings_data.append(line)

    def statistic(self):
        if self.stats_type == 'f':
            if len(self.integers_data) > 0:
                print(f"Integers - Count: {len(self.integers_data)}, Min: {min(self.integers_data)}, Max: {max(self.integers_data)}, Sum: {sum(self.integers_data)}, Avg: {sum(self.integers_data) / len(self.integers_data)}")
            if len(self.floats_data) > 0:
                print(f"Floats - Count: {len(self.floats_data)}, Min: {min(self.floats_data)}, Max: {max(self.floats_data)}, Sum: {sum(self.floats_data):.2f}, Avg: {sum(self.floats_data) / len(self.floats_data):.2f}")
        elif self.stats_type == 's':
            print(f"Integers - Count: {len(self.integers_data)}")
            print(f"Floats - Count: {len(self.floats_data)}")
            print(f"Strings - Count: {len(self.strings_data)}")

    def save_to_files(self):
        if_has = [int(bool(self.integers_data)), int(bool(self.floats_data)), int(bool(self.strings_data))]

        with open(f'{self.output_path}/output/{self.file_prefix}integers.txt', 'a' if self.append_mode else 'w') as integers_output:
            for number in self.integers_data:
                integers_output.write(f'{number} ')

        with open(f'{self.output_path}/output/{self.file_prefix}floats.txt', 'a' if self.append_mode else 'w') as floats_output:
            for number in self.floats_data:
                floats_output.write(f'{number} ')

        with open(f'{self.output_path}/output/{self.file_prefix}strings.txt', 'a' if self.append_mode else 'w') as strings_output:
            for string in self.strings_data:
                strings_output.write(f'{string} ')

    def analyze_data(self):
        self.parse_data()
        self.save_to_files()
        self.statistic()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Путь к входному файлу')
    parser.add_argument('-o', '--output_path', help='Путь для сохранения результатов', default='./')
    parser.add_argument('-p', '--file_prefix', help='Префикс имен выходных файлов', default='')
    parser.add_argument('-a', '--append_mode', action='store_true', help='Режим добавления в существующие файлы')
    parser.add_argument('-s', '--stats_type', choices=['f', 's'], default='s', help='Тип статистики: краткая (s) или полная (f)')

    try:
        args = parser.parse_args()
        data_analyzer = DataAnalyzer(args.input_file, args.output_path, args.file_prefix, args.append_mode, args.stats_type)
        data_analyzer.analyze_data()
    except Exception as e:
        print(f'Произошла ошибка: {e}')
