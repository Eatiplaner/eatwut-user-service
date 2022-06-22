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

### ✨ Quick Start in `mongodb_local`

```bash
$ mongo "mongodb://{user_mongo}:{pass_mongo}@localhost:27017"
$ use eatiplaner-user-service
$ load("database/migrations/db.js")
```

### ✨ Linting

```bash
$ bin/lint
```
