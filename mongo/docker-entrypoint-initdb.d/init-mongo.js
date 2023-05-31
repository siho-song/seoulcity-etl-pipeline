db.createUser(
    {
        user: "show",
        pwd: "gkdldhdl",
        roles: [
            { role: "userAdmin", db: "admin" },
            { role: "dbAdmin", db: "admin" },
            { role: "readWrite", db: "admin" }
        ]
    }
);
