# mse1h2024-moodle

## Сборщик активности moodle

### Подключение

Для того, чтобы подключить отслеживание действий на странице, необходимо:
1. Войти в moodle в учетную запись администратора 
2. Перейти во вкладку администрирования сайта ("Site administration")
3. Выбрать раздел "Внешний вид"("Appearance")
4. Выбрать пункт "Дополнительный HTML"("Additional HTML")
5. Вставить в окно `When BODY is opened` код из файла `moodle_stat_tracker_*`
6. В самом низу страницы нажать зеленую кнопку сохранения изменений

С этого момента сборщик активности работает и отслеживает действия всех пользователей на странице.

### Конфигурация подключенного скрипта

```html
<script type="module">
    var interactions = new Interactor({
        trackAll: true,
        interactions: true,
        interactionElement: [],
        interactionEvents: ["mousedown"],
        conversions: true,
        conversionElement: "conversion",
        conversionEvents: ["mouseup", "touchend"],
        endpoint: '/',
        async: true,
        debug: false
    });
</script>
```

Настройка происходит с помощью изменения значений в полях куска кода трекера, который расположен выше.

 - `trackAll` $-$ при установке значения `true` будет отслеживать любое взаимодействие со страницей.
 - `interactionElement` $-$ определяет элементы которые необходимо отслеживать. Для установки нужно внутри квадратных скобок написать название элемента большими буквами в кавычках. (Например
 `interactionElement: ["DIV"]`, будет отслеживать любое взамодействие с элементами `div`).
 - `interactionEvents` $-$ определяет действия которые нужно отслеживать (нажатие мыши, отпускание мыши, клик мыши и т.д.). По умолчанию будет использоваться нажатие мыши. Значения внутри квадратных скобок должны быть написаны строчными буквами в кавычках, как это показано выше.
 - `endpoint` $-$ определяет куда будут отправлены результаты. По умолчанию там будет находится сервер приложения, но при необходимости можно изменить. Нужно лишь прописать путь куда должны отправляться данные.
 - `debug` $-$ необходимо лишь для дальнейшей разработки. По умолчанию будет `false`.

Трекер отслеживания перехода на другую вкладку представлен в файле `moodle_stat_tracker_focus_on_tab`. Данный скрипт отслеживает *только* переключение на другую вкладку браузера и обратно. Никакие другие действия зарегистрированы на данный момент не будут. - на текущий момент не отработает, требует доработки модели.
