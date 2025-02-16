import pyperclip, time, keyboard

# открываем файл с правильной кодировкой
try:
    with open('input.txt', encoding='utf-8') as f:
        lines = f.readlines()
except UnicodeDecodeError:
    # если utf-8 не подходит, пробуем windows-1251
    with open('input.txt', encoding='windows-1251') as f:
        lines = f.readlines()

if not lines:
    print('input.txt is empty. Exiting...')
    exit()
else:
    print('running...')
    for line in lines:
        line = line.strip()  # удаляем лишние пробелы и переносы строк
        if line:  # пропускаем пустые строки
            pyperclip.copy(line)
            print('Line copied to clipboard:', line)
            keyboard.wait('ctrl+v')  # ждем нажатия ctrl+v
            time.sleep(0.05)  # небольшой интервал между строками
    print('No more lines to copy. Exiting...')
