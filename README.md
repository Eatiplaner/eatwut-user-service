### ✨ Setup Environment

```bash
$ pnpm install
$ pnpm run prepare
$ cp .env.example .env
```

### ✨ Quick Start in `Docker`

```bash
$ docker-compose up --build
```

### ✨ Quick Start in `local`

```bash
$ bin/dev
```

+ Add docs of MongoDB:
```
----- User Documents -----
{
	"_id": {
		"$oid": "62b0ca6b58dada0af5a861b3"
	},
	"first_name": "Paul",
	"last_name": "Miller",
	"user_name": "447557505611",
	"email": "London",
	"password": {
		"$binary": {
			"base64": "YWRtaW4=", //"admin"
			"subType": "00"
		}
	},
	"phone": "447557505611",
	"birthday": {
		"$timestamp": {
			"t": 0,
			"i": 0
		}
	},
	"is_kol": true,
	"useraddress_id": [
		{
			"$oid": "62b0cafc58dada0af5a861b6"
		}
	]
}

----- UserAddress Documents -----
{
	"_id": {
		"$oid": "62b0cafc58dada0af5a861b6"
	},
	"district": "District 1",
	"city": "Ho Chi Minh City",
	"lat": 106.61773467663059,
	"lng": 10.79037499034012,
	"type": "home"
}
```

### ✨ Linting

```bash
$ bin/lint
```
