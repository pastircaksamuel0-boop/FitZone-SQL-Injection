# FitZone – SQL Injection Demo

## 1. O projekte

FitZone je jednoduchá demonštračná webová aplikácia simulujúca internetový obchod so športovou výživou a fitness príslušenstvom.

Aplikácia umožňuje vyhľadávať produkty v databáze SQLite prostredníctvom webového rozhrania. Jej účelom je demonštrovať zraniteľnosť **SQL Injection (SQLi)** a ukázať, ako môže nesprávne spracovanie používateľského vstupu ovplyvniť SQL dotazy.

Aplikácia je určená výhradne na vzdelávacie a testovacie účely.

## 2. Použité technológie

- **Python 3** – aplikačná logika
- **Flask** – webový framework
- **SQLite** – databáza produktov
- **HTML** – štruktúra webovej stránky
- **CSS** – vizuálne spracovanie
- **JavaScript** – komunikácia medzi webovým rozhraním a serverom

## 3. Štruktúra projektu

```text
SQLi-Lab/
│
├── api.py
├── data.db
├── index.html
├── requirements.txt
├── LICENSE
│
├── static/
│   ├── style.css
│   └── js/
│       └── submit.js
│
└── venv/
```

## 4. Spustenie aplikácie

Aplikácia bola testovaná v prostredí Ubuntu 20.04 LTS.

### Vytvorenie virtuálneho prostredia

```bash
python3 -m venv venv
```

### Aktivácia virtuálneho prostredia

```bash
source venv/bin/activate
```

### Inštalácia závislostí

```bash
pip install -r requirements.txt
```

### Spustenie servera

```bash
python api.py
```

Po spustení je aplikácia dostupná v prehliadači na adrese:

`http://127.0.0.1:5000`

## 5. Databáza

Aplikácia využíva databázu SQLite (`data.db`), ktorá obsahuje tabuľku `data` s nasledujúcimi atribútmi:

| Atribút | Typ | Popis |
|---|---|---|
| id | INTEGER | Identifikátor produktu |
| name | TEXT | Názov produktu |
| category | TEXT | Kategória produktu |
| price | REAL | Cena produktu |
| description | TEXT | Popis produktu |

Databáza obsahuje päť fiktívnych produktov z oblasti športovej výživy a fitness príslušenstva.

## 6. SQL Injection – zraniteľné miesto

Zraniteľnosť sa nachádza v serverovej časti aplikácie, konkrétne v endpoint-e `/search`.

Používateľský vstup sa priamo vkladá do SQL dotazu pomocou spájania textových reťazcov:

```python
statement = "SELECT * FROM data WHERE name LIKE '%" + name + "%'"
c.execute(statement)
```

Takýto spôsob spracovania vstupu umožňuje útočníkovi ovplyvniť výslednú SQL syntax.

Aplikácia nepoužíva parametrizovaný SQL dotaz, a preto je zraniteľná voči SQL Injection.

## 7. Demonštrácia útoku

Pri bežnom vyhľadávaní používateľ zadá názov produktu, napríklad:

`Whey`

Aplikácia následne zobrazí zodpovedajúci produkt z databázy.

Na demonštráciu SQL Injection bol použitý nasledujúci vstup:

```sql
' OR 1=1 -- 
```

Tento vstup upraví podmienku SQL dotazu tak, že sa stane vždy pravdivou. Znaková sekvencia `--` zároveň zakomentuje zvyšok pôvodného SQL dotazu.

Výsledkom je obídenie pôvodného filtra vyhľadávania a zobrazenie všetkých piatich produktov z databázy.

## 8. Možnosť odstránenia zraniteľnosti

Zraniteľnosť je možné odstrániť použitím parametrizovaných SQL dotazov, pri ktorých sa používateľský vstup odovzdáva databáze oddelene od SQL príkazu.

Príklad bezpečnejšej implementácie:

```python
statement = "SELECT * FROM data WHERE name LIKE ?"
c.execute(statement, ('%' + name + '%',))
```

Takýto prístup zabraňuje tomu, aby databáza interpretovala používateľský vstup ako súčasť SQL syntaxe.

## 9. Upozornenie

Aplikácia obsahuje zámerne vytvorenú bezpečnostnú zraniteľnosť. Je určená výhradne na lokálne testovanie, vzdelávanie a demonštráciu SQL Injection.

Nemala by byť nasadzovaná ako verejne dostupná produkčná aplikácia.

## 10. Pôvod a licencia

Projekt vychádza z demonštračnej aplikácie:

https://github.com/vivek3141/sql-injection-demo

Pôvodný projekt bol upravený a rozšírený o vlastné prostredie e-shopu FitZone, databázu produktov a upravené webové rozhranie.

Pôvodná licencia MIT a informácie o autorstve sú zachované v súbore `LICENSE`.
