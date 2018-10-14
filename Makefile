BIN ?= awsec2instances
PREFIX ?= /usr/local

install:
	cp $(BIN).py $(PREFIX)/bin/$(BIN)
	chmod +x $(PREFIX)/bin/$(BIN)
	mkdir $(PREFIX)/bin/$(BIN)_includes
	cp $(BIN)_includes/fn.py $(PREFIX)/bin/$(BIN)_includes/fn.py

uninstall:
	rm -rf $(PREFIX)/bin/$(BIN)
