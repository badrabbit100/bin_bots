### Взять АПИ API_HASH
Берешь отсюда API_HASH и API_ID
https://my.telegram.org/auth

### Копируем папку и вставляем данные API_HASH
```bash
cp -r obrazec parser2 && cd parser2 && nano .env
```

### Ввести СМС
```bash
python3 main.py
```

### Запустить докер
Измени имя *parser2* на любое другое
```bash
sudo docker build -t parser2 -f Dockerfile . && sudo docker run -it  parser2 &
```

### Проверить парсер
```bash
sudo docker ps
```
### Остановить парсер
```bash
sudo docker stop ID_CONTAINER
```
### Удалить парсер
```bash
rm -r parser2
```
