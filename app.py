data = [
        # data[0]
        (
            [
                # x[0]
                (
                    "target_room",
                    'closed-mongodb',
                    0
                ),
                # x[1]
                (
                    "target_room",
                    'deleted-mongodb',
                    0
                )
            ]
        ),
        # data[1]
        (
            [
                # x[0]
                (
                    "non_target_room",
                    'closed-mysql',
                    0
                ),
                # x[1]
                (
                    "target_room",
                    'deleted-mysql',
                    0
                )
            ]
        ),
    ]

result = [x[0] for x in data]
print(result)
