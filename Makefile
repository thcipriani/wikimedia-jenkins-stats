all: index.html

serve: all
	python2 -m SimpleHTTPServer

index.html: README.md
	pandoc -i $< -o $@

.PHONY: all serve
