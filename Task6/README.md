# Условия задачи
1. Запустить браузерные тесты задачи 5 в Selenoid 
  a. Использовать браузеры: Chrome, Firefox и Opera.  
  b. Описать процесс разворачивания Selenoid, настройки и конфигурирования, запуск тестов во всех браузерах. 
2. Развернуть Jenkins и выстроить pipeline из тестов 
  a. Развернуть систему CI Jenkins на виртуальной машине Linux (*или в Docker)  
  b. Создать задачу типа Pipeline 
  c. Описать скрипт Jenkinsfile с обязательными шагами `api-test`, `ui-test`, где описан запуск тестов задачи 4 и 5 соответственно. 
  d. *После прохождения тестов, в системе должны отображаться отчеты о прохождении тестов, привести пример. 
  e. *Запуск тестов выполнить в docker-контейнерах, дать описание преимуществ подхода.
  f. Описать процесс разворачивания Jenkins сервера, создание задачи и ее настройку, работу с Jenkinsfile, настройку отчетов, запуску pipeline. В описании показать получившийся 
Jenkinsfile. 
 
# Окружение для запуска
* Установка была произведена на Ubuntu 19.04
* Python 2.x или Python 3.x
* Python-pip
* Docker

# Задача 1
## Установка Selenoid
Скачать Configuration Manager
```
curl -s https://aerokube.com/cm/bash | bash
```
Подготовить конфигурационный файл browser.json
```
{
    "firefox": {
        "default": "67.0",
        "versions": {
            "67.0": {
                "image": "selenoid/vnc:firefox_67.0",
                "port": "4444",
                "path": "/wd/hub"
            }
        }
    }
}
{
    "chrome": {
        "default": "74.0",
        "versions": {
            "74.0": {
                "image": "selenoid/vnc:chrome_74.0",
                "port": "4444",
                "path": "/wd/hub"
            }
        }
    }
}
{
    "opera": {
        "default": "58.0",
        "versions": {
            "58.0": {
                "image": "selenoid/vnc:opera_58.0",
                "port": "4444",
                "path": "/wd/hub"
            }
        }
    }
}
```
Скачать образы браузеров
```
docker pull selenoid/vnc:firefox_67.0
docker pull selenoid/vnc:chrome_74.0
docker pull selenoid/vnc:opera_58.0
```
Запуск Selenoid
```
./cm selenoid start --vnc
```
Запуск Selenoid UI. Selenoid UI подключается к порту VNC и показывает что происходит с браузером
```
./cm selenoid-ui start
```
