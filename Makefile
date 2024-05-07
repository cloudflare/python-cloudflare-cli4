
PYTHON = python
# PANDOC = pandoc
PYLINT = pylint
TWINE = twine
PYTEST = pytest

SPHINX_RELEASE = 2.20.0
SPHINX_AUTHOR = Martin J. Levy
SPHINX_COPYRIGHT = Copyright (c) 2016 thru 2024, Cloudflare. All rights reserved.

EMAIL = "mahtin@mahtin.com"
NAME = "cloudflare"

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
	@if pip show pytest-cov > /dev/null; \
	then \
		if [ ! -s .coverage ] ; then touch -t 202001011200 .coverage ; fi ; \
		if [ `find CloudFlare CloudFlare/tests cli4 examples pyproject.toml -type f -depth 1 -name '*.py' -newer .coverage | wc -l` != 0 ]; \
		then \
			echo $(PYTEST) --cov=CloudFlare ; \
			$(PYTEST) --cov=CloudFlare ; \
			coverage html ; \
		else \
			true ; \
		fi ; \
	else \
		echo $(PYTEST) -vv ; \
		$(PYTEST) -vv ; \
	fi

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
	$(TWINE) upload -r pypi --repository cloudflare dist/*

showtag: sdist
	@ v=`ls -r dist | head -1 | sed -e 's/cloudflare-\([0-9.]*\)\.tar.*/\1/'` ; echo "\tDIST VERSION =" $$v ; (git tag | fgrep -q "$$v") && echo "\tGIT TAG EXISTS"

tag: sdist
	@ v=`ls -r dist | head -1 | sed -e 's/cloudflare-\([0-9][0-9.][0-9]*[.rc0-9]*\)\.tar.*/\1/'` ; echo "\tDIST VERSION =" $$v ; (git tag | fgrep -q "$$v") || git tag "$$v"

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

docs: all
	@mkdir -p docs/_build docs/_static
	sphinx-apidoc --force --module-first --separate --ext-autodoc -A "$(SPHINX_AUTHOR)" -R "$(SPHINX_RELEASE)" -V "$(SPHINX_RELEASE)" -o docs . 'setup.*'
	sphinx-build -a -E -j auto -b html docs docs/_build/html

clean-docs: all
	rm -rf docs/CloudFlare*.rst docs/cli4*.rst docs/examples*.rst docs/modules*.rst docs/_build docs/_static

lint:
	$(PYLINT) CloudFlare cli4

openapi:
	@tmp=/tmp/_$$$$_ ; \
	$(PYTHON) -m cli4 --dump | sort > $$tmp.1 ; \
	$(PYTHON) -m cli4 --openapi '' | tee $$tmp.5 | sed -e 's/^[A-Z][A-Z]*  *//' -e 's/?.*//' -e 's/\/:[a-z][A-Za-z_]*/\/:id/g' -e 's/\/:[a-z][A-Za-z_]*}/\/:id/g' -e 's/:id\/:id/:id/' -e 's/\/:id$$//' -e 's/\/:id$$//' -e 's/\/:id ;/ ;/' -e 's/ ; Content-Type: .*//' -e 's/\/$$//' | sort -u > $$tmp.2 ; \
	egrep -v '; deprecated' < $$tmp.2 | sed -e 's/ ; .*//' | diff $$tmp.1 - > $$tmp.3 ; \
	echo "In code:" ; \
	egrep '< ' < $$tmp.3 | sed -e 's/< /    /' | sort | tee $$tmp.4 ; \
	echo "In docs:" ; \
	egrep '> ' < $$tmp.3 | sed -e 's/> /    /' | sort | sed -e "s/\//self.add('AUTH', '/" -e "s/$$/'\)/" -e "s/\/:id\//', '/g" ; \
	echo "Deprecated:" ; \
	egrep '; deprecated' < $$tmp.2 | while read cmd x deprecated deprecated_date ; do egrep "$$cmd" $$tmp.4 | sed -e "s/$$/ ; deprecated $$deprecated_date/" ; done | sort | uniq ; \
	echo "Content-Type's:" ; \
	egrep ';' < $$tmp.5 | egrep -v '; deprecated' | egrep -v ' ; Content-Type: application/json' | sed -e 's/^/    /' ; \
	rm $$tmp.?

TUNA_CLI4_TEST_COMMAND = "--openapi="
TUNA_CLI4_TEST_COMMAND = "/ips"

tuna:
	@tmp=/tmp/_$$$$_ ; \
	$(PYTHON) -X importtime -m cli4 $(TUNA_CLI4_TEST_COMMAND) > /dev/null 2> $$tmp.1 ; \
	tuna $$tmp.1 2> /dev/null & \
	tunapid=$$! ; \
	sleep 10 ; \
	kill $$tunapid ; \
	rm $$tmp.?

clean:
	rm -rf build
	rm -rf dist
	mkdir build dist
	$(PYTHON) setup.py -q clean
	rm -rf ${NAME}.egg-info

