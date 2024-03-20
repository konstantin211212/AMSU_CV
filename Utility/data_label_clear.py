import os
import sys
import yaml


def search_list_object_yaml(path):
    list_yaml = []
    num_item = 1
    global configure_yaml
    global path_work
    for i in os.listdir(path):
        if i.endswith(".yaml"):
            list_yaml.append(i)
            print("Найден файл .yaml : ", num_item, i)
            num_item += 1

    if not list_yaml:
        print("Файлов конфигурации не найдено!")
        answer = input("Изменить путь до папки? y|n : ")
        if answer.lower() in "yesда":
            path_work = input("Укажите полный путь до рабочего каталога: ")
            print("Перезапуск поиска списка классов...")
            search_list_object_yaml(path_work)
        else:
            print("Программа завершила работу")
            return False

    if len(list_yaml) > 1:
        num_item_work = int(input("Введите номер файла для редактирования: "))
        while True:
            if 0 < num_item_work <= len(list_yaml):
                print("Выбран файл :", list_yaml[num_item_work - 1])
                configure_yaml = list_yaml[num_item_work - 1]
                return True
            else:
                print("Номер некорректен - повторите попытку...")
                num_item_work = int(input("Введите номер файла для редактирования: "))
    elif len(list_yaml) == 1:
        print("Выбран файл :", list_yaml[0])
        configure_yaml = list_yaml[0]
        return True


def read_and_modify_one_block_of_yaml_data(filename, write_file, key, value):
    with open(f'{filename}', 'r') as f:
        data = yaml.safe_load(f)
        for i, j in enumerate(data[f'{key}']):
            print(i, j)

        print("Введите через пробел номера классов - которые нужно УДАЛИТЬ из датасета")
        num_for_delete = list(map(lambda x: int(x), input().split()))
        new_item_list = []
        for i, j in enumerate(data[f'{key}']):
            if i not in num_for_delete:
                new_item_list.append(j)
        print(data)
        data[f'{key}'] = f'{new_item_list}'
        #daa[f'{key}'] = f'{value}'

        print(data)
    with open(f'{write_file}', 'w') as file:
        yaml.dump(data,file,sort_keys=False)
    print('done!')

configure_yaml = ""
path_work = os.getcwd()

print("Внимание! Скрипт работает с директорией: ")
print(path_work)

search_list_object_yaml(path_work)
final_path_yaml = os.path.join(path_work, configure_yaml)

read_and_modify_one_block_of_yaml_data(final_path_yaml,
                                       os.path.join(path_work, "new_" + configure_yaml),
                                       key='names', value=["None"])


for file in os.listdir(path_work + "\\train\labels\\"):
    if file.endswith(".txt"):
        with open(path_work + "\\train\labels\\" + file, "r+", encoding="UTF-8") as label_file:
            text = label_file.readlines()
            #print(text)
            new_text = []
            # классы указываются пока вручную в коде
            list_num_remove = tuple("2 5 7".split())
            if text:
                for line in text:
                    if not line.startswith(list_num_remove):
                        #print(line)
                        new_text.append(line)
                label_file.seek(0)
                label_file.truncate(0)
                label_file.writelines(new_text)
                # разметка классов перезаписывается без указанных в list_num_remove классов
            label_file.close()
