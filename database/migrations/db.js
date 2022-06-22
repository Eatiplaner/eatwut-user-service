/*--- Create Collection User ---*/
db.createCollection("user", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["_id", "username", "password", "is_kol", "first_name", "last_name", "email", "phone"],
            properties: {
                _id: {
                    bsonType: "objectId",
                },
                username: {
                    bsonType: "string",
                    description: "required and unique"
                },
                password: {
                    bsonType: "string",
                    description: "required, have MD5 hash and auto generated salt (process in logic), strong password recommended"
                },
                is_kol: {
                    bsonType: "bool",
                    description: "required"
                },
                first_name: {
                    bsonType: "string",
                    description: "required"
                },
                last_name: {
                    bsonType: "string",
                    description: "required"
                },
                email: {
                    bsonType: "string",
                    pattern: '[a-z0-9._%+!$&*=^|~#%{}/-]+@([a-z0-9-]+.){1,}([a-z]{2,22})',
                    description: "required, unique, must following email pattern"
                },
                phone: {
                    bsonType: "string",
                    description: "required"
                },
                birthday: {
                    bsonType: "timestamp"
                }
            }
        }
    }
})

/*--- Create Collection UserAdress ---*/
db.createCollection("user_address", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["_id", "user_id"],
            properties: {
                _id: {
                    bsonType: "objectId",
                },
                user_id: {
                    bsonType: "objectId",
                    description: "unique with collection User"
                },
                lat: {
                    bsonType: "double",
                    description: "latitude"
                },
                lng: {
                    bsonType: "double",
                    description: "longitude"
                },
                street: {
                    bsonType: "string"
                },
                ward: {
                    bsonType: "string"
                },
                district: {
                    bsonType: "string"
                },
                city: {
                    bsonType: "string"
                },
                zipcode: {
                    bsonType: "string"
                },
                nationnal: {
                    bsonType: "string"
                },
                type: {
                    bsonType: "string"
                }
            }
        }
    }
})

/* Set Unique */
db.user.createIndex({"username": 1}, {unique: true})
db.user.createIndex({"email": 1}, {unique: true})
db.user_address.createIndex({"user_id": 1}, {unique: true})

/*--- Sample Data ---*/
/* Password meaning: md5_hash("salt" + "password") = md5_hash("123keysalt" + "superadmin") = md5_hash("123keysaltsuperadmin") */
/* Birthday meaning: 2022-06-21 */
db.user.insertOne(
    {
        _id: ObjectId("62b360fe472914ef678899e1"),
        username: "superadmin",
        password: "d48a277c162f7ff86f374e8d21134fb5",
        is_kol: true,
        first_name: "Super",
        last_name: "Admin",
        email: "superadmin@eatiplaner.com",
        phone: "0987654321",
        birthday: Timestamp(1655769600, 1),
    }
)

db.user_address.insertOne(
    {
        _id: ObjectId("62b36112472914ef678899e4"),
        user_id: ObjectId("62b360fe472914ef678899e1"),
        lat: 10.787368734509503,
        lng: 106.69160103615961,
        street: "Nam Kỳ Khởi Nghĩa",
        ward: "Bến Thành",
        district: "Quận 1",
        city: "Thành phố Hồ Chí Minh",
        zipcode: "70000",
        nationnal: "Việt Nam",
        type: "home"
    }
)