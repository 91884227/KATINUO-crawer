# KATINUO-crawer

## crawer_for_katino.py
爬取 [卡迪諾新聞的資料](https://ck101.com/)
爬完後生成 katino_data.csv
### usage Parameter
```
python crawer_for_katino.py constrain PROCESS_NUMBER
```

| Parameter | meaning | e.g. |
| -------- | -------- | -------- |
| constrain | 是否限制每個版的最大爬取數 (0: 沒有 1:有) | 0 |
| PROCESS_NUMBER | cpu process的最大數目 | 2 |

### usage example
```
python crawer_for_katino.py  0 2 
```
## find_legal_board.py
### usage Parameter
```
python find_legal_broad.py DERIVER_PATH 
```
> python find_legal_broad.py "C:/Users/Chuck/Desktop/計畫/chromedriver.exe"

| Parameter | meaning | e.g. |
| -------- | -------- | -------- |
| DERIVER_PATH | CHROME PATH     | "C:/Users/Chuck/Desktop/計畫/chromedriver.exe" | 

## usage example
```
python find_legal_broad.py "C:/Users/Chuck/Desktop/計畫/chromedriver.exe"
```


