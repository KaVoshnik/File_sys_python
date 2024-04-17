import argparse

def sort_data_by_type(input_file, output_path, file_prefix):
    integers_output = open(f'{output_path}/{file_prefix}integers.txt', 'w')
    floats_output = open(f'{output_path}/{file_prefix}floats.txt', 'w')
    strings_output = open(f'{output_path}/{file_prefix}strings.txt', 'w')

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()

            try:
                number = int(line)
                integers_output.write(f'{number} ')
            except ValueError:
                try:
                    number = float(line)
                    floats_output.write(f'{number} ')
                except ValueError:
                    strings_output.write(f'{line} ')

    integers_output.close()
    floats_output.close()
    strings_output.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Путь к входному файлу')
    parser.add_argument('-o', '--output_path', help='Путь для сохранения результатов', default='./')
    parser.add_argument('-p', '--file_prefix', help='Префикс имен выходных файлов', default='')

    try:
        args = parser.parse_args()
        sort_data_by_type(args.input_file, args.output_path, args.file_prefix)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
