# CI/CD pipeline

[Источник](https://habr.com/ru/companies/jugru/articles/505994/ "Статья с hubr'а, которая описывает мою затею")

_Практическое применение знаний о CI/CD, для их последующего закрепления_
___

![Изображение](https://habrastorage.org/getpro/habr/upload_files/fd5/8e7/aed/fd58e7aed7c9aa1cc417ffaf2d315561.png "CI/CD pipeline")


#### Ожидаемый результат

Автоматизация процесса
1. Таски в JIRA
2. Сборка билда
3. Запуск тестов
4. Выпуск релиза
5. Анотация PR
6. Деплой

Идея будет реализована в рамках github actions без использования travis, jenkins, terraform и прочих сторонних сервисов.