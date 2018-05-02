# Dirty hack to get emails of members out of Yahoo Groups
#
# Written to get the B3ta newsletter out of Yahoo Groups
# by http://twitter.com/robmanuel
#
# It uses Python to spin up Chrome,
# logs in and then calls the internal API that 
# makes the members page and then spits out a load
# of json files which you can fiddle with or grep.
#
# As I said, this aint pretty but it got a job done
# and might be useful to someone with same problem.
# 
# grep -E -o "\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b" *txt | uniq | sort
# useful grep to get the emails out
#
# and another to count them as a bit of a sanity check
# grep -E -o "\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b" *txt | uniq | sort | wc -l
#

