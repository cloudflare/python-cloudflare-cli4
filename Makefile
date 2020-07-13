
PYTHON = python
PANDOC = pandoc
PYLINT = pylint

EMAIL = "mahtin@mahtin.com"
EMAIL = "martin@cloudflare.com"
NAME = "cloudflare"

all:	README.rst CHANGELOG.md build

README.rst: README.md
	$(PANDOC) --from=markdown --to=rst < README.md > README.rst 

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

sdist: all
	make clean
	make test
	$(PYTHON) setup.py -q sdist
	@rm -rf ${NAME}.egg-info

bdist: all
	make clean
	make test
	$(PYTHON) setup.py -q bdist
	@rm -rf ${NAME}.egg-info

upload: clean all tag upload-github upload-pypi

upload-github:
	git push
	git push origin --tags

upload-pypi:
	$(PYTHON) setup.py -q sdist upload --sign --identity="$(EMAIL)"

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
	python -m cli4 --dump | sed -e 's/^\///' | sort > $$tmp.1 ; \
	python -m cli4 --api | sed -e 's/.* //' -e 's/\/:[^:\/]*//g' -e 's/^\///' | sort | uniq > $$tmp.2 ; \
	echo "In code:" ; \
	diff $$tmp.1 $$tmp.2 | egrep '< ' | sed -e 's/< /         /' | sort ; \
	echo "In docs:" ; \
	diff $$tmp.1 $$tmp.2 | egrep '> ' | sed -e 's/> /         /' | sort ; \
	rm $$tmp.?

clean:
	rm -rf build
	rm -rf dist
	mkdir build dist
	$(PYTHON) setup.py -q clean
	rm -rf ${NAME}.egg-info

