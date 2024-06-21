import pandas as pd


def check_csv_file(file_path):
    try:
        df = pd.read_csv(file_path, sep=',', error_bad_lines=False, warn_bad_lines=True)
        print("CSV файл успешно прочитан.")
        return df
    except pd.errors.ParserError as e:
        print("Ошибка при чтении CSV файла:", e)
        return None

def print_info(df):
    if df is not None:
        print("Информация о данных:")
        print(df.info())

        print("Первые 5 строк данных:")
        print(df.head())
    else:
        print("Данные не были загружены из-за ошибки.")

def save_cleaned_csv(df, output_path):
    if df is not None:
        df.to_csv(output_path, index=False)
        print(f"Очищенный файл сохранен как {output_path}")

# Путь к вашему CSV файлу
file_path = 'data/salary_update.csv'
output_path = 'data/salary_update_cleaned.csv'

df = check_csv_file(file_path)
print_info(df)
save_cleaned_csv(df, output_path)
