# create a scrip that , what ever is your input they send you to google search

import webbrowser

print("Find your input on internet - google search!!")
query = input("Enter your Google query: ")
url = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % str(query)
webbrowser.open_new(url)