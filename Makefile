
PYTHON = python
# PANDOC = pandoc
PYLINT = pylint
TWINE = twine

EMAIL = "mahtin@mahtin.com"
NAME = "cloudflare"

OPENAPI_URL = "https://github.com/cloudflare/api-schemas/raw/main/openapi.json"

#all:	README.rst CHANGELOG.md build
all:	CHANGELOG.md build

# README.rst: README.md
# 	$(PANDOC) --wrap=none --from=markdown --to=rst < README.md > README.rst 

CHANGELOG.md: FORCE
	@ tmp=/tmp/_$$$$.md ; \
	( \
		cp /dev/null $$tmp ; \
		echo '# Change Log' ; \
		echo '' ; \
		git log --date=iso-local --pretty=format:' - %ci [%h](../../commit/%H) %s' ; \
		echo '' ; \
	)  >> $$tmp ; \
	diff $$tmp CHANGELOG.md || ( cp $$tmp CHANGELOG.md ; echo "CHANGELOG.md - updated" ) ; \
	rm $$tmp
FORCE:

build: setup.py
	$(PYTHON) setup.py -q build

install: build
	sudo $(PYTHON) setup.py -q install
	sudo rm -rf ${NAME}.egg-info

test: all
#	 to be done

cli4test: all
	$(PYTHON) -m cli4 /ips > /dev/null

sdist: all
	make clean
	make test
	$(PYTHON) setup.py -q sdist
	$(TWINE) check dist/*
	@rm -rf ${NAME}.egg-info

bdist: all
	make clean
	make test
	$(PYTHON) setup.py -q bdist
	$(TWINE) check dist/*
	@rm -rf ${NAME}.egg-info

bdist_wheel: all
	make clean
	make test
	$(PYTHON) setup.py -q bdist_wheel
	$(TWINE) check dist/*
	@rm -rf ${NAME}.egg-info

upload: clean all tag upload-github upload-pypi

upload-github:
	git push
	git push origin --tags

upload-pypi:
	## $(PYTHON) setup.py -q sdist bdist_wheel upload # --sign --identity="$(EMAIL)"
	$(TWINE) upload -r pypi dist/*

showtag: sdist
	@ v=`ls -r dist | head -1 | sed -e 's/cloudflare-\([0-9.]*\)\.tar.*/\1/'` ; echo "\tDIST VERSION =" $$v ; (git tag | fgrep -q "$$v") && echo "\tGIT TAG EXISTS"

tag: sdist
	@ v=`ls -r dist | head -1 | sed -e 's/cloudflare-\([0-9.]*\)\.tar.*/\1/'` ; echo "\tDIST VERSION =" $$v ; (git tag | fgrep -q "$$v") || git tag "$$v"

sign:
	v=`ls -r dist | head -1 | sed -e 's/cloudflare-\([0-9.]*\)\.tar.*/\1/'` ; echo "\tDIST VERSION =" $$v ; \
	mkdir -p tarball ; \
	rm -f tarball/$$v.tar.gz.asc tarball/$$v.zip.asc ; \
	curl -sS -o tarball/$$v.tar.gz https://codeload.github.com/cloudflare/python-cloudflare/tar.gz/$$v ; \
	curl -sS -o tarball/$$v.zip https://codeload.github.com/cloudflare/python-cloudflare/zip/$$v ; \
	gpg --default-key ${EMAIL} --armor --detach-sign tarball/$$v.tar.gz ; \
	gpg --default-key ${EMAIL} --armor --detach-sign tarball/$$v.zip ; \
	ls -l tarball/$$v.tar.gz tarball/$$v.zip ; \
	ls -l tarball/$$v.tar.gz.asc tarball/$$v.zip.asc ;

lint:
	$(PYLINT) CloudFlare cli4

api:
	@tmp=/tmp/_$$$$_ ; \
	$(PYTHON) -m cli4 --dump | sort > $$tmp.1 ; \
	$(PYTHON) -m cli4 --api | sed -e 's/^[A-Z][A-Z]*  *//' -e 's/?.*//' -e 's/\/:[a-z][A-Za-z_]*/\/:id/g' -e 's/\/:[a-z][A-Za-z_]*}/\/:id/g' -e 's/:id\/:id/:id/' -e 's/\/:id$$//' -e 's/\/:id$$//' -e 's/\/:id ;/ ;/' -e 's/\/$$//' | sort -u > $$tmp.2 ; \
	egrep -v '; deprecated' < $$tmp.2 | diff $$tmp.1 - > $$tmp.3 ; \
	echo "In code:" ; \
	egrep '< ' < $$tmp.3 | sed -e 's/< /    /' | sort | tee $$tmp.4 ; \
	echo "In docs:" ; \
	egrep '> ' < $$tmp.3 | sed -e 's/> /    /' | sort | sed -e "s/\//self.add('AUTH', '/" -e "s/$$/'\)/" -e "s/\/:id\//', '/g" ; \
	echo "Deprecated:" ; \
	egrep '; deprecated' < $$tmp.2 | while read cmd x deprecated deprecated_date ; do egrep "$$cmd" $$tmp.4 | sed -e "s/$$/ ; deprecated $$deprecated_date/" ; done | sort | uniq ; \
	rm $$tmp.?

openapi:
	@tmp=/tmp/_$$$$_ ; \
	$(PYTHON) -m cli4 --dump | sort > $$tmp.1 ; \
	$(PYTHON) -m cli4 --openapi $(OPENAPI_URL) | sed -e 's/^[A-Z][A-Z]*  *//' -e 's/?.*//' -e 's/\/:[a-z][A-Za-z_]*/\/:id/g' -e 's/\/:[a-z][A-Za-z_]*}/\/:id/g' -e 's/:id\/:id/:id/' -e 's/\/:id$$//' -e 's/\/:id$$//' -e 's/\/:id ;/ ;/' -e 's/\/$$//' | sort -u > $$tmp.2 ; \
	egrep -v '; deprecated' < $$tmp.2 | diff $$tmp.1 - > $$tmp.3 ; \
	echo "In code:" ; \
	egrep '< ' < $$tmp.3 | sed -e 's/< /    /' | sort | tee $$tmp.4 ; \
	echo "In docs:" ; \
	egrep '> ' < $$tmp.3 | sed -e 's/> /    /' | sort | sed -e "s/\//self.add('AUTH', '/" -e "s/$$/'\)/" -e "s/\/:id\//', '/g" ; \
	echo "Deprecated:" ; \
	egrep '; deprecated' < $$tmp.2 | while read cmd x deprecated deprecated_date ; do egrep "$$cmd" $$tmp.4 | sed -e "s/$$/ ; deprecated $$deprecated_date/" ; done | sort | uniq ; \
	rm $$tmp.?

TUNA_CLI4_TEST_COMMAND = "/ips"
TUNA_CLI4_TEST_COMMAND = "--api"
TUNA_CLI4_TEST_COMMAND = "--openapi $(OPENAPI_URL)"

tuna:
	@tmp=/tmp/_$$$$_ ; \
	$(PYTHON) -X importtime -m cli4 $(TUNA_CLI4_TEST_COMMAND) > /dev/null 2> $$tmp.1 ; \
	tuna $$tmp.1 2> /dev/null & \
	tunapid=$$! ; \
	sleep 1 ; \
	kill $$tunapid ; \
	rm $$tmp.?

clean:
	rm -rf build
	rm -rf dist
	mkdir build dist
	$(PYTHON) setup.py -q clean
	rm -rf ${NAME}.egg-info

