# BLOCKCHAIN
Learning to build a Blockchain & Cryptocurrency using Python, JS & React.

**Activate The Virtual Environment**
```
source blockchain-env/bin/activate
```

**Install All Packages**
```
pip3 install -r requirements.txt 
```

**Run the Tests**

Make sure to activate the virtual environment first.

```
python3 -m pytest backend/tests
```

**Run the application and API**

```
python3 -m backend.app
```

**Run a Peer Instance**

```
export PEER=True && python3 -m backend.app
```

**Run the Frontend**

In the frontend directory:
```
npm run start
```