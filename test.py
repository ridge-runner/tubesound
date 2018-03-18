# Just a throw-away file to test the readline fuctionself.
# Goal: read text to list obj.

path = "/home/bvandyke/proj/src/github.com/ridge-runner/tubesound/url-list.txt"

url_list = []

with open(path, "r") as urls:
    urls = urls.readlines()
    urls = [x.strip() for x in urls]
    url_list = urls

del url_list[0:2] #clean up instructions on url list text file.

print('The Completed List:\n\n')
print(url_list)
