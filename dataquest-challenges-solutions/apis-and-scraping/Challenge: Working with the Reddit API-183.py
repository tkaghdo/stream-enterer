## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)

python_top = response.json()

## 3. Getting the most upvoted article ##

python_top_articles = python_top["data"]["children"]
most_upvoted_value = -999
most_upvoted = -1
for i in python_top_articles:
    if i["data"]["ups"] > most_upvoted:
        most_upvoted_value = i["data"]["ups"]
        most_upvoted = i["data"]["id"]

## 4. Getting article comments ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
url = "https://oauth.reddit.com/" + "r/" + "python/comments/" + "4b7w9u"
response = requests.get(url,headers=headers)
comments = response.json()

## 5. Getting the most upvoted comment ##

comments_list = comments[1]["data"]["children"]
most_upvoted_comment = ""
most_upvotes_comment = 0
for comment in comments_list:
    co = comment["data"]
    if co["ups"] >= most_upvotes_comment:
        most_upvoted_comment = co["id"]
        most_upvotes_comment = co["ups"]

## 6. Upvoting a comment ##

payload = {"dir": 1, "id": "d16y4ry"}
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.post("https://oauth.reddit.com/api/vote", json=payload, headers=headers)
status = response.status_code