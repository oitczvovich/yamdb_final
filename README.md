![](https://img.shields.io/badge/Python-3.7.5-blue)
![](https://img.shields.io/badge/Django-2.2.16-green)
![](https://img.shields.io/badge/DjangoRestFramework-3.12.4-red)
![](https://img.shields.io/badge/Docker-3.8-yellow)
![example workflow](https://github.com/oitczvovich/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
<br><br>
# YaMDb

## Описание
Ранее мы создали контейнер приложения [api_yamdb](https://github.com/oitczvovich/infra_sp2), образ которого размещен на [Docker Hub](https://hub.docker.com/r/oitczvovich/infra_web/tags).<br>
В данном проекте мы настроили приложения по принципу Continuous Integration и Continuous Deployment, что реализует:
- автоматический запуск тестов,
- обновление образов на Docker Hub,
- автоматический деплой на боевой сервер при пуше в главную ветку main.
  
автор