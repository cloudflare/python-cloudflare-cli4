:

#
# A Hack - not worth publishing
#

tmp="/tmp/c$$"
tmp="/tmp/c0"

trap "rm -f ${tmp}_*; exit" 0 1 2 15

if true
then
	curl -s -S https://api.cloudflare.com/ > ${tmp}_api.html
	ls -l ${tmp}_api.html 1>&2
	cp ${tmp}_api.html /tmp/api.html
else
	cp /tmp/api.html ${tmp}_api.html
fi

cat ${tmp}_api.html | sed -e '
s/<\/br>/&\
/g
s/<\/h[0-9]>/&\
/g' | egrep language-http |\
sed -e '
s/\/organization\//\/organizations\//
/GET \/object\/:object_id/d
s/<[^>]*>//g
s/^[ 	]*//
s/\/:[a-z_]*\//\/:identifier\//g
s/\/:[a-z_]*$/\//
s/\/$//' |\
awk '
BEGIN	{
		methods[1] = "GET"
		methods[2] = "PUT"
		methods[3] = "POST"
		methods[4] = "PATCH"
		methods[5] = "DELETE"
	}
/ /	{
		if (match(a[$2],$1)==0) {
			a[$2] = a[$2] " " $1
		}
	}
END	{
			for (m=1;m<=5;m++) {
				printf "|%-8s", "`" methods[m] "`"
			}
			printf "|%-8s|\n", "API Call"
			for (m=1;m<=5;m++) {
				printf "|%-8s", "---"
			}
			printf "|%-8s|\n", ":---"
		for (k in a) {
			for (m=1;m<=5;m++) {
				if (match(a[k], methods[m])) {
					printf "|%-8s", "`" methods[m] "`"
				} else {
					printf "|%-8s", ""
				}
			}
			printf "|%s|\n", k
		}
	}
' | sort -t/ -k2,3

