# python_parser
Создать скрипт проверки уровня логирования
Создать скрипт для управления конфигурационными файлами управления логами работающий в
следующих режимах:
Режим 1. Проверка уровня логирования
Требуется вывести для просмотра значения параметров, указанные в файлах
В каталоге opt/upiter/plot/task/bin/etc/config для всех файлов с маской имени "*.json" вывести
значения из
"log": {
"file": {
"level" : "значение"
}}
В каталоге opt/upiter/plot/task/bin/etc/config в файле broker.xml вывести значение параметра из
<log>
<level>значение</level>
</log>
В каталоге opt/upiter/plot/task/doka/_config в файле doka.ini вывести значение параметров из
[LOGS]
IS_SQL_LOG =значение,
IS_CEF_LOG =значение,
IS_DBG_LOG =значение
В каталоге opt/upiter/plot/task/doka/_config в файле doka.log.json вывести значение из
{level: значение,
}
Режим 2. Установка максимального уровня логирования
В каталоге opt/upiter/plot/task/bin/etc/config во всех файлах по маске имени "*.json" установить
значения
"log": {
"file": {
"level" : "6"
}}
В каталоге opt/upiter/plot/task/bin/etc/config в файле broker.xml установить значение
<log>
<level>4</level>
</log>
В каталоге opt/upiter/plot/task/doka/_config в файле doka.ini установить значение в секции [LOGS]
параметров
IS_SQL_LOG =y,
IS_CEF_LOG =y,
IS_DBG_LOG =y
При отсутствии любого указанного параметра необходимо его добавить
В каталоге opt/upiter/plot/task/doka/_config в файле doka.log.json установить значение
{level: 6,
}
Open Created 1 hour ago by leshchun

Режим 3. Установка минимального уровня логирования
В каталоге opt/upiter/plot/task/bin/etc/config во всех файлах по маске имени установить
"log": {
"file": {
"level" : "2"
}}
В каталоге opt/upiter/plot/task/bin/etc/config в файле broker.xml установить
<log>
<level>1/level>
</log>
В каталоге opt/upiter/plot/task/doka/_config в файле doka.ini установить значение в секции [LOGS]
параметров
IS_SQL_LOG =n,
IS_CEF_LOG =n,
IS_DBG_LOG =n
В каталоге opt/upiter/plot/task/doka/_config в файле doka.log.json установить значение
{level: 2,
}
