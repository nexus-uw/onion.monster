# onion.monster
dynamic dns service attempt to learn pythong

 python manage.py makemigrations
python manage.py migrate

GANDI_KEY=TOTALLY_MY_KEY python manage.py runserver

things to fix
hardcoded domain root
create tokens
handle errors cleaner
handle sub domains?


todo
block subdomains, but put in second wildcard domain record
landing page
register api -> need some sort of auth method to limit this....
ratelimiting
centralized db
client lib
for record should change key to secondary key so that i could be rototated for an account
allow override of ip address (lets one set both ipv4 and 6 at same time)
support TXT record (lets encrypt without public internet? not sure why, but here we are)
do docker secret instead of env