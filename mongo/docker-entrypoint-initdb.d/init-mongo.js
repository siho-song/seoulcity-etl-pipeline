db.createUser(
    {
        user: "show",
        pwd: "gkdldhdl",
        roles: [
            { role: "userAdmin", db: "seoulcity" },
            { role: "dbAdmin", db: "seoulcity" },
            { role: "readWrite", db: "seoulcity" }
        ]
    }
);
