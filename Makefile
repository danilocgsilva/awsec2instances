BIN ?= awsec2instances
PREFIX ?= /usr/local

install:
	cp $(BIN).py $(PREFIX)/bin/$(BIN)
	chmod +x $(PREFIX)/bin/$(BIN)

uninstall:
	rm -f $(PREFIX)/bin/$(BIN)
