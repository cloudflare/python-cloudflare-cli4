:

tmp="/tmp/c$$"
tmp="/tmp/c0"

# trap "rm -f ${tmp}_*; exit" 0 1 2 15

(sed -e 's/#.*//' | egrep setattr) < ../CloudFlare/api_v4.py | egrep -v self._unused | cut -d, -f4,5,6 | sed -e 's/^ "/\//' -e 's/", "/\/:identifier\//g' -e 's/"))$//' | sort -u > ${tmp}_1
if false
then
	curl -s -S https://api.cloudflare.com/ > ${tmp}_api.html
else
	cp /tmp/api.html ${tmp}_api.html
fi
egrep 'language-http' < ${tmp}_api.html | sed -e 's/\/organization\//\/organizations\//' -e '/GET \/object\/:object_id/d' -e 's/<[^>]*>//g' -e 's/^[ 	]*//' -e 's/\/:[a-z_]*\//\/:identifier\//g' -e 's/\/:[a-z_]*$/\//' -e 's/\/$//' | tee ${tmp}_3 |  awk '{print $2}' | sort -u > ${tmp}_2

echo "< GitHUb vs > Documentation"

diff ${tmp}_1 ${tmp}_2

