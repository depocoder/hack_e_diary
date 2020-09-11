# hack_e_diary

## Описание проекта.   

Этот проект позволяет исправить ваши тройки и двойки на пятерки, удалить все замечания, добавить комментарии похвалы от учителей.   
Для того чтобы провернуть подобное у вашего учереждения должен быть дневник, как в этом [репозитории](https://github.com/devmanorg/e-diary/tree/master).
Так же вам надо как-то попасть на сервер вашего учереждения, возможно вы узнаете ssh ключ или сможете пробраться к серверам, так же есть у вас есть доступ к файлу базы данных.

## Полезные ссылки.
[**Репозиторий дневника**](https://github.com/devmanorg/e-diary/tree/master)    
[**Пример базы данных дневника**](https://dvmn.org/filer/canonical/1562234129/166/)   
[**Как подключить к ssh серверу linux**](https://1cloud.ru/help/linux/podkljuchenie-ssh-linux)   
[**Основы SSH**](https://www.youtube.com/watch?v=sbVYRf_6Hvg)

## Измение базы данных.  

 **Настоятельно рекомендую попробовать сначала на своем компьютере!**
 
Вам нужно попасть в папку самого электронного дневника.   
Если вы только пробуете изменить базу на своем компьютере не забудьте установить сам дневник и пример базы данных.   
Она выглядит примерно так.   
![](https://i.imgur.com/oGnCYWT.png) 

### Linux, Mac Os:
```Bash
sudo apt-get install git 
sudo apt-get install python3
git clone https://github.com/herypank/hack_e_diary
python3 manage.py shell 
from hack_e_diary.script import fix_everything
fix_everything("")
``` 
*В кавычках указываете ФИО, например "Фролов Иван".*
Далее скрипт сам подскажет что вводить.    
**НЕ ЗАБУДЬТЕ ПОСЛЕ ИСПОЛЬЗОВАНИЯ УДАЛИТЬ ПАПКУ hack_e_diary**.   
`rm -rf hack_e_diary`
