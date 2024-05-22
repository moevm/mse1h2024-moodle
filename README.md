# mse1h2024-moodle

## Сборщик активности moodle
## Результаты итераций
### Итерация 4
1. [Презентация с результатами итерации](https://github.com/moevm/mse1h2024-moodle/wiki/Итерация4#презентация)
2. [Скринкаст с демонстрацией фич](https://github.com/moevm/mse1h2024-moodle/wiki/Итерация4#скринкаст-с-демонстрацией-фич)
3. [Описание тестов](https://github.com/moevm/mse1h2024-moodle#тестирование-приложения)
### Итерация 3
1. [Презентация с результатами итерации](https://github.com/moevm/mse1h2024-moodle/wiki/Итерация3#презентация)
2. [Подробный план итерации](https://github.com/moevm/mse1h2024-moodle/wiki/Итерация4#план-на-итерацию-4)
3. [Скринкаст с демонстрацией фич](https://github.com/moevm/mse1h2024-moodle/wiki/Итерация3#скринкаст-с-демонстрацией-фич)

### Итерация 2
1. [Презентация с результатами итерации](https://github.com/moevm/mse1h2024-moodle/wiki/Итерация2#презентация)
2. [Скринкаст с демонстрацией фич](https://github.com/moevm/mse1h2024-moodle/wiki/Итерация2#скринкаст-с-демонстрацией-фич)

## Инструкция для работы с программой:
### Варинт 1. 
**Основной при работе с devtools (с помощью которого можно отследить весь функционал собираемой статистики с moevm) - не поднимается moodle и mariadb - порты оставлены открытыми, чтобы можно было отправлять данные статистики с moevm**
1. Сборка проекта

   Для UNIX подобных систем:
   - Находясь в корневой папке проекта запустить скрипт с помощью команды `bash ./init-deploy.sh`. В случае запуска в первый раз, скрипт собирает и поднимает контейнеры, а в случае повторного запуска также останавливает и удаляет всеконтейнеры, а также тома, связанные с ними
   
   Другие системы:
   - Если программа запускается не первый раз и между запусками вносились изменения в исходный код, то необходимо удалить образы и volumes. Важно, что у mongodb два volumes - один с соответствующим названием, другой с идентификатором. Для того, чтобы узнать, какие volumes необходимо удалить использовать следующую команду: `docker inspect mongodb`. Далее с помощью поиска можно найти соответствующие volumes.
   - Для запуска версии проекта необходимо собрать проект с помощью команды `docker-compose build`
   - Далее необходимо поднять контейнеры с помощью команды `docker compose -f .\docker-compose.prod.yaml up`
2. Убедиться, что все контейнеры подняты и по адресу `http://localhost:8081` открывается веб приложение
3. Войти под правами администратора в веб приложение: login - `ivan@mail.ru`,  password - `bhewrtfm3klmt3`
4. Убедиться, что на главное странице просмотра статистики отображены 3 записи - будет означать, что корректно собрана статистика
5. Открыть в браузере https://e.moevm.info/ (для стабильной работы отключить блокировщик рекламы)
6. Перейти в панель исследования элемента ([инструкции для разных браузеров](https://www.businessinsider.com/guides/tech/how-to-inspect-element)), открыть панель console
7. Открыть файл [moodle_stat_tracker_without_script.html](https://github.com/moevm/mse1h2024-moodle/blob/main/stat_tracker/moodle_stat_tracker.html)
8. Скопировать из него содержимое
9. При первом запуске или если еще никгда не выполнялось далее в панели "Исследование элемента" в браузере разрешить копирование кода с помощью команды `allow paste`
10. После чего скопировать туда скрипт и подтвердить выполненине, нажав кнопку "Enter"
11. Если выполненные на странице действия инициировали переход на другую страницу повторить действия 7-9, 11
12. Вернуться на страницу веб-приложения, обновить страницу статистики и убедиться, что все действия, выполненные Вам добалены в список


### Варинт 2. 
**Требует проверки от администратора moevm Основной при работе с панелью администратора на moevm (с помощью которого можно отследить весь функционал собираемой статистики с moevm) - не поднимается moodle и mariadb - порты оставлены открытыми, чтобы можно было отправлять данные статистики с moevm**
Повторить действия 1 - 5 из Варианта 1

6. Открыть файл [moodle_stat_tracker.html](https://github.com/moevm/mse1h2024-moodle/blob/main/stat_tracker/moodle_stat_tracker_without_script.html)
7. Далее в соответствие с  инструкцией "Подключение" ниже необходимо вставить скрипт для отслеживания действий пользователей, не забыть подтвердить вставку
8. Выполнить действия
9. Перейти в веб приложение для отслеживания собранных действий


### Вариант 3.
**Отладочный**
1. Для запуска версии проекта необходимо собрать проект с помощью команды `docker-compose build`, после чего поднять его с помощью команды `docker-compose up`
2. Далее необходимо запустить moodle по адресу `http://localhost`
3. В moodle необходимо авторизоваться с использованием `user = "user", password = "bitnami"`
4. Далее в соответствие с  инструкцией "Подключение" ниже необходимо вставить скрипт из ветки `#137-local-moodle-tracker` для отслеживания действий пользователей, не забыть подтвердить вставку
5. Далее необходимо запустить web-приложение с по адресу `http://localhost:8081`
6. Войти под данными: login - `ivan@mail.ru`,  password - `bhewrtfm3klmt3`
7. В главном окне веб приложения отобразится собранная статистика

Для проверки работы с бд можно воспользоваться API через swagger по адресу: `http://localhost:8080/docs`




## Подключение

Для того, чтобы подключить отслеживание действий на странице, необходимо:
1. Войти в moodle в учетную запись администратора 
2. Перейти во вкладку администрирования сайта ("Site administration")
3. Выбрать раздел "Внешний вид"("Appearance")
4. Выбрать пункт "Дополнительный HTML"("Additional HTML")
5. Вставить в окно `When BODY is opened` код из файла `moodle_stat_tracker.html`
6. В самом низу страницы нажать кнопку сохранения изменений

С этого момента сборщик активности работает и отслеживает действия всех пользователей на странице.

### Конфигурация подключенного скрипта
**!!Важно для сбора статистики с пользователей, работающих за другими компьютерами необходимо поменять localhost на реальный адрес поднятого сервера**


```html
 function initTracker(){
        var interactions = new Interactor({
        trackAll: false,
        numberActionsToSend: 5,
        trackPagePresence: true,
        interactions: true,
        interactionElement: ["A", "BUTTON", "TEXTAREA", "INPUT"],
        interactionEvents: ["mousedown", "copy", "paste"],
        conversions: true,
        conversionElement: "conversion",
        conversionEvents: ["scroll", "contextmenu"],
        endpoint: 'http://localhost:8080/api/statistics',
        async: true,
        debug: true
    });
    }
```

Настройка происходит с помощью изменения значений в полях куска кода трекера, который расположен выше.

 - `trackAll` $-$ при установке значения `true` будет отслеживать любое взаимодействие со страницей.
 - `numberActionsToSend` $-$ Определяет число действий пользователя которые нужно отправлять за итерацию. По умолчанию отсылается по 5 действий пользователя, но можно изменить это значение.
 - `trackPagePresence` $-$ при установке значения `true` будет отслеживать переход с отслеживаемой вкладки на другую.
 - `interactionElement` $-$ определяет элементы которые необходимо отслеживать. Для установки нужно внутри квадратных скобок написать название элемента большими буквами в кавычках. (Например
 `interactionElement: ["DIV"]`, будет отслеживать любое взамодействие с элементами `div`). По умолчанию отслеживаются взаимодействия с элементами `A`, `BUTTON`, `TEXTAREA`, `INPUT`. 
 - `interactionEvents` $-$ определяет действия которые нужно отслеживать (нажатие мыши, отпускание мыши, клик мыши и т.д.). По умолчанию будет использоваться нажатие мыши, копирование в буфер обмена и вставка из буфера обмена. Значения внутри квадратных скобок должны быть написаны строчными буквами в кавычках, как это показано выше.
 - `endpoint` $-$ определяет куда будут отправлены результаты. По умолчанию там будет находится сервер приложения, но при необходимости можно изменить. Нужно лишь прописать путь куда должны отправляться данные.
 - `debug` $-$ необходимо лишь для дальнейшей разработки. По умолчанию будет `false`.

Проверка работоспособности сервера и базы данных осуществляется с помощью следующей функции:
 ```html
 healthCheck(3)
```  
Инициализация трекера происходит только при успешной проверке.
Количество повторных попыток подключения указывается в вызове функции healthCheck() (по умолчанию 3).
При исчерпании попыток подключения мудл работает в штатном режиме, как будто скрипт не подключался.

В ветке `main` находится скрипт, работающий на e.moevm.info (для работы через devtools необходимо использовать файл moodle_stat_tracker_without_script.html)

В ветке `#137-local-moodle-tracker` находится версия скрипта для работы с локальной чистой версией moodle.

### Требования к браузерам

В настоящее время Interactor поддерживает современные браузеры: Chrome, Firefox и Safari. Приветствуется дополнительное тестирование и ввод данных.

[Оригинальный источник](https://github.com/greenstick/interactor?tab=readme-ov-file#documentation)

### Тестирование приложения

Подробное описание по запуску тестирований описано на [wiki-страничке](https://github.com/moevm/mse1h2024-moodle/wiki/%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
