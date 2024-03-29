def main(context):
    if (context.req.path == "/"):
        return context.res.json({"msg": "working, use /subscribe to register users"})
    if (context.req.path == "/dayorder"):
        day_order = day_order_data[context.req.query['date']]["do"]
        context.log(day_order)
        return context.res.json({"msg" : day_order})
    return context.res.json({"msg": "no date provided or invalid path"})

day_order_data = {
    "01-01-24": {
        "do": "nothing"
    },
    "02-01-24": {
        "do": "Day 4"
    },
    "03-01-24": {
        "do": "Day 5"
    },
    "04-01-24": {
        "do": "Day 1"
    },
    "05-01-24": {
        "do": "Day 2"
    },
    "06-01-24": {
        "do": "nothing"
    },
    "07-01-24": {
        "do": "nothing"
    },
    "08-01-24": {
        "do": "Day 3"
    },
    "09-01-24": {
        "do": "Day 4"
    },
    "10-01-24": {
        "do": "Day 5"
    },
    "11-01-24": {
        "do": "Day 1"
    },
    "12-01-24": {
        "do": "Day 2"
    },
    "13-01-24": {
        "do": "nothing"
    },
    "14-01-24": {
        "do": "nothing"
    },
    "15-01-24": {
        "do": "nothing"
    },
    "16-01-24": {
        "do": "nothing"
    },
    "17-01-24": {
        "do": "nothing"
    },
    "18-01-24": {
        "do": "Day 3"
    },
    "19-01-24": {
        "do": "Day 4"
    },
    "20-01-24": {
        "do": "nothing"
    },
    "21-01-24": {
        "do": "nothing"
    },
    "22-01-24": {
        "do": "Day 5"
    },
    "23-01-24": {
        "do": "Day 1"
    },
    "24-01-24": {
        "do": "Day 2"
    },
    "25-01-24": {
        "do": "Day 3"
    },
    "26-01-24": {
        "do": "nothing"
    },
    "27-01-24": {
        "do": "nothing"
    },
    "28-01-24": {
        "do": "nothing"
    },
    "29-01-24": {
        "do": "Day 4"
    },
    "30-01-24": {
        "do": "Day 5"
    },
    "31-01-24": {
        "do": "Day 1"
    },
    "01-02-24": {
        "do": "Day 2"
    },
    "02-02-24": {
        "do": "Day 3"
    },
    "03-02-24": {
        "do": "nothing"
    },
    "04-02-24": {
        "do": "nothing"
    },
    "05-02-24": {
        "do": "Day 4"
    },
    "06-02-24": {
        "do": "Day 5"
    },
    "07-02-24": {
        "do": "Day 1"
    },
    "08-02-24": {
        "do": "Day 2"
    },
    "09-02-24": {
        "do": "Day 3"
    },
    "10-02-24": {
        "do": "nothing"
    },
    "11-02-24": {
        "do": "nothing"
    },
    "12-02-24": {
        "do": "Day 4"
    },
    "13-02-24": {
        "do": "Day 5"
    },
    "14-02-24": {
        "do": "Day 1"
    },
    "15-02-24": {
        "do": "Day 2"
    },
    "16-02-24": {
        "do": "Day 3"
    },
    "17-02-24": {
        "do": "nothing"
    },
    "18-02-24": {
        "do": "nothing"
    },
    "19-02-24": {
        "do": "Day 4"
    },
    "20-02-24": {
        "do": "Day 5"
    },
    "21-02-24": {
        "do": "Day 1"
    },
    "22-02-24": {
        "do": "Day 2"
    },
    "23-02-24": {
        "do": "Day 3"
    },
    "24-02-24": {
        "do": "nothing"
    },
    "25-02-24": {
        "do": "nothing"
    },
    "26-02-24": {
        "do": "Day 4"
    },
    "27-02-24": {
        "do": "Day 5"
    },
    "28-02-24": {
        "do": "Day 1"
    },
    "29-02-24": {
        "do": "Day 2"
    },
    "01-03-24": {
        "do": "Day 3"
    },
    "02-03-24": {
        "do": "nothing"
    },
    "03-03-24": {
        "do": "nothing"
    },
    "04-03-24": {
        "do": "Day 4"
    },
    "05-03-24": {
        "do": "Day 5"
    },
    "06-03-24": {
        "do": "Day 1"
    },
    "07-03-24": {
        "do": "Day 2"
    },
    "08-03-24": {
        "do": "Day 3"
    },
    "09-03-24": {
        "do": "nothing"
    },
    "10-03-24": {
        "do": "nothing"
    },
    "11-03-24": {
        "do": "Day 4"
    },
    "12-03-24": {
        "do": "Day 5"
    },
    "13-03-24": {
        "do": "Day 1"
    },
    "14-03-24": {
        "do": "Day 2"
    },
    "15-03-24": {
        "do": "Day 3"
    },
    "16-03-24": {
        "do": "nothing"
    },
    "17-03-24": {
        "do": "nothing"
    },
    "18-03-24": {
        "do": "Day 4"
    },
    "19-03-24": {
        "do": "Day 5"
    },
    "20-03-24": {
        "do": "Day 1"
    },
    "21-03-24": {
        "do": "Day 2"
    },
    "22-03-24": {
        "do": "Day 3"
    },
    "23-03-24": {
        "do": "nothing"
    },
    "24-03-24": {
        "do": "nothing"
    },
    "25-03-24": {
        "do": "Day 4"
    },
    "26-03-24": {
        "do": "Day 5"
    },
    "27-03-24": {
        "do": "Day 1"
    },
    "28-03-24": {
        "do": "Day 2"
    },
    "29-03-24": {
        "do": "nothing"
    },
    "30-03-24": {
        "do": "nothing"
    },
    "31-03-24": {
        "do": "nothing"
    },
    "01-04-24": {
        "do": "Day 3"
    },
    "02-04-24": {
        "do": "Day 4"
    },
    "03-04-24": {
        "do": "Day 5"
    },
    "04-04-24": {
        "do": "nothing"
    },
    "05-04-24": {
        "do": "nothing"
    },
    "06-04-24": {
        "do": "nothing"
    },
    "07-04-24": {
        "do": "nothing"
    },
    "08-04-24": {
        "do": "nothing"
    },
    "09-04-24": {
        "do": "nothing"
    },
    "10-04-24": {
        "do": "nothing"
    },
    "11-04-24": {
        "do": "nothing"
    },
    "12-04-24": {
        "do": "nothing"
    },
    "13-04-24": {
        "do": "nothing"
    },
    "14-04-24": {
        "do": "nothing"
    },
    "15-04-24": {
        "do": "nothing"
    },
    "16-04-24": {
        "do": "nothing"
    },
    "17-04-24": {
        "do": "nothing"
    },
    "18-04-24": {
        "do": "nothing"
    },
    "19-04-24": {
        "do": "nothing"
    },
    "20-04-24": {
        "do": "nothing"
    },
    "21-04-24": {
        "do": "nothing"
    },
    "22-04-24": {
        "do": "nothing"
    },
    "23-04-24": {
        "do": "nothing"
    },
    "24-04-24": {
        "do": "nothing"
    },
    "25-04-24": {
        "do": "nothing"
    },
    "26-04-24": {
        "do": "nothing"
    },
    "27-04-24": {
        "do": "nothing"
    },
    "28-04-24": {
        "do": "nothing"
    },
    "29-04-24": {
        "do": "nothing"
    },
    "30-04-24": {
        "do": "nothing"
    },
    "01-05-24": {
        "do": "nothing"
    },
    "02-05-24": {
        "do": "nothing"
    },
    "03-05-24": {
        "do": "nothing"
    },
    "04-05-24": {
        "do": "nothing"
    },
    "05-05-24": {
        "do": "nothing"
    },
    "06-05-24": {
        "do": "nothing"
    },
    "07-05-24": {
        "do": "nothing"
    },
    "08-05-24": {
        "do": "nothing"
    },
    "09-05-24": {
        "do": "nothing"
    },
    "10-05-24": {
        "do": "nothing"
    },
    "11-05-24": {
        "do": "nothing"
    },
    "12-05-24": {
        "do": "nothing"
    },
    "13-05-24": {
        "do": "nothing"
    },
    "14-05-24": {
        "do": "nothing"
    },
    "15-05-24": {
        "do": "nothing"
    },
    "16-05-24": {
        "do": "nothing"
    },
    "17-05-24": {
        "do": "nothing"
    },
    "18-05-24": {
        "do": "nothing"
    },
    "19-05-24": {
        "do": "nothing"
    },
    "20-05-24": {
        "do": "nothing"
    },
    "21-05-24": {
        "do": "nothing"
    },
    "22-05-24": {
        "do": "nothing"
    },
    "23-05-24": {
        "do": "nothing"
    },
    "24-05-24": {
        "do": "nothing"
    },
    "25-05-24": {
        "do": "nothing"
    },
    "26-05-24": {
        "do": "nothing"
    },
    "27-05-24": {
        "do": "nothing"
    },
    "28-05-24": {
        "do": "nothing"
    },
    "29-05-24": {
        "do": "nothing"
    },
    "30-05-24": {
        "do": "nothing"
    },
    "31-05-24": {
        "do": "nothing"
    }
}
