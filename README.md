# Secret santa

## 1. Run du script

```bash
source .venv/bin/activate
python3 main.py
```

## 2. Initialisation de l'environnement

### 1. Récupération du dépôt git

```bash
git clone git@github.com:LorianeD/Secret-Santa.git
```

### 2. Dépendances

1. Avec venv

```bash
cd secret-santa
./scripts/build_env.sh
```

2. Sans venv

```bash
cd secret-santa
pip install -r requirements.txt
```

## 3. Customiser les données

Vous pouvez changer les personnes et les couples dans `secretsanta/data.py` avant de lancer le programme.
